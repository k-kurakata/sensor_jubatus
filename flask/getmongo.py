# usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient
import json

class convertMongo:
    mongo_client       = MongoClient('127.0.0.1', 27017)
    sensor_db          = mongo_client['sensordb']
    sensors_collection = sensor_db.sensors
    global pre
    global train_sensors_dic
    pre = sensor_db.predict
    train_sensors_dic = {}
    i = 0

    for data in sensors_collection.find():
        del data['_id']
        json_list  = json.dumps(data)
        train_sensors_dic[i] = json.loads(json_list)
        i += 1

    def getTrainSensorsDic(self):
        return train_sensors_dic
    
    def postDB(self, result, value):
        pre.insert({'result':result, 'value':value})

    def getTable(self, dic):
        df = pd.DataFrame(dic)
        return df

if __name__ == '__main__':
    convert_mongo = convertMongo()
    print convert_mongo.getTrainSensorsDic()
