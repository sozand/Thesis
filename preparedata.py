import pandas as pd
import numpy as np
import datetime
from PIL import Image
import os
import re
import gc
import random
import json
import time
start_time = time.time()
from find_image_from_name import search_for_filename

#disdir = 'D: / labels /' # files to be moved
#movedir = 'D: / data /' # file path to move

# def copy(dirpath,savepath):
#   filepath=os.listdir(dirpath)
#   #print(filepath)
#   count=255
#   for i in filepath:
#     path1=dirpath+i+'/img.png'
#     path2=dirpath+i+'/label.png'

#     pathsave1=savepath+'/img/'+str(count)+'.png'
#     pathsave2=savepath+'/label/'+str(count)+'.png'

#     shutil.move(path1, pathsave1)
#     shutil.move(path2, pathsave2)
#     count=count+1
# copy(disdir,movedir)
multi_angle=False
crop = True
labels = pd.read_csv('./dataset-stack-info-script.csv', header=None).values


#sort labels into a dictionary of days present in the dataset
days_dict = {}
for label in labels:
    #day = datetime.datetime.strptime(label[2], timestamp_format).date()
    day = label[4]

    if day in days_dict:
        days_dict[day].append(label)
    else:
        days_dict[day] = [label]
print(f"Number of timepoints: {len(days_dict)}...")

# Okay now step through the items in the first day
first_day = min(days_dict.keys())
primaries = days_dict[first_day]

angle_regex = '^VIS_SV_(\d+)_'
all_records = []
for label in primaries:
  snapshot_ID = label[1] #ID สำหรับหาโฟเดอร์รูปภาพ
  barcode = label[2] #ตัวลิ้งต้น เอาไว้ตามการเจริญเติบโต
  IID = label[3] #Plant line สายพันธุ์
  treatment = label[5] #Treatment
  image_filename = label[6] #Stack image file name

  if multi_angle:
      image_angle = re.findall(angle_regex, image_filename)

      if not image_angle:
          # This could be a top-view image, or can't find the angle from the filename.
          continue

      if isinstance(image_angle, list):
          image_angle = image_angle[0]

  all_images = [] #[[file_paht_0_1,file_paht_0_2],[file_paht_1_1,file_paht_1_2],...,[file_paht_18_1,file_paht_18_2]]

  # Step through the days, looking for corresponding images through to the end date.
  for key in sorted(days_dict.keys()):
      records = days_dict[key]
      found = False
      stacked = False

      for record in records:
        r_snapshotID = record[1]
        r_barcode = record[2]
        r_IID = record[3]
        r_treatment = record[5]
        r_fn = record[6]

        if r_fn.startswith('['):
            r_fn = json.loads(r_fn)
            stacked = True

        if multi_angle:
            if ('_'+image_angle+'_' in r_fn) and (r_IID == IID) and (r_treatment == treatment):
                # Got a hit, add it to the list
                found = True
                if crop == True:
                    r_file_path = search_for_filename('crop_'+r_fn)
                else:
                    r_file_path = search_for_filename(r_fn)
                all_images.append(r_file_path)
                break
        else:
            if (r_IID == IID) and (r_barcode == barcode) and (r_treatment == treatment):
                # Got a hit, add it to the list
                found = True

                if stacked:
                    if crop == True:
                        r_file_path = [search_for_filename('crop_'+f) for f in r_fn]
                    else:
                        r_file_path = [search_for_filename(f) for f in r_fn]
                else:
                    if crop == True:
                        r_file_path = search_for_filename('crop_'+r_fn)
                    else:
                        r_file_path = search_for_filename(r_fn)

                all_images.append(r_file_path)
                break

      # By default, just add a None value which we will detect later.
      if not found:
          all_images.append(None)

  if not isinstance(label, list):
      label = label.tolist()

  label.append(all_images) # [id,line*,date=0,treatment*,fileNames, file_path of everyday in the dataset [0-18]]
  all_records.append(label)
pd_all_records = pd.DataFrame(all_records)
pd_all_records.to_csv('./all_records.csv', sep=',', header=None, index=False)
print("--- %s seconds ---" % (time.time() - start_time))