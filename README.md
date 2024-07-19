![Example Image](images/Cover.png)

## HEMIT Dataset Overview
This dataset is one of the contributions of our paper:  HEMIT: H&E to Multiplex-immunohistochemistry Image Translation with Dual-Branch Pix2pix Generator.

The HEMIT dataset is tailored for image-to-image stain translation. It contains cellular-wise registered H&E and mIHC image pairs, derived from the same sectioning approach to ensure high alignment quality. The raw data is sourced from the ImmunoAIzer work [1], which includes 8 whole slide images (WSIs) from colon cancer patients.

## Dataset Download

We have uploaded the dataset to Mendeley Data platform, it is currently under review by the Mendeley Team, and we will update the download link once the review is complete.

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

The code for implementation of the dual-branch method can be accessed at: [DualBranch_Pix2pix](https://github.com/BianChang/Pix2pix_DualBranch).

## References

[1] Bian, Chang, et al. "ImmunoAIzer: a deep learning-based computational framework to characterize cell distribution and gene mutation in tumour microenvironment." Cancers 13.7 (2021): 1659.

[2] Isola, Phillip, et al. "Image-to-image translation with conditional adversarial networks." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.

## Citation

If you use this code or dataset in your research, please cite our work. The paper has been accepted by the 5th International Workshop on Multiscale Multimodal Medical Imaging (MMMI 2024) and The 1st Workshop on Machine Learning for Multimodal/-sensor Healthcare Data (ML4MHD 2024). 

We will provide full citation details once it is published. Please check back later for the complete citation information.