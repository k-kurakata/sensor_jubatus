#!/usr/bin/env python
# coding: utf-8

import csv

f = open('data.csv', 'rb')

dataReader = csv.reader(f)
dic = {}
i = 0

for row in dataReader:
    dic[i] =  row[1]
    i += 1
