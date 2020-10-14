import pandas as pd
import numpy as np
import datetime
from PIL import Image
import os
import re
import gc
import random
import json

all_image_filenames = []
images_directory = './Nitrogen_Images'
output_all_image_filenames = './all_image_filenames.csv'

for root, dirnames, filenames in os.walk(images_directory):
    for filename in [filename for filename in filenames if filename.endswith('.png') and filename.startswith('crop_VIS_SV')]:
        all_image_filenames.append(os.path.join(root, filename))

pd_all_image_filenames = pd.DataFrame(all_image_filenames)
pd_all_image_filenames.to_csv(output_all_image_filenames, sep=',', header=None, index=False)