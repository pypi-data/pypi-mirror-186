#!/bin/bash
str=`python3 -V`
apt-get update -y
echo 'Version: ' $str
oldIFS=$IFS
IFS='.' 
y=($str)
if [[ ${y[1]} = '9' ]];then
	echo '3.9'
	curl 'https://gitcode.net/q924257/mediapipe-title/-/raw/master/mediapipe-0.8-cp39-cp39-linux_aarch64.whl' -O -#
	pip3 install mediapipe-0.8-cp39-cp39-linux_aarch64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
	rm -f mediapipe-0.8-cp39-cp39-linux_aarch64.whl
elif [[ ${y[1]} = '10' ]];then
	echo '3.8'
	curl 'https://gitcode.net/q924257/mediapipe-title/-/raw/master/mediapipe-0.8-cp310-cp310-linux_aarch64.whl' -O -#
	pip3 install mediapipe-0.8-cp310-cp310-linux_aarch64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
	rm -f mediapipe-0.8-cp310-cp310-linux_aarch64.whl
elif [[ ${y[1]} = '8' ]];then
	echo '3.8'
	curl 'https://gitcode.net/q924257/mediapipe-title/-/raw/master/mediapipe-0.8-cp38-cp38-linux_aarch64.whl' -O -#
	pip3 install mediapipe-0.8-cp38-cp38-linux_aarch64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
	rm -f mediapipe-0.8-cp38-cp38-linux_aarch64.whl
elif [[ ${y[1]} = '7' ]];then
	echo '3.7'
	curl 'https://gitcode.net/q924257/mediapipe-title/-/raw/master/mediapipe-0.8-cp37-cp37-linux_aarch64.whl' -O -#
	pip3 install mediapipe-0.8-cp37-cp37-linux_aarch64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
	rm -f mediapipe-0.8-cp37-cp37-linux_aarch64.whl
elif [[ ${y[1]} = '6' ]];then
	echo '3.6'
	curl 'https://gitcode.net/q924257/mediapipe-title/-/raw/master/mediapipe-0.8-cp36-cp36-linux_aarch64.whl' -O -#
	pip3 install mediapipe-0.8-cp36-cp36-linux_aarch64.whl -i https://pypi.tuna.tsinghua.edu.cn/simple
	rm -f mediapipe-0.8-cp36-cp36-linux_aarch64.whl
fi
