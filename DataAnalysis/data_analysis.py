#!/usr/bin/python3

import pandas as pd
names = ['id','title','year','rating','votes','length','genres']
data = pd.read_csv('imdb_top_10000.txt', sep="\t", names=names, index_col=0)
#this line will prnt out all the data
data
#this function should print out the first column from the data that we have 
data.head()

""" this will show the first 3 colmn """
data.head(3)

# this line will print out the last 5 comlumns from our data

data.tail()

# go throuth the data and tel you for each comlumn how many values you have there and what type each column is 
data.info()

# go throuth the data and gives a lot of usefull discription to the data 
data.describe()

""" we can also export data to another file using the pandas library """

data.to_csv("test.csv", header=True , index=True, sep=',')


"""we can sort data as show the next line of code """
""" this line will print data sorted from the biggest value to the lowest , however if u dnt set the ascending to Flase it will generate it automatcally from the lowest to the highest"""
data1 = data.sort_values(by='rating', ascending = False)
# now exprot this sorted data to another file
data1.to_csv("SortedTest.csv", header=True, index= True, sep=',')
