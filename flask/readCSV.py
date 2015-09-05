#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import csv

class ReadCSV():
    def outPutNameList(self) :
        f = open('csv/data.csv', "r")
        reader = csv.reader(f)
        for row in reader:
            name_list =  row
            break
        return name_list

    def outPutDataFrame(self):
        df = pd.read_csv('csv/data.csv')
        name_list   = self.outPutNameList()
        number_list =  df['Unnamed: 0']
        var   = [0]*len(name_list)
        i = 0
        for name in name_list :
            if name != "" :
                var[i] = df[name]
                i += 1
        return var

    def outPutData(self, dataframe):
        listx = [0] * len(dataframe)
        i = 0
        for value in dataframe :
            listx[i] = value
            i += 1
        return listx

if __name__ == '__main__':
    hoge = ReadCSV()
    # hoge.outPutData()
    dataframe = hoge.outPutDataFrame()
    hoge.outPutData(dataframe[1])
