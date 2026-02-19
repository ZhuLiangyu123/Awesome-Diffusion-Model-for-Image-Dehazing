# This is the code for calculating SAM, ERGAS, UIQI, QNR, BRISQUE, NIQE, PSNR, SSIM, CIEDE2000, LPIPS, and FID.


import os
import cv2
import lpips
import torch
import argparse
import numpy as np
from scipy import stats
from scipy.linalg import sqrtm
from skimage import color, metrics
from scipy.ndimage import gaussian_filter
from sklearn.metrics import mean_squared_error
from skimage.metrics import structural_similarity as ssim
from torchvision.models import Inception_V3_Weights


# SAM
def calculate_sam(image1, image2):
    img1 = image1.astype(np.float64)
    img2 = image2.astype(np.float64)
    eps = 1e-8
    dot = np.sum(img1 * img2, axis=2)
    norm1 = np.linalg.norm(img1, axis=2)
    norm2 = np.linalg.norm(img2, axis=2)
    cos = dot / (norm1 * norm2 + eps)
    cos = np.clip(cos, -1, 1)
    sam = np.mean(np.arccos(cos))
    return np.degrees(sam)


# ERGAS
def calculate_ergas(image1, image2, ratio=1):
    img1 = image1.astype(np.float64)
    img2 = image2.astype(np.float64)
    mean_ref = np.mean(img2, axis=(0, 1))
    rmse = np.sqrt(np.mean((img1 - img2) ** 2, axis=(0, 1)))
    ergas = 100 / ratio * np.sqrt(np.mean((rmse / (mean_ref + 1e-8)) ** 2))
    return ergas


# UIQI
def calculate_uiqi(image1, image2):
    img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    h, w, c = img1.shape
    win_size = 7
    if min(h, w) < win_size:
        win_size = min(h, w) // 2 * 2 + 1
    return ssim(img1, img2, channel_axis=2, win_size=win_size)


# QNR
def calculate_qnr(image1, image2):
    sam_val = calculate_sam(image1, image2)
    ergas_val = calculate_ergas(image1, image2)
    return np.exp(-sam_val / 10) * np.exp(-ergas_val / 100)


# BRISQUE
def calculate_brisque(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).astype(np.float32)
    mu = gaussian_filter(gray, sigma=1)
    mu_sq = mu ** 2
    sigma = np.sqrt(np.abs(gaussian_filter(gray ** 2, sigma=1) - mu_sq))
    eps = 1e-8
    mscn = (gray - mu) / (sigma + eps)
    alpha = np.mean(np.abs(mscn))
    beta = np.std(mscn)
    score = alpha + beta
    return score


# NIQE
def calculate_niqe(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).astype(np.float32)
    gray = (gray - np.mean(gray)) / (np.std(gray) + 1e-8)
    mu = cv2.GaussianBlur(gray, (7, 7), 7 / 6)
    sigma = np.sqrt(np.abs(cv2.GaussianBlur(gray ** 2, (7, 7), 7 / 6) - mu ** 2))
    mscn = (gray - mu) / (sigma + 1)
    shape, loc, scale = stats.gennorm.fit(mscn.flatten())
    niqe_score = np.abs(shape) + np.abs(scale)
    return niqe_score


# PSNR
def calculate_psnr(image1, image2):
    mse = mean_squared_error(image1.flatten(), image2.flatten())
    return 20 * np.log10(255.0 / np.sqrt(mse))


# SSIM
def calculate_ssim(image1, image2):
    img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    h, w, c = img1.shape
    win_size = 7
    if min(h, w) < win_size:
        win_size = min(h, w) // 2 * 2 + 1
    return metrics.structural_similarity(img1, img2, channel_axis=2, win_size=win_size)


