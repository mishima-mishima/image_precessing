import numpy as np
import matplotlib.pyplot as plt

from skimage import io, data, img_as_float
from skimage.metrics import structural_similarity as ssim


def SSIM(fname_gt, fname_gen):
  gt = io.imread(fname_gt)
  gen = io.imread(fname_gen)

  ssim_result = ssim(gt, gen, data_range=gen.max() - gen.min(), multichannel=True)
  return ssim_result

# usage
def main():

  SSIM_result = SSIM('./samples/gt.jpg', './samples/gen1.jpg')

  print(SSIM_result)

if __name__=='__main__':
  main()
