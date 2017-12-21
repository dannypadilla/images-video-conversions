'''
This program converts a set of images to a video file of a specified format

* 1. Choose whether to convert from:
* # a. Images to Video
* # b. Video to Images
* 2. Specify file(s) location by:
* # a. Putting file(s) in tmp_files folder (DEFAULT)
* # b. Specifying path ("c:/file/is/here")
* 3. Specify the desired format for the output file
* # A. Supported VIDEO format:
* # # i.   MJPG - .mp4 (preferred for OSX)
* # # ii.  DIVX - .avi (preferred for WINDOWS)
* # # iii. X264 - .mkv
* # B. Supported IMAGE format:
* # # i.   .jpeg
* # # ii.  .tiff
* # # iii. .bmp
* # # iv.  .png
* # # v.   .gif
* 4. Specify frame size
* # a. Value must be >= 1.0

Usage:
  main.py [<args_tbd>]

  Output is created in created_files folder
'''

import numpy as np
import cv2
import os
import sys

path_to_images = ""
name_to_new_file = ""
fps = "" # has to be >= 1.0

front_slash = "/" # for now



# **************************************************************** #

if __name__ == '__main__':

    print(__doc__)

    try:
        fn = sys.argv[1] # unused for now
    except:
        fn = 0

    what = 1
