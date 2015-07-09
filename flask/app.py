# -*-coding:utf-8-*-

# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import jubatus

from lux_classifier import LuxClassifier

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

name = 'test2'

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    title = u"ようこそ"
    return render_template('hello.html',
                           name=name, title=title)
#
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = u"こんにちは"
    if request.method == 'POST':
        mongo_server_ip     = request.form['mongo_server_ip']
        mongo_server_port   = request.form['mongo_server_port']
        jubatus_server_ip   = request.form['jubatus_server_ip']
        jubatus_server_port = request.form['jubatus_server_port']
        db_name             = request.form['jubatus_server_port']
        collection_name     = request.form['jubatus_server_port']

        # POSTで得られる値はstr型なのでintに変換する
        jubatus_server_port = int(jubatus_server_port)
        mongo_server_port   = int(mongo_server_port)

        client = jubatus.Classifier(jubatus_server_ip, jubatus_server_port, name)
        lux_classifier = LuxClassifier()
        result_list = lux_classifier.predict(client)

        return render_template('hello.html',
                               jubatus_server_ip   = jubatus_server_ip,
                               jubatus_server_port = jubatus_server_port,
                               mongo_server_ip     = mongo_server_ip,
                               mongo_server_port   = mongo_server_port,
                               result_list         = result_list)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('hello'))

def jubatusPredict():
    return render_template('hello.html',
                           name  = name, 
                           title = title)

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に
