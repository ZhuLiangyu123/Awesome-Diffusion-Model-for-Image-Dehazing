# Awesome-Diffusion-Model-for-Image-Dehazing
We aim to provide a comprehensive summary of papers and code related to image dehazing based on diffusion models, to help interested individuals quickly understand and practice in this field.

However, due to individual limitations in energy and expertise, some researchers' work may inevitably not be taken into account. We welcome researchers to leave their recent work in the Issues section, and we will update this page as soon as possible.


## Cite US
If this work is helpful to you, we expect you can cite this work and star this repository. Thanks!
```
title={Diffusion Models and Its Applications in Image Dehazing: A Survey},
author={Liangyu Zhu, Yanzhao Su, Zhigao Cui, Yunwei Lan, Nian Wang, Lanqing Zhang, Yanping Cai},
journal={IET Image Processing},
year={2026}
```

## Image Dehazing Datasets
We summarize the datasets for image dehazing and provide detailed descriptions of each dataset. The summary and description of these datasets are under continuous update. The image dehazing datasets can be found [here](https://github.com/ZhuLiangyu123/Awesome-Image-Dehazing-Datasets).


## Image Quality Assessment Metrics
For images with ground truth, we provide the calculation methods of PSNR, SSIM, and LPIPS [here](https://github.com/ZhuLiangyu123/Awesome-Diffusion-Model-for-Image-Dehazing/blob/main/Calculate_PSNR_SSIM_LPIPS.py).


## Diffusion Models for Image Dehazing
| |Publication|Year|Method|Paper Title|First Author|Code Link|
|:-:|:-:|:-:|-|:-:|:-:|:-:|
|1|MMSP|2024|KCDiff|Robust Real-World Image Dehazing via Knowledge Guided Conditional Diffusion Model Finetuning|Haoran Wei|-|
|2|ECCV|2024|DiffLI<sup>2</sup>D|Unleashing the Potential of the Semantic Latent Space in Diffusion Models for Image Dehazing|Zizheng Yang|-|
|3|IEEE TITS|2024|RSHazeDiff|RSHazeDiff: A Unified Fourier-aware Diffusion Model for Remote Sensing Image Dehazing|Jiamei Xiong|[Code](https://github.com/jm-xiong/RSHazeDiff)|
|4|CVIU|2024|DehazeDP|Learning depth-aware decomposition for single image dehazing|Yumeng Kang|[Code](https://github.com/stallak/DehazeDP)|
|5|arXiv|2023|DehazeDDPM|High-quality image dehazing with diffusion model|Hu Yu|[Code](https://github.com/yuhuUSTC/DehazeDDPM)|
|6|Neural Networks|2024|HazeAug|Frequency compensated diffusion model for real-scene dehazing|Jing Wang|[Code](https://github.com/W-Jilly/frequency-compensated-diffusion-model-pytorch)|
|7|CGF|2024|DADM|Density‐Aware Diffusion Model for Efficient Image Dehazing|Ling Zhang|[Code](https://github.com/benchacha/DADM)|
|8|ICIC|2024|MP-DDPM|A Multi-scale Patch Approach with Diffusion Model for Image Dehazing|Yao Guo|-|
|9|ICIP|2024|-|Clouds and Haze Co-Removal Based on Weight-Tuned Overlap Refinement Diffusion Model for Remote Sensing Images|Jingxuan Zhang|-|
|10|ISCAS|2024|DehazeDiff|DehazeDiff: When Conditional Guidance Meets Diffusion Models for Image Dehazing|Longyu Cheng|-|
|11|SMC|2023|DehazeDM|DehazeDM: Image dehazing via patch autoencoder based on diffusion models|Yuming Yang|-|
|12|GRSL|2023|ARDD-Net|Remote sensing image dehazing using adaptive region-based diffusion models|Yufeng Huang|-|
|13|GRSL|2024|ADND-Net|Diffusion models based null-space learning for remote sensing image dehazing|Yufeng Huang|-|
|14|CCC|2024|FP-Diff|Frequency-based and Physics-guiding Diffusion Model for Single Image Dehazing|Siying Xie|-|
|15|ICIGP|2024|-|Image Dehazing based on Iterative-Refining Diffusion Model|Jiarong Wang|-|
|16|ICMA|2024|DTDM|Image Dehazing Method Based on Diffusion Model|Fengxu Guan|-|
|17|TGRS|2024|-|Integrated Methodology for Atmospheric Correction and Cloud Removal of Multispectral Remote Sensing Images Using Guided Diffusion Model|Anran Li|-|
|18|TCSVT|2025|DMSR|When Aware Haze Density Meets Diffusion Model for Synthetic-to-Real Dehazing|Shibai Yin|-|
|19|ICASSP|2024|Diff-HOD|Diff-HOD: Diffusion Model for Object Detection in Hazy Weather Conditions|Yizhan Li|-|
|20|AAAI|2025|Diff-Dehazer|Exploiting Diffusion Prior for Real-World Image Dehazing with Unpaired Training|Yunwei Lan|[Code](https://github.com/ywxjm/Diff-Dehazer)|
|21|ICLR|2025|DiffAD|Addressing domain shift with diffusion-based adaptation for real image dehazing|Zixuan Chen|-|
|22|APSIPA ASC|2024|-|Enhanced RefineDNet for Single Image Dehazing|Jingyu Ren|-|
|23|arXiv|2025|DiffDehaze|Learning Hazing to Dehazing: Towards Realistic Haze Generation for Real-World Image Dehazing|Ruiyi Wang|[Code](https://github.com/ruiyi-w/Learning-Hazing-to-Dehazing)|
|24|NeurIPS|2024|-|Exploring Fixed Point in Image Editing: Theoretical Support and Convergence Optimization|Chen Hang|-|
|25|arXiv|2025|IDDM|IDDM: Bridging Synthetic-to-Real Domain Gap from Physics-Guided Diffusion for Real-world Image Dehazing|Shijun Zhou|-|
|26|SPL|2025|KDDM|Scene Text Detection in Foggy Weather Utilizing Knowledge Distillation of Diffusion Models|Zhaoxi Liu|-|
|27|TGRS|2025|MS-FODN|Collaboration of Dehazing and Object Detection Tasks: A Multi-Task Learning Framework for Foggy Image|Yu Wan|-|
|28|MoSICom|2024|RD-DDPM|Revamped Lane detection in hazy environments using Denoising Diffusion Probabilistic Model|Sivakumar Palanirajan|-|
|29|arXiv|2025|FDG-Diff|FDG-Diff: Frequency-Domain-Guided Diffusion Framework for Compressed Hazy Image Restoration|Ruicheng Zhang|[Code](https://github.com/SYSUzrc/FDG-Diff)|
|30|ICME|2025|ProDehaze|ProDehaze: Prompting Diffusion Models Toward Faithful Image Dehazing|Tianwen Zhou|[Code](https://github.com/TianwenZhou/ProDehaze)|
|31|arXiv|2025|BeyondHaze|Seeing Beyond Haze: Generative Nighttime Image Dehazing|Beibei Lin|-|
|32|ICMLC|2024|UnDiff|Uncertainty-Aware Diffusion Model for Real-World Image Dehazing|YuanJian Qiao|-|
|33|ICCV|2025|-|When Schrödinger Bridge Meets Real-World Image Dehazing with Unpaired Training|Yunwei Lan|-|
|34|arXiv|2025|FrDiff|Frequency Domain-Based Diffusion Model for Unpaired Image Dehazing|Chengxu Liu|-|
|35|Signal Image Video P|2025|DehazeDiff|DehazeDiff: Image Dehazing via Mask-guided Diffusion Model|Liqun Luo|-|
|36|ESWA|2025|-|Efficient image dehazing via temporal-aware diffusion|Haobo Liang|[code](https://github.com/fatsotiger/E_Diff_dehaze)|
|37|Opt. Laser Technol.|2025|-|Adaptive dual-domain-guided semantics diffusion model for image defogging|Shaohui Jin|-|

## Diffusion Models for All-in-One Image Restoration (Including Dehazing)
| |Publication|Method|Paper Title|First Author|Code Link|
|:-:|:-:|:-:|-|:-:|:-:|
|1|VISUAL COMPUT 2024|UTDM|UTDM: a universal transformer-based diffusion model for multi-weather-degraded images restoration|Yongbo Yu|[Code](https://github.com/RHEPI/UTDM)|
|2|IEEE TPAMI 2023|WeatherDiff|Restoring vision in adverse weather conditions with patch-based denoising diffusion models|Ozan Özdenizci|[Code](https://github.com/IGITUGraz/WeatherDiffusion)|
|3|TMM 2024|WaveDM|Wavedm: Wavelet-based diffusion models for image restoration|Yi Huang|[Code](https://github.com/stayalive16/WaveDM)|
|4|arXiv 2024|GenDeg|GenDeg: Diffusion-Based Degradation Synthesis for Generalizable All-in-One Image Restoration|Sudarshan Rajagopalan|[Code](https://github.com/sudraj2002/GenDeg)|
|5|ECCV 2024|AutoDIR|Autodir: Automatic all-in-one image restoration with latent diffusion|Yitong Jiang|[Code](https://github.com/jiangyitong/AutoDIR)|
|6|arXiv 2024|FoundIR|FoundIR: Unleashing Million-scale Training Data to Advance Foundation Models for Image Restoration|Hao Li|[Code](https://github.com/House-Leo/FoundIR)|
|7|CVPR 2024|DiffUIR|Selective Hourglass Mapping for Universal Image Restoration Based on Diffusion Model|Dian Zheng|[Code](https://github.com/iSEE-Laboratory/DiffUIR)|
|8|arXiv 2023|IR-SDE|Image restoration with mean-reverting stochastic differential equations|Ziwei Luo|[Code](https://github.com/Algolzw/image-restoration-sde)|
|9|CVPR 2023|Refusion|Refusion: Enabling large-size realistic image restoration with latent-space diffusion models|Ziwei Luo|[Code](https://github.com/Algolzw/image-restoration-sde)|
|10|arXiv 2024|-|Consistent Diffusion: Denoising Diffusion Model with Data-Consistent Training for Image Restoration|Xinlong Cheng|-|
|11|ACCV 2024|DiffLoss|DiffLoss: unleashing diffusion model as constraint for training image restoration network|Jiangtong Tan|-|
|12|arXiv 2024|JCDM|Joint Conditional Diffusion Model for Image Restoration with Mixed Degradations|Yufeng Yue|-|
|13|CVPR 2024|DTPM|Learning Diffusion Texture Priors for Image Restoration|Tian Ye|-|
|14|CVPR 2024|DiffTTA|Genuine Knowledge from Practice: Diffusion Test-Time Adaptation for Video Adverse Weather Removal|Yijun Yang|[Code](https://github.com/scott-yjyang/DiffTTA)|
|15|arXiv 2024|CFMW|CFMW: Cross-modality Fusion Mamba for Multispectral Object Detection under Adverse Weather Conditions|Haoyuan Li|[Code](https://github.com/lhy-zjut/CFMW)|
|16|MMM 2025|TDM|TDM: Temporally-Consistent Diffusion Model for All-in-One Real-World Video Restoration|Yizhou Li|[Code](https://github.com/Yizhou-Li-CV/TDM)|
|17|CVPR 2024|TextualDeg Removal|Improving image restoration through removing degradations in textual representations|Jingbo Lin|[Code](https://github.com/mrluin/TextualDegRemoval)|
|18|arXiv 2024|Instruct-IPT|Instruct-ipt: All-in-one image processing transformer via weight modulation|Yuchuan Tian|[Code](https://github.com/huawei-noah/Pretrained-IPT)|
|19|CVPR 2024|Diff-Plugin|Diff-Plugin：Revitalizing Details for Diffusion-based Low-level Tasks|Yuhao Liu|[Code](https://github.com/yuhaoliu7456/Diff-Plugin/)|
|20|arXiv 2024|Diff-Restorer|Diff-restorer: Unleashing visual prompts for diffusion-based universal image restoration|Yuhong Zhang|-|
|21|arXiv 2023|VIDiff|Vidiff: Translating videos via multi-modal instructions with diffusion models|Zhen Xing|[Code](https://github.com/ChenHsing/VIDiff)|
|22|PR 2025|PhyDiff|Learning physical-aware diffusion priors for zero-shot restoration of scattering-affected images|Yuanjian Qiao|-|
|23|AAAI 2025|Up-Restorer|Up-Restorer: When Unrolling Meets Prompts for Unified Image Restoration|Minghao Liu|-|
|24|arXiv 2023|SUD&sup2;|SUD&sup2;: Supervision by Denoising Diffusion Models for Image Reconstruction|Matthew A Chan|-|

