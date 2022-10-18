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

print('開始しますよ(´・ω・)')
model = load_model('../data/model/cnn.h5')
classes = pickle.load(open('classes.sav', 'rb'))
index=0

with open('../data/jinshin_zahyou.csv') as f_in:
    for line in f_in:
        coord = line.split(',')
        # File Name
        FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/image2/"+str(index)+".png")

        #オプションの設定
        options = Options()
        options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        options.add_argument('--headless')

        # set driver and url
        driver = webdriver.Chrome(options=options)
        url = 'http://localhost:8090/map?x='+coord[0]+'&y='+coord[1]

        # set window size
        driver.set_window_size(900,900)
        driver.get(url)
        time.sleep(1)

        # Get Screen Shot
        png = driver.find_element_by_id('map').screenshot_as_png
        with open('../data/image2/'+str(index)+'.png', 'wb') as f:
                f.write(png)
        driver.quit()

        #画像の前処理
        files = glob.glob('../data/tmp.png')
        box = []
        for file in files:
            img = cv2.imread(file)
            img = cv2.resize(img,dsize=(224,224))
            img = img.astype('float32')
            img /= 255.0
            img = img[None, ...]
            result = model.predict(img)

        #確率が一番大きいクラス
        pred = result.argmax()
        print(pred)
        index+=1
print('(´・ω・)(´・ω・)(´・ω・)(´・ω・)\n終わりますよ(´・ω・)')
