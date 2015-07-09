# -*-coding:utf-8-*-

# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import jubatus

from lux_classifier import LuxClassifier

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# メッセージをランダムに表示するメソッド
def picked_up():
    host = '192.168.33.10'
    port = 9199
    name = 'test2'

    client = jubatus.Classifier(host, port, name)
    lux_classifier = LuxClassifier()
    return lux_classifier.predict(client)

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    title = u"ようこそ"
    message = 'hello'
    # index.html をレンダリングする
    return render_template('hello.html',
                           message=message, title=title)
#
# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = u"こんにちは"
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        name = request.form['name']
        # index.html をレンダリングする
        return render_template('hello.html',
                               name=name, title=title)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('hello'))

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
