# -*-coding:utf-8-*-

# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import jubatus

from lux_classifier import LuxClassifier

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

host = '127.0.0.1' 
port = 9199
name = 'test2'

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    client = jubatus.Classifier(host, port, name)
    lux_classifier = LuxClassifier()

    title = u"ようこそ"
    results = lux_classifier.predict(client)
    result = results
    # index.html をレンダリングする
    return render_template('hello.html',
                           result=result, title=title)
#
# # /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = u"こんにちは"
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        name = request.form['name']
        # index.html をレンダリングする
        host = name
        return render_template('hello.html',
                               result=result, title=title)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
