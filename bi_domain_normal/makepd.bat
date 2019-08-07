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
	python -m homcloud.pict.binarize_nd -T picture2d -t 128 -s -m black-base -I -D -o diagramsbl/!N!.idiagram binary/!N!.tif

	python -m homcloud.vectorize_PD -x "[-29.5:15.5]" -X 45 -y "[-29.5:15.5]" -Y 45 -D 0 -C 1.0 -p 1.0 -d 0 -H histoinfo.json -o vectsbl/!N!.txt diagramsbl/!N!.idiagram

	python -m homcloud.plot_diagram -d 0 -l -x "[-29.5:15.5]" -X 45 diagramsbl/!N!.idiagram -o pdbl/!N!.tif
	
	python -m homcloud.pict.binarize_nd -T picture2d -t 128 -s -m white-base -I -D -o diagramswh/!N!.idiagram binary/!N!.tif

	python -m homcloud.vectorize_PD -x "[-29.5:15.5]" -X 45 -y "[-29.5:15.5]" -Y 45 -D 0 -C 1.0 -p 1.0 -d 0 -H histoinfo.json -o vectswh/!N!.txt diagramswh/!N!.idiagram

	python -m homcloud.plot_diagram -d 0 -l -x "[-29.5:15.5]" -X 45 diagramswh/!N!.idiagram -o pdwh/!N!.tif
)


pause