# usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient
import json

class convertMongo:

    # 引数に入れたDB情報をディクショナリにして返す
    def inputInformation(self, mongo_ip, mongo_port, db_name):
        # collection_name    = sensors_collection
        mongo_client       = MongoClient(mongo_ip, mongo_port)
        sensor_db          = mongo_client[db_name]
        sensors_collection = sensor_db.sensors
        db_information = {'mongo_client'      : mongo_client, 
                          'sensor_db'         : sensor_db,
                          'sensors_collection': sensors_collection}
        return db_information

    def getTrainSensorsDic(self, mongo_ip, mongo_port, db_name):
        convert_mongo  = convertMongo()
        # mongo_client       = db_informatino['mongo_client']
        # sensor_db          = db_informatino['sensor_db']
        # sensors_collection = db_informatino['sensors_collection']

        mongo_client       = MongoClient(mongo_ip, mongo_port)
        sensor_db          = mongo_client[db_name]
        sensors_collection = sensor_db.sensors
        global pre
        global train_sensors_dic
        pre = sensor_db.predict
        train_sensors_dic = {}
        db_information    = {}
        i = 0

        for data in sensors_collection.find():
            del data['_id']
            json_list  = json.dumps(data)
            train_sensors_dic[i] = json.loads(json_list)
            i += 1

        return train_sensors_dic
    
    def postDB(self, result, value):
        pre.insert({'result':result, 'value':value})

    def getTable(self, dic):
        df = pd.DataFrame(dic)
        return df
    

if __name__ == '__main__':
    convert_mongo = convertMongo()
    print convert_mongo.getTrainSensorsDic('127.0.0.1', 27017, 'sensordb')
