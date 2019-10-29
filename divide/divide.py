#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image, ImageFilter
import cv2

# divide
def divide(image, divide_size=(16, 16)):
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

# combine
def combine(images, divide_size=(16, 16), image_size=(192, 256, 4)):
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
  images = divide('test.png')
  combined_image = combine(images)
  combined_image = combined_image[:, :, [2, 1, 0, 3]]
  cv2.imwrite('combined.png', combined_image)

if __name__=='__main__':
  main()