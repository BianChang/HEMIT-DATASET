import os
import numpy as np
import csv
from skimage.io import imread
from skimage.metrics import structural_similarity as ssim, peak_signal_noise_ratio


def compute_metrics(directory_name):
    csv_path = os.path.join(directory_name, 'score.csv')

    with open(csv_path, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([
            'file_name', 'dapi_ssim', 'cd3_ssim', 'panck_ssim', 'average_ssim',
            'dapi_pearson', 'cd3_pearson', 'panck_pearson', 'average_pearson',
            'dapi_psnr', 'cd3_psnr', 'panck_psnr', 'average_psnr'
        ])

        for filename in os.listdir(directory_name):
            if filename.endswith('_fake_B.tif'):
                path_to_file = os.path.join(directory_name, filename)
                fake_image = imread(path_to_file)
                base_name = filename[:-11]
                real_image_name = base_name + 'real_B.tif'
                real_image_path = os.path.join(directory_name, real_image_name)
                real_image = imread(real_image_path)

                # Extract channels
                channels = ['dapi', 'cd3', 'panck']
                ssim_scores = []
                pearson_correlations = []
                psnr_scores = []
                tiny = 1e-15  # tiny constant to avoid numerical issues

                for i, channel in enumerate(channels):
                    real_channel = real_image[:, :, i].astype(float)
                    fake_channel = fake_image[:, :, i].astype(float)

                    # Adding tiny value to avoid zero values which can affect correlation computation
                    real_channel[0, 0] += tiny
                    fake_channel[0, 0] += tiny

                    # Compute SSIM
                    ssim_score = ssim(real_channel, fake_channel, data_range=real_channel.max() - real_channel.min())
                    ssim_scores.append(ssim_score)

                    # Compute Pearson correlation coefficient
                    pearson_corr = np.corrcoef(real_channel.flatten(), fake_channel.flatten())[0, 1]
                    pearson_correlations.append(pearson_corr)

                    # Compute PSNR
                    psnr_score = peak_signal_noise_ratio(real_channel, fake_channel)
                    psnr_scores.append(psnr_score)

                # Calculate averages
                average_ssim = np.mean(ssim_scores)
                average_pearson = np.mean(pearson_correlations)
                average_psnr = np.mean(psnr_scores)

                # Write results to CSV
                csv_writer.writerow([
                    base_name, *ssim_scores, average_ssim,
                    *pearson_correlations, average_pearson,
                    *psnr_scores, average_psnr
                ])
