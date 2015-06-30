#!/usr/bin/env python
# coding=utf-8

import csv

def read_data(filename):
    csv_reader = csv.reader(open(filename))
    for row in csv_reader:
        print row


if __name__ == "__main__":
    read_data("w.csv")

