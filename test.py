from datetime import datetime
from find_image_from_name import search_for_filename

#timestamp = datetime.strptime('2016-06-11 07:01:54', '%Y-%m-%d %H:%M:%S')

img_path = search_for_filename("crop_VIS_SV_0_z750_h1_g0_e85_v500_129461_0.png")
print(img_path)