# CIEDE2000
def calculate_ciede2000(img1, img2):
    lab1 = color.rgb2lab(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    lab2 = color.rgb2lab(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    delta_e = color.deltaE_ciede2000(lab1, lab2)
    return np.mean(delta_e)


# LPIPS
def calculate_lpips(img1, img2, lpips_model=None):
    if lpips_model is None:
        lpips_model = lpips.LPIPS(net='alex')
    img1_t = torch.from_numpy(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)).permute(2, 0, 1).unsqueeze(0).float() / 127.5 - 1.0
    img2_t = torch.from_numpy(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)).permute(2, 0, 1).unsqueeze(0).float() / 127.5 - 1.0
    with torch.no_grad():
        d = lpips_model(img1_t, img2_t)
    return d.item()


# FID
def calculate_fid(imgs1, imgs2):
    from torchvision.models import inception_v3
    from torchvision import transforms
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = inception_v3(weights=Inception_V3_Weights.IMAGENET1K_V1, transform_input=False).to(device)
    model.fc = torch.nn.Identity()
    model.eval()
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((299, 299)),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    def get_features(imgs):
        feats = []
        with torch.no_grad():
            for img in imgs:
                img_t = preprocess(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).unsqueeze(0).to(device)
                feat = model(img_t).cpu().numpy().reshape(-1)
                feats.append(feat)
        return np.array(feats)
    act1 = get_features(imgs1)
    act2 = get_features(imgs2)
    mu1, sigma1 = act1.mean(axis=0), np.cov(act1, rowvar=False)
    mu2, sigma2 = act2.mean(axis=0), np.cov(act2, rowvar=False)
    diff = mu1 - mu2
    covmean = sqrtm(sigma1.dot(sigma2))
    if np.iscomplexobj(covmean):
        covmean = covmean.real
    fid = diff.dot(diff) + np.trace(sigma1 + sigma2 - 2 * covmean)
    return fid


def load_images_from_folder(folder, file_names):
    images = []
    for filename in file_names:
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


def resize_to_match(img1, img2):
    h, w = img2.shape[:2]
    return cv2.resize(img1, (w, h), interpolation=cv2.INTER_CUBIC)


def main(train_folder, target_folder):
    train_images = sorted(os.listdir(train_folder))
    target_images = sorted(os.listdir(target_folder))
    sam, ergas, uiqi, qnr, brisque, niqe, psnr, ssim, ciede, lpips_list = [], [], [], [], [], [], [], [], [], []
    lpips_model = lpips.LPIPS(net='alex')
    imgs1, imgs2 = [], []

    for train_img, target_img in zip(train_images, target_images):
        train_image = cv2.imread(os.path.join(train_folder, train_img))
        target_image = cv2.imread(os.path.join(target_folder, target_img))

        if train_image.shape != target_image.shape:
            train_image = resize_to_match(train_image, target_image)

        sam.append(calculate_sam(train_image, target_image))
        ergas.append(calculate_ergas(train_image, target_image))
        uiqi.append(calculate_uiqi(train_image, target_image))
        qnr.append(calculate_qnr(train_image, target_image))
        brisque.append(calculate_brisque(train_image))
        niqe.append(calculate_niqe(train_image))
        psnr.append(calculate_psnr(train_image, target_image))
        ssim.append(calculate_ssim(train_image, target_image))
        ciede.append(calculate_ciede2000(train_image, target_image))
        lpips_list.append(calculate_lpips(train_image, target_image, lpips_model))

        imgs1.append(train_image)
        imgs2.append(target_image)

    print(f"SAM: {np.mean(sam):.3f}")
    print(f"ERGAS: {np.mean(ergas):.3f}")
    print(f"UIQI: {np.mean(uiqi):.3f}")
    print(f"QNR: {np.mean(qnr):.3f}")
    print(f"BRISQUE: {np.mean(brisque):.3f}")
    print(f"NIQE: {np.mean(niqe):.3f}")
    print(f"PSNR: {np.mean(psnr):.3f}")
    print(f"SSIM: {np.mean(ssim):.3f}")
    print(f"CIEDE2000: {np.mean(ciede):.3f}")
    print(f"LPIPS: {np.mean(lpips_list):.3f}")

    fid = calculate_fid(imgs1, imgs2)
    print(f"FID: {fid:.3f}")


if __name__ == "__main__":
    train_folder = r"E:\AAA"       # Dehazing result
    target_folder = r"E:\GT"       # GT
    main(train_folder, target_folder)
