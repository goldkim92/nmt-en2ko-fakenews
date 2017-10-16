# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 01:12:39 2017

@author: USER
"""

#%%
from k_dataset import DataSet

#%%
dataset = DataSet()
#stances = dataset.stances   # list(dict), dict key: 'Body ID', 'Headline', 'Stance'
articles = dataset.articles # dict, {int(Body ID) : articleBody}
