#!/usr/bin/env python
# coding=utf-8

import csv

class NewDataStructure(object):
    def __init__(self, filename):
        self.filename = filename
        
    def get_distinctid(self):
        key = []
        f = open(self.filename)
        for row in csv.reader(f):
            if row[0] not in key:
                key.append(row[0])
        f.close()
        return key

    def make_new_structure(self):
        pure_id = self.get_distinctid()
        data_empty_value = {}
        for key in pure_id:
            data_empty_value[key] = []
        return data_empty_value

    def make_new_data(self):
        new_data = self.make_new_structure()
        f = open(self.filename)
        for row in csv.reader(f):
            value_row = [cell for cell in row[1:]]
            new_data[row[0]].append(value_row)
        f.close()
        return new_data

    def find_way(self, processid):
        object_data = self.make_new_data()
        values = object_data[processid]
        for v in values:
            if v[2]=='5':
                print v[0]
                self.find_way("00"+v[0])
            else:
                #return v[1]
                print v[1]


if __name__ == "__main__":
    new = NewDataStructure("ws.csv")
    new.find_way("00001")
