file_path = ""

import os
os.getcwd()
os.chdir(file_path)

import cv2
import numpy as np

#フォルダパス指定
data_dir_path = file_path
file_list = os.listdir(file_path)
    
#フォルダ内各ファイルを二値化    
for file_name in file_list:
    title, ext = os.path.splitext(file_name)
    if ext == '.tif':
        abs_name = data_dir_path +'\\' + file_name
        gray = cv2.imread(abs_name,0)

        th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 1)
        
            # カーネルの定義
        kernel = np.ones((3,3), np.uint8)

    # 膨張・収縮処理(方法2)
        dilate = cv2.dilate(th2, kernel)
        erode = cv2.erode(dilate, kernel)

        cv2.imwrite(file_path + "\\gauss\\" + file_name,erode)    

#研究では81 1