#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import csv

class ReadCSV():
    def outPutData(self):
        df = pd.read_csv('csv/data.csv')
        name_list   = self.outPutNameList()
        value_list  = [0]*len(name_list)
        number_list =  df['Unnamed: 0']
        value_list  =  df[name_list[4]]
        listx = [0] * len(value_list)
        i = 0

        for data in value_list:
            listx[i] = data
            i += 1
        return listx

    def outPutNameList(self):
        f = open('csv/data.csv', "r")
        reader = csv.reader(f)
        for row in reader:
            name_list =  row
            break
        return name_list

if __name__ == '__main__':
    hoge = ReadCSV()
    # hoge.outPutData()
    print hoge.outPutData()
