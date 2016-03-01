#!/usr/bin/env python
# coding: utf-8

# host = '192.168.33.10'
host = '127.0.0.1'
port = 9199
name = 'test2'

import sys
import json
import random
import jubatus
from jubatus.common import Datum
# from getmongo import convertMongo 
from getpre import preMongo

# getmongo = convertMongo()

class LuxClassifier():

    def predict(self, client):
        getpre  = preMongo()
        dic_pre = getpre.getDic()
        data = []
        predict_result = {}

        for line in dic_pre:
            value = dic_pre[line]['Value']
            data.append(Datum({'Value':value}))

        for d in data:
            res = client.classify([d])
            getmongo.postDB(max(res[0], key=lambda x: x.score).label, str(d.num_values[0][1]))

            sys.stdout.write(max(res[0], key=lambda x: x.score).label)
            sys.stdout.write(' ')
            sys.stdout.write(str(d.num_values[0][1]))
            sys.stdout.write('\n')

            hoge = str(d.num_values[0][1])
            result = max(res[0], key=lambda x: x.score).label   
            predict_result.update({'Result': result, 
                'Value'  : hoge})

            return predict_result['Result']

if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.Classifier(host, port, name)
    lux_classifier = LuxClassifier()
    print lux_classifier.predict(client)
