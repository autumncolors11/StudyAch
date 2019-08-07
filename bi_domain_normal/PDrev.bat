@echo off

@setlocal enabledelayedexpansion

cd %~dp0


python -m homcloud.view_vectorized_PD -o dif350_RT.png -l -t Temp350_RTdif meandifvector/mean350_RTwh.txt biRT/histoinfo.json
	

pause