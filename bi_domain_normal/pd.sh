#!/bin/bash

#list1="50 RT bl"
list1="RT 50 wh"

#list3="100 50 bl"
list2="50 100 wh"

#list5="150 100 bl"
list3="100 150 wh"

#list7="200 150 bl"
list4="150 200 wh"

#list9="250 200 bl"
list5="200 250 wh"

#list11="300 250 bl"
list6="250 300 wh"

#list13="350 300 bl"
list7="300 350 wh"

list8="RT 350 wh"
#list16="350 RT bl"


#list
#list19="200 150 wh"
#list5="RT 50 bl"
#list10="50 100 bl"
#list14="100 150 bl"
#list18="150 200 bl"
#list22="200 250 bl"
#list26="250 300 bl"
#list4="350 300 wh"
#list8="50 RT wh"
#list23="250 200 wh"
#list27="300 250 wh"
# "${list17[*]}" "${list18[*]}" "${list19[*]}" "${list20[*]}" "${list21[*]}" "${list22[*]}" "${list23[*]}" "${list24[*]}" "${list25[*]}" "${list26[*]}" "${list27[*]}" "${list28[*]}"


for U in D B; do

	for lisnum in  "${list1[*]}" "${list2[*]}" "${list3[*]}" "${list4[*]}" "${list5[*]}" "${list6[*]}" "${list7[*]}" "${list8[*]}" ; do
		echo $lisnum
		
		XYA=$(echo $lisnum | cut -d " " -f 1)
		XYB=$(echo $lisnum | cut -d " " -f 2)
		XYC=$(echo $lisnum | cut -d " " -f 3)
		
		
		P=$XYA
		Q=$XYB
		R=$XYC
	

		echo $P
		echo $Q
		echo $R

		cd rev_domain_$U
		mkdir bi$P$Q$R
		cd -

		Num=$(wc -l < BDaddress/address_birth_mean${P}_${Q}${R}.txt)
		N=$Num


		for numline in 1 ; do
			BirthB=$( sed -n ${numline}p BDaddress/address_birth_mean${P}_${Q}${R}.txt )
			DeathD=$( sed -n ${numline}p BDaddress/address_death_mean${P}_${Q}${R}.txt )
			echo $numline
			echo $BirthB
			echo $DeathD
		

			for i in `seq -f %04g 1 10`; do

				python -m homcloud.view_index_pict -d 0 -$U -S 8 -f "birth == ${BirthB}" -f "death == ${DeathD}" --no-label bi$P/binary/${i}.tif bi$P/diagrams$R/${i}.idiagram -o rev_domain_${U}/bi${P}${Q}${R}/${P}_${Q}${R}_${i}.tif	
				
			done
			echo $U $N $numline $i
			
			
		done



		for numline in `seq 2 $N` ; do
			
			BirthB=$( sed -n ${numline}p BDaddress/address_birth_mean${P}_${Q}${R}.txt )
			DeathD=$( sed -n ${numline}p BDaddress/address_death_mean${P}_${Q}${R}.txt )

			for i in `seq -f %04g 1 10`; do
				
				python -m homcloud.view_index_pict -d 0 -${U} -S 8 -f "birth == ${BirthB}" -f "death == ${DeathD}" --no-label rev_domain_${U}/bi${P}${Q}${R}/${P}_${Q}${R}_${i}.tif bi${P}/diagrams${R}/${i}.idiagram -o rev_domain_${U}/bi${P}${Q}${R}/${P}_${Q}${R}_${i}.tif	

			done
			
			echo $U $N $numline $i
			
		done
	done

done


read -p "Hit enter: "