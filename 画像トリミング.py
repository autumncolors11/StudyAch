file_path = ""

import os
os.getcwd()
os.chdir(file_path)

import cv2
import numpy as np


file_list = os.listdir(file_path)
    
for file_name in file_list:
    title, ext = os.path.splitext(file_name)
    if ext ==  ".png":
        abs_name = file_path +'\\' + file_name
        img = cv2.imread(abs_name)


    #新しい配列に入力画像の一部を代入
    #[]内はY軸，X軸の順であることに注意
        size = img[35:570,50:700]

    #書き出し
        title = "50-" + file_name
        cv2.imwrite(title ,size)
        
"""
cut not-bar [50:570,50:600]
cut bar [50:570,50:690]
[y,x] ←これ
"""