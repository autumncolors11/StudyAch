#!/bin/bash

#list1=(aa bb)
#list2=(cc dd)

#for l in list1 list2
#do
#  x=$l[0]
#  echo ${!x}
#  y=$l[1]
#  echo ${!y}
  
#done

cd C:/Users/euphr/Documents/Study/bi_domain
pwd
list1="300 350 bl"
list2="350 300 bl"


P=300
Q=350
R=bl
U=B
N=25

BirthB=-5
DeathD=-2
numline=1

for numline in 1 ; do
		


	echo $BirthB

	for i in `seq -f %04g 1 10`; do

		python -m homcloud.view_index_pict -d 0 -$U -S 10 -f birth == $birthB -f death == $deathD --no-label -o 300_350bl_${i}.tif ${i}.tif ${i}.idiagram

	done
		
	echo $N $numline $i
		
done


read -p "Hit enter: "