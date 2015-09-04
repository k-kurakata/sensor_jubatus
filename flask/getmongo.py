# usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient
import json
import csv

class convertMongo:

    def getTrainSensorsDic(self, mongo_ip, mongo_port, db_name, collection_name):
        convert_mongo      = convertMongo()
        mongo_client       = MongoClient(mongo_ip, mongo_port)
        sensor_db          = mongo_client[db_name]
        sensors_collection = sensor_db[collection_name]
        global pre
        global train_sensors_dic
        pre = sensor_db.predict
        train_sensors_dic = {}
        db_information    = {}
        csv_list          = []
        i = 0
        for data in sensors_collection.find():
            del data['_id']
            json_list = json.dumps(data)
            train_sensors_dic[i] = json.loads(json_list)
            csv_list.append(train_sensors_dic[i])   # データフレーム用に作成
            i += 1
        # CSVに落としこむ
        df = pd.DataFrame(csv_list)
        describe = df.describe()
        df.to_csv('csv/data.csv')
        describe.to_csv('csv/describe.csv')
        # print df[["Name", "Value"]]
        # print df.describe()
        return train_sensors_dic
    
    def postDB(self, result, value):
        pre.insert({'result':result, 'value':value})

    def getTable(self, dic):
        df = pd.DataFrame(dic)
        return df

if __name__ == '__main__':
    convert_mongo = convertMongo()
    convert_mongo.getTrainSensorsDic('127.0.0.1', 27017, 'sensordb', 'sensors')
