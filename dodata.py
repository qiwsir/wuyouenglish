#!/usr/bin/env python
# coding=utf-8

import csv

def read_data(filename, start_id):
    csv_reader = csv.reader(open(filename))
    new_data = {}
    for row in csv_reader:
        if row[3]:        
            value_row = [cell for cell in row[1:]]
            if start_id != row[0]:
                start_id = row[0]

            new_data[start_id] = []
            new_data[start_id].append(value_row)
    return new_data


if __name__ == "__main__":
    print read_data("w.csv", "00001")

