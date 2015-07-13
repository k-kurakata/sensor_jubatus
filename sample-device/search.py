#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
from lux_classifier import LuxClassifier
import jubatus

CK = "a71iiYuMoJrhSSZBQBWF5bDVm"
CS = 'bhKEUnaccqA75t9JWjHJ6A7E76RlU4ce1N23p8Y61muh8NvF2k' 
AT = '2587234754-SBW9JesNhQEOPlsrqwSpt3YlhwYCliMDfyAbvPU' 
AS = 'ntqzPEeLlvXsG14KCEkdxeGLSKRKIVrQT3dg3E9rA7njj'      

client = jubatus.Classifier('127.0.0.1', 9199, 'tweet')
lux_classifier = LuxClassifier()

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
while True :
    result_dictionary = lux_classifier.predict(client)
    print result_dictionary['Value']
    previous_params = ""
    if previous_result != result :
        if result == "True":
            params = {"status": u"いるよ"}
        else :
            params = {"status": u"いないよ"}
        previous_result = result 


# OAuth認証で POST method で投稿
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.post(url, params = params)

# レスポンスを確認
    if req.status_code == 200:
        print ("OK")
    else:
        print ("Error: %d" % req.status_code)
