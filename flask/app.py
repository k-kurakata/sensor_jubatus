# -*-coding:utf-8-*-

# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import jubatus

from lux_classifier import LuxClassifier

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

jubatus_server_ip = '127.0.0.1' 
jubatus_server_port = 9199 
name = 'test2'

hoge = ''

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    # client = jubatus.Classifier(jubatus_server_ip, jubatus_server_port, name)
    # lux_classifier = LuxClassifier()
    #
    title = u"ようこそ"
    # results = lux_classifier.predict(client)
    # result = results
    return render_template('hello.html',
                           name=name, title=title)
#
# # /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = u"こんにちは"
    if request.method == 'POST':
        mongo_server_ip     = request.form['mongo_server_ip']
        mongo_server_port   = request.form['mongo_server_port']
        jubatus_server_ip   = request.form['jubatus_server_ip']
        jubatus_server_port = request.form['jubatus_server_port']

        return render_template('hello.html',
                               jubatus_server_ip   = jubatus_server_ip,
                               jubatus_server_port = jubatus_server_port,
                               mongo_server_ip     = mongo_server_ip,
                               mongo_server_port   = mongo_server_port,
                               )
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('hello'))

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
