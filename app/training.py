import os
import cv2
import numpy as np
import glob as glob
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from keras.applications.vgg16 import VGG16
from keras.models import Sequential
from keras.models import model_from_json
from keras.models import Model
from keras.layers import Input, Activation, concatenate, Dense, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
import pickle

# 適宜パスを変更してください
path = "../data/datasets/road_linear"

X = []
Y = []

folders = os.listdir(path)
classes = [f for f in folders if os.path.isdir(os.path.join(path, f))]
n_classes = len(classes)

#画像を読み込んでリサイズ
for label,class_name in enumerate(classes):
  files = glob.glob(path + "/" +  class_name + "/*.png")
  for file in files:
    img = cv2.imread(file)
    img = cv2.resize(img,dsize=(224,224))
    X.append(img)
    Y.append(label)

#正規化
X = np.array(X)
X = X.astype('float32')
X /= 255.0

#ラベル
Y = np.array(Y)
Y = np_utils.to_categorical(Y,n_classes)
Y[:5]

#学習用とテスト用に分割
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
print(X_train.shape)#学習データ(8割)
print(X_test.shape)#テストデータ(2割)
print(Y_train.shape)#学習データ(8割)
print(Y_test.shape)#テストデータ(2割)


#vgg16
input_tensor = Input(shape=(224,224,3))
#最後の1000の層を省く
base_model = VGG16(weights='imagenet', input_tensor=input_tensor,include_top=False)


#後付けで入れたい層の作成
top_model = Sequential()
top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
top_model.add(Dense(n_classes, activation='softmax'))

model = Model(inputs=base_model.input, outputs=top_model(base_model.output))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

#学習と評価
model.fit(X_train, Y_train, epochs=20, batch_size=16)
score = model.evaluate(X_test, Y_test, batch_size=16)

#クラス名の保存
pickle.dump(classes, open('classes.sav', 'wb'))
model.save('../data/model/cnn.h5')
