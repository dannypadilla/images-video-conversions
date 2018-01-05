import numpy as np
import cv2
import os
from subprocess import check_output

## need better numbering sorting [currently handles [01, 02, etc..] not [1, 2,.., 10, 11, etc..]
## handle cmd line args; path, file_name, fps... good enough for now tho
## on each frame add frame #, detection, telemetry?, etc.... 
## clean up plz

imgs_path = "./tmp_files/"
file_name = "./created_files/run4_3fps.avi"
fps = 2.0 # has to be >= 1.0

front = "/" # for appending front_slash..... meh

ls = check_output(["ls", imgs_path]).decode("utf8")

print(len(ls))
