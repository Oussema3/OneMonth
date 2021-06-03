#!/usr/bin/python3

import pandas as pd
names = ['id','title','year','rating','votes','length','genres']
data = pd.read_csv('imdb_top_10000.txt', sep="\t", names=names, index_col=0)

