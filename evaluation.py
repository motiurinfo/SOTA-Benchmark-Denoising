import cv2
import sys
from skimage.metrics import structural_similarity
from skimage.metrics import peak_signal_noise_ratio

def calculate_psnr_ssim(im1,im2):
    img1 = cv2.imread(im1)
    img2 = cv2.imread(im2)
    height = img1.shape[0] # keep original width
    width = 1024
    dim = (width, height)
    # resize image
    img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
    PNSR = peak_signal_noise_ratio(img1, img2)
    SSIM = structural_similarity(img1, img2, multichannel=True)
    return PNSR,SSIM


image1 = sys.argv[1]
image2 = sys.argv[2]

 

PNSR,SSIM = calculate_psnr_ssim(image1,image2)
print("PSNR: " + str(PNSR) + " and SSIM: " + str(SSIM))
