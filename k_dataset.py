# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 01:07:54 2017

@author: USER
"""

#%% import
from csv import DictReader

#%%
class DataSet():
    def __init__(self, bodies="bodies", stances="stances", path="fake-news"):
        self.path = path

        print("Reading dataset")
        bodies = bodies+".csv"
        stances = stances+".csv"

        self.stances = self.read(stances)
        articles = self.read(bodies)
        self.articles = dict()

        #make the body ID an integer value
        for i,_ in enumerate(self.stances):
            self.stances[i] = dict(self.stances[i])
            self.stances[i]['Body ID'] = int(self.stances[i]['Body ID'])

        #copy all bodies into a dictionary
        for article in articles:
            self.articles[int(article['Body ID'])] = article['articleBody']

        print("Total stances: " + str(len(self.stances)))
        print("Total bodies: " + str(len(self.articles)))



    def read(self,filename):
        rows = []
        with open(self.path + "/" + filename, "r", encoding='utf-8') as table:
            r = DictReader(table)

            for line in r:
                rows.append(line)
        return rows

