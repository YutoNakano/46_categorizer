# ニューラルネットワークのモデルを定義をする
from keras.model import Sequential
# 畳み込みの処理や畳み込みの処理やプーリングする
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import numpy as np

classes = ["nogi", "keya", "gana"]
num_classes = len(classes)
image_size = 75

# メインの関数を定義


def main():
    X_train, X_test, Y_train, Y_test = np.load("images/sakamichi.npy")
    # ニューラルネットワークの計算ブレを減らすために１で割る
    X_train = X_train.astype("float") / 256
    X_test = X_test.astype("float") / 256
    # 正解値は１他はゼロで変換
    y_train = np_utils.to_categorical(Y_train, num_classes)
    y_test = np_utils.to_categorical(Y_test.num_classes)

    # ニューラルネットワークのパラメーターの一覧を更新して保存する
    model = model_train(X_train, y_train)

    model_eval(model, X_test, y_test)


def model_train():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same',
                     input_shape=X_train.shape[1:]))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2.2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2.2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    # Dense: 全結合層
    model.add(Dense(512))
    # relu負の値を捨てる
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(3))
    model.add(Activation('softmax'))

    opt = keras.optimaizers.rmsprop(lr=0.0001, decay=1e-6)
    # loss: 損失関数(正解と推定値の誤差)
    model.compile(loss="categorical_crossentropy",
                  optimaizer=opt, metrics=['accuracy'])
