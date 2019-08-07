import os
os.getcwd()
os.chdir("")

import numpy as np

#cos類似度の定義
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

#総当たりでcos類似度を算出 
result = []
for i in range(1,10):
    for k in range(i+1,11):
        file1 = "00{:02d}.txt".format(i)
        file2 = "00{:02d}.txt".format(k)
        
        a1 = np.loadtxt(file1)
        a2 = np.loadtxt(file2)
        
        sim = cos_sim(a1,a2)
        result.append(sim)

#平均        
ave = np.mean(result)
#偏差
std = np.std(result)
print(result)
print( )
print("平均:" + str(ave))
print("偏差:" + str(std))