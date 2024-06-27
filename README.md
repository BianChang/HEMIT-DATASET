# Introduction to the HEMIT Dataset

**Note**: This documentation is prepared for double-blind review. I confirm that no identifying information is included. This document is intended to help reviewers understand the scope and content of the HEMIT dataset. The final version of the file, will be released upon the camera-ready version of the paper.

## Overview

The HEMIT dataset is tailored for image-to-image stain translation. It contains cellular-wise registered H&E and mIHC image pairs, derived from the same sectioning approach to ensure high alignment quality. The raw data is sourced from the ImmunoAIzer work [1], which includes 8 whole slide images (WSIs) from colon cancer patients.


## Dataset Details

- **Number of Samples**:
  - **Train**: 3717
  - **Validation**: 630
  - **Test**: 945
- **Image Patch Size**: 1024x1024 pixels
- **mIHC Image Channels**: 3-channel: DAPI, panCK, CD3
- **Image Format**: TIF

## File Structure

  ```    
  HEMIT
├── test
│   ├── input
│   │   ├── [7941,48408]_patch_0_0.tif
│   │   ├── [7941,48408]_patch_0_1.tif
│   │   ├── [7941,48408]_patch_0_2.tif
│   │   └── ...
│   ├── label
│   │   ├── [7941,48408]_patch_0_0.tif
│   │   ├── [7941,48408]_patch_0_1.tif
│   │   ├── [7941,48408]_patch_0_2.tif
│   │   └── ...
├── val
│   ├── input
│   │   ├── [12146,53552]_patch_0_0.tif
│   │   ├── [12146,53552]_patch_0_1.tif
│   │   ├── [12146,53552]_patch_0_2.tif
│   │   └── ...
│   ├── label
│   │   ├── [12146,53552]_patch_0_0.tif
│   │   ├── [12146,53552]_patch_0_1.tif
│   │   ├── [12146,53552]_patch_0_2.tif
│   │   └── ...
├── train
│   ├── input
│   │   ├── [6407,49798]_patch_0_0.tif
│   │   ├── [6407,49798]_patch_0_1.tif
│   │   ├── [6407,49798]_patch_0_2.tif
│   │   └── ...
│   ├── label
│   │   ├── [6407,49798]_patch_0_0.tif
│   │   ├── [6407,49798]_patch_0_1.tif
│   │   ├── [6407,49798]_patch_0_2.tif
│   │   └── ...


  ```
Corresponding images in a pair are of the same size and have the same filename, e.g., `/HEMIT/train/input/[6407,49798]_patch_0_0.tif` is considered to correspond to `/HEMIT/train/label/[6407,49798]_patch_0_0.tif`.

## Evaluation Metrics

We use several evaluation metrics to assess the performance of our model:

- **SSIM (Structural Similarity Index)**: Measures the similarity between two images, focusing on changes in structural information, luminance, and contrast.
- **Pearson Correlation**: Evaluates the linear relationship between the generated and real datasets, providing a measure of how closely the generated data matches the real data in terms of linear correlation.
- **PSNR (Peak Signal-to-Noise Ratio)**: Quantifies the quality of the generated images compared to the real images, with higher values indicating better quality and less noise.


The overall training and testing scheme follows the general structure of pix2pix [2]

## Code Availability

The code for implementation of the dual-branch method can be accessed at: [Anonymous code for paper review](https://anonymous.4open.science/r/HEMIT-DualBranch-Blind/).

Note that the code is for review purposes only and we will release the final version upon camera-ready version of the paper.

## References

[1] Bian, Chang, et al. "ImmunoAIzer: a deep learning-based computational framework to characterize cell distribution and gene mutation in tumour microenvironment." Cancers 13.7 (2021): 1659.

[2] Isola, Phillip, et al. "Image-to-image translation with conditional adversarial networks." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.

