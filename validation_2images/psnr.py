import numpy as np
import matplotlib.pyplot as plt

from skimage import io, data, img_as_float
from skimage.metrics import peak_signal_noise_ratio as psnr


def PSNR(fname_gt, fname_gen):
  gt = io.imread(fname_gt)
  gen = io.imread(fname_gen)

  psnr_result = psnr(gt, gen, data_range=gen.max() - gen.min())
  return psnr_result

# usage
def main():

  PSNR_result = PSNR('./samples/gt.jpg', './samples/gen1.jpg')

  print(PSNR_result)

if __name__=='__main__':
  main()