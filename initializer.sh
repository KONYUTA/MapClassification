#/bin/zsh
set -e
set -x

mkdir ./data/image
mkdir ./data/model
mkdir ./MAPServer

##############################//
#target installation		#//
############################//
pip install selenium==3.141.0
pip install chromedriver-binary==104.0.5112.79.0

##############################//
#dirctories for datasets	#//
############################//
mkdir data/datasets
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
	mkdir dir
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
	mkdir dir
done

set +x
echo 'done(´・ω・)!!'
