# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:02:27 2019

@author: Dima
"""

import pandas as pd

df=pd.read_pickle('associative_analysis10%.pkl')
s=[]
for i in df.index:
    if len(df['items'][i])==1:
        s.append(i)
df=df.drop(s)
df=df.reset_index(drop=True)
s=[]
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
for i in df.index:
    for j in df['ordered_statistics'][i]:
        if (j['confidence']>=0.3)&(j['lift']>=1.2):
            s.append(j['items_base'])
            s1.append(j['items_add'])
            s2.append(j['confidence'])
            s3.append(j['lift'])
            s4.append(df['support'][i])
            s5.append(len(df['items'][i]))
d={'items_base':s,'items_add':s1,'confidence':s2,'lift':s3,'support':s4,'len_of_trans':s5}
df1 = pd.DataFrame(data=d)
df1.to_pickle('lift-1,2_conf-0,3.pkl')
df1.to_excel('lift-1,2_conf-0,3.xlsx')