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

    # df編集時に使う関数
    def dfToCsv(self, del_start, del_end):
        df = pd.read_csv('csv/data.csv')
        del_start = int(del_start)
        del_end   = int(del_end)
        # edit_df   = df.ix[del_start : del_end]
        edit_df_start = df.ix[0:del_start]
        edit_df_end   = df.ix[del_end:200]
        edit_df = pd.concat([edit_df_start, edit_df_end])
        edit_describe  = edit_df.describe()
        edit_df.to_csv('csv/edit_data.csv')
        edit_describe.to_csv('csv/edit_describe.csv')

if __name__ == '__main__':
    hoge = ReadCSV()
    dataframe = hoge.outPutDataFrame()
    # print hoge.outPutData(dataframe[1])
    hoge.dfToCsv(10, 100)
    # print dataframe
