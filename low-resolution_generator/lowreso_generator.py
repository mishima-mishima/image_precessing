import os
import glob
from PIL import Image

ratio = 4 # reduction rate (1/ratio)
image_path = 'images/inputs/*.png' # pass to input images

def downsampling(img):
  input_size, _ = img.size

  # downsampling: nearest
  # upsampling: bicubic
  img_resize = img.resize((int(input_size/ratio), int(input_size/ratio)), Image.BICUBIC)
  img_resize = img_resize.resize((input_size, input_size), Image.BICUBIC)
  return img_resize

  """
  # downsampling: lanczos
  # upsampling: bicubic
  img_resize = img.resize((int(input_size/ratio), int(input_size/ratio)), Image.LANCZOS)
  img_resize = img_resize.resize((input_size, input_size), Image.BICUBIC)
  return img_resize
  """

def main():
  files = glob.glob(image_path)

  for f in files:
    img = Image.open(f)
    img_resize = img.resize((int(img.width / 2), int(img.height / 2)))
    img_resize = downsampling(img)
    title, ext = os.path.splitext(f)
    img_resize.save(title + '_low' + ext)

if __name__ == "__main__":
  main()