file_path = "C:\"

import os
os.getcwd()
os.chdir(file_path)


"""
ベース：適応的二値化
小領域での二値化判断アルゴリズム：大津法

ADAPTIVE_THRESH_では平均orガウシアンのみ
→対象ピクセルを周囲nピクセル範囲内のみでの大津法で計算し閾値決定
"""



#実行する二値化の詳細

import cv2
import numpy as np

def threshold(src,ksize=3,c=0):
    
    #畳み込み演算をしない領域の幅
    d = int((ksize-1)/2)
    h,w = src.shape[0],src.shape[1]
    
    
    dst = np.empty((h,w))
    dst.fill(255)
    
    n = ksize**2
    
    #yを0からhまで走査，かつyの各値でxを0からwまで走査
    for y in range(0,h):
        for x in range(0,w):
            
            hist = [np.sum(src[y-d:y+d+1,x-d:x+d+1] == i) for i in range(256)]
            
            s_max = (0,-10)

            print("map",x,y)
            
            for th in range(256):              

                n1 = sum(hist[:th])
                n2 = sum(hist[th:])
                
                if n1 == 0 : mu1 = 0
                else : mu1 = sum([i * hist[i] for i in range(0,th)]) / n1
                if n2 == 0 : mu2 = 0
                else : mu2 = sum([i * hist[i] for i in range(th,256)]) / n2
                    
                s = n1 * n2 * (mu1 - mu2) ** 2
                
                if s > s_max[1]:
                    s_max = (th,s)
                    

            t = s_max[0]
            
            if(src[y][x] < t - c).any(): dst[y][x] = 0
            else:dst[y][x] = 255
                
    return dst





#二値化の実行

def main():
    # 入力画像読み込み
    for knum in range(11,103,4):
        for cnum in range(0,3):

            img = cv2.imread("mini-0001.tif")

    # グレースケール変換
            gray = cv2.cvtColor(img,0)

    # 方法1
            dst1 = threshold(gray, ksize=knum,c=cnum)

    # 出力
            cv2.imwrite("binarymulti/adapt_otsu/mini-0001-"+ str(knum) + "-" + str(cnum) +".tif", dst1)

            print("カーネルサイズ",knum,"Cのサイズ",cnum,"適応的二値化大津適応的二値化大津適応的二値化大津")

    
if __name__ == "__main__":
    main()
