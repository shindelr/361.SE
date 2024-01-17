# Author: Robin Shindelman
# Date: 2023-01-11
# Description: A script that renames all the files in the images/ 
# directory to be consistent. Took a lot of googling to figure out how to use 
# OS module in this context!

import os


src_dir = './361proj1/images'
img_rename = 'otter_'

# os.listdir() looks up the directory passed to it
all_images = [image for image in os.listdir(src_dir)] 

# Rename all the paths, which consequently renames the target files.
for index, name in enumerate(all_images):
    og_path = os.path.join(src_dir, name)
    renamed = img_rename + str(index) + '.jpg'
    re_pathed = os.path.join(src_dir, renamed)
    # Basically swaps the old path for the new}
    os.rename(og_path, re_pathed)
