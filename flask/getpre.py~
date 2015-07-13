#usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import json

class preMongo:
    con = MongoClient('127.0.0.1', 27017)
    db  = con['sensordb']
    # col = db.sensors_predict
    col = db.predict_sensors
    global dic
    dic = {}
    count = 0

    for data in col.find():
        del data['_id']
        json_list = json.dumps(data)
        dic[count] = json.loads(json_list)
        count += 1

    def getDic(self):
        return dic

    # count = 0
    # for count in dic:
    #     print dic[count]
