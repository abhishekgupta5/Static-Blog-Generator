#!/usr/bin/env python3

#Getting metadata
def get_metadata(source_file):
    fobj_read = open(source_file)
    data = fobj_read.readlines()
    i = 1
    dic = {}
    while i<=7:
        key = data[i].split('.. ')[1].split(': ')[0]
        value = data[i].split('.. ')[1].split(': ')[1].split('\n')[0]
        dic[key] = value
        i+=1
    return dic
