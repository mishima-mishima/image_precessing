# -*- coding: utf-8 -*-
import os
import shutil
import cv2
import sys

def sampling(video_file, image_dir='image/', image_file='img_%s.png', frame_rate=30):
    # Delete the entire directory tree if it exists.
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)

    # Make the directory if it doesn't exist.
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Video to frames
    i = 0
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read() # Capture frame-by-frame
        if flag == False:  # Is a frame left?
            break
        if i%frame_rate==0:
            cv2.imwrite(image_dir+image_file % str(int(i/frame_rate)).zfill(6), frame)  # Save a frame
            print('Save', image_dir+image_file % str(int(i/frame_rate)).zfill(6))
        i += 1

    cap.release()  # When everything done, release the capture

def main():
  sampling('sample.mp4')
if __name__ == "__main__":
    main()
