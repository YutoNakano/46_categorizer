import os
import glob
from PIL import Image

wsize = input('Image Size: ')
if wsize == '':
    wsize = 700  # デフォルトは幅700px
else:
    wsize = int(wsize)
# 指定フォルダのjpgファイル一覧を取得
files = glob.glob('images/out_kanjikeyaki/*.jpg')

# ファイル一覧をループ
for f in files:
    img = Image.open(f)
    # 指定幅以下の画像はスキップ
    if wsize >= img.width:
        continue
    # 指定幅からリサイズレートを算出
    rate = wsize / img.width
    # リサイズレートから高さを算出
    hsize = int(img.height * rate)
    # リサイズ実行
    img_resize = img.resize((wsize, hsize))
    # 新しいファイル名を作成
    imgdir = os.path.dirname(f)
    imgname = os.path.basename(f)
    newfname = imgdir + "/resize_" + imgname
    print(newfname)
    # リサイズ画像を指定ファイル名で保存
    img_resize.save(newfname)
