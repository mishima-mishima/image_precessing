#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image, ImageFilter
import cv2

def divide(image, divide_size=(16, 16)):
  """
  divide input image into any size

  Parameters
  ----------
  image : string
    file name of input image(path)
  divide_size : (int, int)
    the size of after divide image

  Returns
  -------
  divided : numpy.ndarray
    the list of divided image
  """
  im = np.array(Image.open(image))
  (image_height, image_width,channels) = im.shape
  divide_height, divide_width = divide_size

  divide_num_x = int(image_width / divide_width)
  divide_num_y = int(image_height / divide_height)

  divided = []
  for i in range(divide_num_y):
    for j in range(divide_num_x):
      y = i * divide_height
      x = j * divide_width
      divided.append(im[y:y+divide_height,x:x+divide_width,:])

  divided = np.array(divided)
  return divided

def combine(images, divide_size=(16, 16), image_size=(192, 256, 4)):
  """
  combine input image list

  Parameters
  ----------
  images : numpy.ndarray
    the list of divided image
  divide_size : (int, int)
    the size of after divide image
  image_size : (int, int)
    the size of original image

  Returns
  -------
  combined_image : numpy.ndarray
    combined image
  """
  (image_height, image_width,channels) = image_size
  divide_height, divide_width = divide_size

  divide_num_x = int(image_width / divide_width)
  divide_num_y = int(image_height / divide_height)

  combined_image = np.zeros(image_size)
  for i in range(divide_num_y):
    for j in range(divide_num_x):
      y = i * divide_height
      x = j * divide_width
      part = images[0]
      combined_image[y:y+divide_height,x:x+divide_width,:] = part
      images = np.delete(images, 0, 0)

  return combined_image

# usage
def main():
  images = divide('test.png') # divide image
  combined_image = combine(images) # combine image
  combined_image = combined_image[:, :, [2, 1, 0, 3]] # change the order of channels(im this case, this image has 4 channels)
  cv2.imwrite('combined.png', combined_image)

if __name__=='__main__':
  main()