# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:27:44 2019

@author: Dima
"""
import pandas as pd
import numpy as np
df=pd.read_excel('quantile_9_k_itog.xlsx',index_col=0)
df1=df.copy()
names=df1.columns
for i in names:
        print(i)
        first=i+' '+df1[i][df1[i].isna()==False].astype('str')
        second=df1[i][df1[i].isna()]
        first=first.combine_first(second)
        df1[i]=first
print('end_of main_fragment')
df1.to_excel('with_names.xlsx') 