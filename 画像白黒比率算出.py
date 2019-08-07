file_path = "C"

import os
os.getcwd()
os.chdir(file_path)

import cv2
import numpy as np

file_list = os.listdir(file_path)

result= []
for file_name in file_list:
    title, ext = os.path.splitext(file_name)
    if ext == '.tif':
        abs_name = file_path +'\\' + file_name
        grayimg = cv2.imread(abs_name, 0)

# 読み込み画像


# 全画素数
        sizeall = grayimg.size

# 画像内の白色部分のピクセル数
        sizewhite = cv2.countNonZero(grayimg)
    
# Ps(白色ピクセル数の割合)
        Pss = sizewhite / sizeall

        per = Pss * 100
        print(per,file_name)

        result.append(per)

lis = np.average(result)
print("平均")
print(lis)
print("標準偏差")
print(np.std(result))