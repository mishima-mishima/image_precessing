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
  (image_width, image_height,channels) = im.shape
  divide_width, divide_height = divide_size

  divide_num_x = int(image_width / divide_width)
  divide_num_y = int(image_height / divide_height)

  divided = []
  for i in range(divide_num_x):
    for j in range(divide_num_y):
      x = i * divide_width
      y = j * divide_height
      divided.append(im[x:x+divide_width,y:y+divide_height,:])

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
  (image_width, image_height,channels) = image_size
  divide_width, divide_height = divide_size

  divide_num_x = int(image_width / divide_width)
  divide_num_y = int(image_height / divide_height)

  combined_image = np.zeros(image_size)
  for i in range(divide_num_x):
    for j in range(divide_num_y):
      x = i * divide_width
      y = j * divide_height
      part = images[0]
      combined_image[x:x+divide_width,y:y+divide_height,:] = part
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