import os
import pandas as pd

all_image_filenames = pd.read_csv('./all_image_filenames.csv', header=None).values

def search_for_filename(search_filename):
    #print(search_filename)
    for img_path in all_image_filenames:
        #print(img_path[0])
        #print(type(img_path[0]))
        #print(os.path.basename(img_path[0]))
        if os.path.basename(img_path[0]) == search_filename:
            return img_path[0]

    return None