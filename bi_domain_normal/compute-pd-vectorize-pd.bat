@echo off

@setlocal enabledelayedexpansion

cd %~dp0

set padding=4

mkdir diagrams vects



for /l %%i in (1, 1, 10) do (
    
	set NUM=%%i

	set N=0000!NUM!

	set N=!N:~-4!

	echo !N!
	python -m homcloud.pict.binarize_nd -T picture2d -t 128 -s -m black-base -I -D -o diagrams/!N!.idiagram binary/!N!.tif

	python -m homcloud.vectorize_PD -x "[-29.5:15.5]" -X 45 -y "[-29.5:15.5]" -Y 45 -D 0 -C 1.0 -p 1.0 -d 0 -H histoinfo.json -o vects/!N!.txt diagrams/!N!.idiagram

	python -m homcloud.plot_diagram -d 0 -l -x "[-29.5:15.5]" -X 45 diagrams/!N!.idiagram -o pd/!N!.tif
)


pause