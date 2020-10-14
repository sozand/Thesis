import cv2
import pandas as pd
import numpy as np
import tensorflow as tf
import datetime
from PIL import Image
from crop_image import crop
from show_image import plot_image
import os
import re
import gc
import random
import json
from shutil import copyfile
import time
start_time = time.time()


all_image_filenames = []
images_directory = './Nitrogen_Images'
output_all_image_filenames = './all_image_filenames.csv'
window=1300
start_x = 580
start_y = 360

for root, dirnames, filenames in os.walk(images_directory):
  #print(root)
  for filename in [filename for filename in filenames if filename.endswith('.png') and filename.startswith('VIS_SV')]:
    # for filename in [filename for filename in filenames if filename.endswith('.png')]:
    #     all_image_filenames.append(os.path.join(root, filename))
    img = cv2.imread(os.path.join(root, filename))
    crop(img,start_x,start_y,window,window,root,filename,mode='save_crop')

print("--- %s seconds ---" % (time.time() - start_time))