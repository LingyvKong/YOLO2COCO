# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:00:59 2021

@author: kongly01
作用：将 images_root 文件夹下的所有jpg的路径写入 data_root/images.txt, 
                            纯图片名（不带.jpg后缀）写到 trainval.txt
"""

import os
import glob

data_root = "/ssd2/other/kongly01/testset"
images_root = "/ssd2/other/kongly01/testset/images"

paths = glob.glob(os.path.join(images_root, '*.jpg'))
print(len(paths))

# with open(os.path.join(data_root, "images.txt"),'a') as f:
#     for file in paths:
#         f.write(file + "\n")

with open(os.path.join(data_root, "trainval.txt"),'a') as f:
    for file in paths:
        pure_imgname = os.path.basename(file).split('.')[0]
        f.write(pure_imgname + "\n")



