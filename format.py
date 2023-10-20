#!/bin/env python3
import os
import pickle
vocabulary = {}
for file in os.listdir():
    vocabulary[file] = []
    with open(file) as f:
        for line in f.readlines():
            vocabulary[file].append(line.split()[0:2])

with open('vocabulary.pkl', 'wb') as f:
    pickle.dump(vocabulary, f, protocol=pickle.HIGHEST_PROTOCOL)

print(vocabulary)
