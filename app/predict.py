import os
import sys
import numpy as np
import chromedriver_binary
from selenium import webdriver
from keras.utils import np_utils
from keras.applications.vgg16 import VGG16
from sklearn.model_selection import train_test_split
from keras.layers import Input, Activation, Dense, Flatten, Dropout
from selenium.webdriver.chrome.options import Options
from tensorflow.keras.optimizers import Adam
from keras.models import model_from_json
from keras.models import Sequential
from keras.models import load_model
from keras.models import Model
import glob as glob
import pickle
import time
import cv2
from natsort import natsorted

print('開始しますよ(´・ω・)')
model = load_model('../data/model/cnn.h5')
classes = pickle.load(open('classes.sav', 'rb'))
res = open('result.txt', 'w')

        #画像の前処理
files = glob.glob('../data/converted/image/*.png')
files = natsorted(files)
box = []
for file in files:
    print(file)
    img = cv2.imread(file)
    img = cv2.resize(img,dsize=(224,224))
    img = img.astype('float32')
    img /= 255.0
    img = img[None, ...]
    result = model.predict(img)

    #確率が一番大きいクラス
    pred = result.argmax()
    print(pred)
    res.write(str(pred)+'\n')
print('(´・ω・)(´・ω・)(´・ω・)(´・ω・)\n終わりますよ(´・ω・)')
