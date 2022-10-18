#/bin/zsh

echo '色々と準備をします。時間がかかるのでその間に羊羹でもどうぞ。'
set -x

mkdir ./data/image
mkdir ./data/model
mkdir ./data/datasets
mkdir ./data/image/converted
mkdir ./MAPServer
touch ./data/binarization.sh
echo '#!/bin/zsh\nfind image | while read png;do\n\tconvert -threshold 90% ${png} converted/${png}\ndone' > ./data/binarization.sh

##############################//
#target installation for app#//
############################//
set -e
# 「pip3」の部分はPythonとpipの紐付けに応じて書き換えてください。
# chromedriver-binaryのバージョンはChromeのバージョンに応じて一番近いやつを入れてください。
#
pip3 install selenium==3.141.0
pip3 install chromedriver-binary==104.0.5112.79.0
pip3 install --upgrade pip
pip3 install opencv-python
pip3 install scikit-learn
pip3 install tensorflow
pip3 install natsort

##############################//
#compile java app#//
############################//
src_path[1]="./app/kon/lib/coord"
src_path+="./app/kon/lib/col"
src_path+="./app/kon/lib/debug"
#
javac ./app/MakeDataset.java
for dir in $src_path;do
    for f in $(find $dir -type f | grep .java);do
        javac $f
    done
done

##############################//
#dirctories for datasets	#//
############################//
#1. road_shape
road_shape_path[1]="./data/datasets/road_shape"
road_shape_path+="./data/datasets/road_shape/0"
road_shape_path+="./data/datasets/road_shape/1"
road_shape_path+="./data/datasets/road_shape/7"
road_shape_path+="./data/datasets/road_shape/11"
road_shape_path+="./data/datasets/road_shape/12"
road_shape_path+="./data/datasets/road_shape/13"
road_shape_path+="./data/datasets/road_shape/14"
road_shape_path+="./data/datasets/road_shape/21"
for dir in $road_shape_path;do
	mkdir $dir
done
#2
#road_linear
road_linear_path[1]="./data/datasets/road_shape"
road_linear_path+=road_linear_path[1]+"0"
road_linear_path+=road_linear_path[1]+"1"
road_linear_path+=road_linear_path[1]+"2"
road_linear_path+=road_linear_path[1]+"3"
road_linear_path+=road_linear_path[1]+"4"
road_linear_path+=road_linear_path[1]+"5"
road_linear_path+=road_linear_path[1]+"6"
road_linear_path+=road_linear_path[1]+"7"
road_linear_path+=road_linear_path[1]+"8"
road_linear_path+=road_linear_path[1]+"9"
for dir in $road_linear_path;do
	mkdir $dir
done

set +x
echo 'done(´・ω・)!!'
