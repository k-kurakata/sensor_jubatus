# usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient
import json
import csv

class convertMongo:

    def getTrainSensorsDic(self, mongo_ip, mongo_port, db_name, collection_name):
        f = open('data.csv', 'ab')
        dataWriter = csv.writer(f)
        convert_mongo      = convertMongo()

        mongo_client       = MongoClient(mongo_ip, mongo_port)
        sensor_db          = mongo_client[db_name]
        sensors_collection = sensor_db[collection_name]
        global pre
        global train_sensors_dic
        pre = sensor_db.predict
        train_sensors_dic = {}
        db_information    = {}
        i = 0
        for data in sensors_collection.find():
            del data['_id']
            json_list = json.dumps(data)
            train_sensors_dic[i] = json.loads(json_list)
            i += 1
        csv_list = train_sensors_dic.items()
        print csv_list
        dataWriter.writerows(csv_list)
        f.close()
        return train_sensors_dic
    
    def postDB(self, result, value):
        pre.insert({'result':result, 'value':value})

    def getTable(self, dic):
        df = pd.DataFrame(dic)
        return df

if __name__ == '__main__':
    convert_mongo = convertMongo()
    convert_mongo.getTrainSensorsDic('127.0.0.1', 27017, 'sensordb', 'sensors')
