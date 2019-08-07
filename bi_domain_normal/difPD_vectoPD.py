import numpy as np
import cupy as cp

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#2つの平均ベクトル読み込み → 差分を取る → 正or負の部分のみ取り出して正の値にする → 0以上は1に変換 → PDに変換 → 逆解析

#白黒のうちの対象
color = "wh"

#対象とする温度 twoとoneどちらが基準かはすぐ下を参照
twos =["50", "100", "150", "200", "250", "300", "350","350"]
ones =["RT", "50", "100", "150", "200", "250", "300","RT"]

#指定した温度の組でループ
for one, two in zip(ones, twos):

    ### 減算PDの作成
    #注目するPD (減算されるPD)
    att_vec0 = np.loadtxt("bi"+ one +"/"+ color + one +".txt")

    #減算するPD
    obj_vec0 = np.loadtxt("bi"+ two +"/"+ color + two +".txt")

    #PDの二値化
    att_vec = np.array([1 if i > 0 else i for i in att_vec0])
    obj_vec = np.array([1 if i > 0 else i for i in obj_vec0])

    #二値化PDの減算
    dif_vec0 = att_vec - obj_vec

    #減算したPDの正部分のみの取り出し
    dif_vec = [0 if i< 0 else i for i in dif_vec0]

    np.savetxt("meandifvector/mean" + one + "_" + two + color + ".txt", dif_vec)




    txttitle = "meandifvector/mean" + one + "_" + two + color +".txt"

    pd = np.loadtxt(txttitle)

    ### ベクトルをPD配列に再構築
    #最初の1行目
    mat0 = pd[1:2]
    mat = np.pad(mat0,[0,44],"constant")

    #2行目以降を対角線沿いに三角形になるように堆積
    for i in range(2,46):

        lis = pd[int(1+i*(i-1)/2): int(((i*(i+1))/2)+1)]

        lis0 = np.pad(lis,[0,45-i],"constant")
        
        if len(lis0)!= 45:
            lis0 = np.pad(lis0, [0,1],"constant")

        mat = np.vstack((mat,lis0))

    #指定した範囲のプロットを消去する
    # mat[0]:ヒートマップの左が0の行を示す
    for j in range(0,30):
        for k in range(0,45):
            if mat[j][k] != 0:
                mat[j][k] = 0
    
    
    

    #反転
    #fig = np.flip(mat, axis=0)

    fig = mat

    
    plt.figure()
    sns.heatmap(fig, cmap="Reds", linewidths=0.01,linecolor="k")
    plt.savefig("heatmap1/heatmap"+one+"_"+two+".png")
    plt.close('all')
    
    

    binary = np.where(fig == 1)

    


    """
    add = address
    birth=2n-1 death=2n
    offset_death,offset_birth：ベクトル座標からPDの座標にずらすための補正
    binary[0]:death
    binary[1]:birth
    """

    add = []

    #実際のPDの座標とのズレの補正
    offset_birth = -28
    offset_death = -29

    """
    for i in range(0,len(binary[0])):
        add0 = offset_birth + binary[0][i]
        add1 = offset_death + binary[1][i]

        add.append(add1)
        add.append(add0)
    add = list(map(int,add))
    print(add)

    np.savetxt("address_" + txttitle,add, fmt="%.0d")
    """

    addb = []
    for i in range(0,len(binary[1])):
        add0 = offset_birth + binary[1][i]

        addb.append(add0)
    add = list(map(int,addb))
    np.savetxt("BDaddress/address_birth_mean" + one + "_" + two + color +".txt", addb, fmt="%.0d")

    addd = []
    for i in range(0,len(binary[0])):
        add0 = offset_death + binary[0][i]

        addd.append(add0)
    addd = list(map(int,addd))
    np.savetxt("BDaddress/address_death_mean" + one + "_" + two + color +".txt", addd, fmt="%.0d")