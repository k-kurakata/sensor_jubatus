#!/usr/bin/env python
# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import jubatus
from lux_classifier import LuxClassifier

client = jubatus.Classifier('127.0.0.1', 9199, 'test')
previous_result = 'previous'

oath_key_dict = {
        "consumer_key"       : "a71iiYuMoJrhSSZBQBWF5bDVm",
        "consumer_secret"    : "bhKEUnaccqA75t9JWjHJ6A7E76RlU4ce1N23p8Y61muh8NvF2k",
        "access_token"       : "2587234754-SBW9JesNhQEOPlsrqwSpt3YlhwYCliMDfyAbvPU",
        "access_token_secret": "ntqzPEeLlvXsG14KCEkdxeGLSKRKIVrQT3dg3E9rA7njj"
        }

CK = oath_key_dict["consumer_key"]
CS = oath_key_dict["consumer_secret"]
AT = oath_key_dict["access_token"]
AS = oath_key_dict["access_token_secret"]

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
lux_classifier = LuxClassifier()
result         = lux_classifier.predict(client)
print result

if(result != previous_result):
    if (result == 'True'):
        params = {"status": u"人がいるよ"}
    else :
        params = {"status": u"人がいないよ"}
    previous_result = result

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
