#!/bin/env python3
""" formats file containing latex tables to vocabulary for my hinid spelling trainer"""
import sys
import pickle

vocabulary = {}
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if "label" in line:
            new_key = line.strip().replace("label{tab:","").replace("}","")
            vocabulary[new_key] = []
        else:
            vocabulary[new_key].append([x.strip() for x in line.rstrip().split("&")[0:2]])

with open('vocabulary.pkl', 'wb') as f:
    pickle.dump(vocabulary, f, protocol=pickle.HIGHEST_PROTOCOL)
