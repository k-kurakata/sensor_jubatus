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
from getmongo import preMongo

getmongo = preMongo()

class LuxClassifier():

    def train(self, client):
        train_sensors_dic = getmongo.getDic()
        train_sensor_data = []
        value = 0
    
        for line in train_sensors_dic:
            value  = train_sensors_dic[line]['Value']
            result = train_sensors_dic[line]['Result']
            train_sensor_data.append((result, Datum({'Value': value})))
    
        # training data must be shuffled on online learning!
        random.shuffle(train_sensor_data)
    
        # run train
        client.train(train_sensor_data)
        print 'Train Complete!'

if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.Classifier(host, port, name)
    lux_classifier = LuxClassifier()
    lux_classifier.train(client)
