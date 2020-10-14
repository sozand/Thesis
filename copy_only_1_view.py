import pandas as pd
import numpy as np
import datetime
from PIL import Image
import os
import re
import gc
import random
import json
from shutil import copyfile


all_image_filenames = []
images_directory = './Nitrogen_Images'
output_all_image_filenames = './all_image_filenames.csv'

for root, dirnames, filenames in os.walk(images_directory):
  #print(root)
  for filename in [filename for filename in filenames if filename.endswith('.png') and filename.startswith('crop_VIS_SV_0')]:
    # for filename in [filename for filename in filenames if filename.endswith('.png')]:
    #     all_image_filenames.append(os.path.join(root, filename))
    copyfile(os.path.join(root, filename),'/home/sozand/thesis dataset/side_view_only/'+filename)