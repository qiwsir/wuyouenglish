#!/usr/bin/env python
# coding=utf-8

import csv

class NewDataStructure(object):
    def __init__(self, filename):
        self.reader = csv.reader(open(filename))

    def data_key(self, p_id):
        key = {}         
        for row in self.reader:
            if p_id != row[0]:
                p_id = row[0]
            key[p_id] = []
        return key

#def read_data(filename, key):
#    csv_reader = csv.reader(open(filename))
#    new_data = {}
#    for row in csv_reader:
#        value_row = [cell for cell in row[1:]]
#        if key != row[0]:
#            key = row[0]
#
#        new_data[key] = []
#        new_data[key].append(value_row)
#    return new_data


if __name__ == "__main__":
    new = NewDataStructure("w.csv")
    print new.data_key("00001")
