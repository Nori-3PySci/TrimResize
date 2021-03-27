# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import os
from PIL import Image

newname = "XXX-"

default_path = r"directory"

iPhone_fix_size = [0, 100, 0, 0, 1000, 0] #[left, upper, right, lower, width, height] width&height 0 = keep ratio
MBAir_fix_size = [0, 290, 0, 0, 1000, 0]
iPadmini_fix_size = [0, 40, 0, 0, 1000, 0]
other_fix_size = [0, 0, 0, 0, 1000, 0]

iPhone_ss_size = [1125, 2436]
MBAir_ss_size = [3104, 1834]
iPadmini_ss_size = [1536, 2048]

ext_list = [".png", ".PNG"]


# +
def path_set(default_path):
    if default_path == "":
        path_temp = os.getcwd()
    else:
        path_temp = default_path
    return path_temp

def file_select(default_path, newname, ext_list):
    list_temp = []
    for file in os.listdir(default_path):
        if file[-4:] in ext_list:
            if not newname in file:
                list_temp.append(file)
    return list_temp
            
def trimming(im, fix_size):
    width = im.size[0]
    height = im.size[1]
    im_trim = im.crop((fix_size[0], fix_size[1], width - fix_size[2], height - fix_size[3]))
    return im_trim

def resizing(im, fix_size):
    width = im.size[0]
    height = im.size[1]
    resize_width = fix_size[4]
    resize_height = fix_size[5]
    
    resized = im
    
    if resize_width == 0 and resize_height == 0:
        print("ERROR: resize_size should not be [0, 0]")
    elif resize_height == 0:
        if width > resize_width:
            resized = im.resize((resize_width, int(height/(width/resize_width))))
    elif resize_width == 0:
        if height > resize_height:
            resized = im.resize((int(width/(height/resize_height)), resize_height))
    elif resize_size[0] != 0 and resize_size[1] != 0:
        if width > resize_width and height > resize_height:
            resized = im.resize((resize_width, resize_height))
        
    return resized
    


# -

if __name__ == '__main__':
    default_path = path_set(default_path)
    file_list = sorted(file_select(default_path, newname, ext_list))
    
    os.chdir(default_path)
    
    i = 1
    filling = len(str(len(file_list))) + 1
    
    for file in file_list:
        im = Image.open(file)
        if im.size[0] == iPhone_ss_size[0] and im.size[1] == iPhone_ss_size[1]:
            im_trim = trimming(im, iPhone_fix_size)
            im_trim_resize = resizing(im_trim, iPhone_fix_size)
            im_trim_resize.save(newname + str(i).zfill(filling) + ".png")
        elif im.size[0] == MBAir_ss_size[0] and im.size[1] == MBAir_ss_size[1]:
            im_trim = trimming(im, MBAir_fix_size)
            im_trim_resize = resizing(im_trim, MBAir_fix_size)
            im_trim_resize.save(newname + str(i).zfill(filling) + ".png")       
        elif im.size[0] == iPadmini_ss_size[0] and im.size[1] == iPadmini_ss_size[1]:
            im_trim = trimming(im, iPadmini_fix_size)
            im_trim_resize = resizing(im_trim, iPadmini_fix_size)
            im_trim_resize.save(newname + str(i).zfill(filling) + ".png") 
        else:
            im_resize = resizing(im, other_fix_size)
            im_resize.save(newname + str(i).zfill(filling) + ".png") 
        i = i + 1




