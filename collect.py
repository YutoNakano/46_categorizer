# 画像データ集めに便利なライブラリ
from icrawler.builtin import BingImageCrawler
# システムパラメーターを取得、操作する標準ライブラリ
import sys
# ファイル、プロセスなどOS依存の情報を取得、操作するライブラリ
import os
# sys.argvは、pythonのスクリプトを起動したときに与えられた、コマンドライン引数を文字列のリストとして格納した変数。
argv = sys.argv
# path.isdirはディレクトリかどうか調べるやつ
if not os.path.isdir(argv[1]):
    # ディレクトリを再帰的に作成する
    os.makedirs(argv[1])
