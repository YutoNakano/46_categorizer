import numpy as np
from PIL import Image
import os, glob, random

#変数の初期化
photo_size = 75   #画像サイズ
X = []#画像データを格納するリスト
y = []#ラベルデータを格納するリスト


def glob_images2(path, label, max_photo, rotate):
    files = glob.glob(path + "/*.jpg")#ファイルの一覧を得る
    random.shuffle(files)
    used_file={}
    #各ファイルを処理
    i = 0
    for f in files:
        if i >= max_photo: break
        if f in used_file: continue# 同じファイルを使わない
        used_file[f] = True
        i += 1
        #画像ファイルを読む
        img = Image.open(f)
        img = img.convert('RGB')#色空間をRGBに合わせる
        #同一サイズにリサイズ
        img = img.resize((photo_size, photo_size))
        X.append(image_to_data(img))
        y.append(label)
        if not rotate: continue
        

def image_to_data(img):#画像データを正規化
    data = np.asarray(img)
    data = data / 256
    data = data.reshape(photo_size, photo_size, 3)
    return data

#最大枚数max_photoのデータセットを作る
def make_dataset2(max_photo, outfile, rotate):
    global X
    global y
    X = []
    y = []
    #各画像のフォルダーを読む
    glob_images2("./gana", 0, max_photo, rotate)
    glob_images2("./keya", 1, max_photo, rotate)
    glob_images2("./nogi", 2, max_photo, rotate)
    X = np.array(X, dtype=np.float32)
    np.savez(outfile, X=X, y=y)
    print("saved:" + outfile)

#データセットを作成する
make_dataset2(300, "photo-train.npz", rotate=True)
make_dataset2(100, "photo-test.npz", rotate=False)