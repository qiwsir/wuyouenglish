#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xml.etree.cElementTree as ET
tree = ET.ElementTree(file="4056.xml")
tree
root = tree.getroot()
dataset = (root[0].attrib)
key_dataset = {'number'}
for d in key_dataset:
    print "%s: %s" % (d, dataset.get(d))
referenceFunction = (root[0][0][0][0].attrib)
key_referenceFunction = {'category', 'subCategory', 'name', 'CASNumber', 'unit', 'amount','generalComment'}
for s in key_referenceFunction:
    print "%s: %s" % (s, referenceFunction.get(s))
geography = (root[0][0][0][1].attrib)
key_geography = {'location'}
for t in key_geography:
    print "%s: %s" % (t, geography.get(t))