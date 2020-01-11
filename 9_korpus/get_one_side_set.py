# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:55:17 2019

@author: Dima
"""

import pandas as pd
df=pd.read_pickle('associative_analysis_Otstavanie_supp_20%.pkl')
spisok_items=[]
spisok_support=[]
s=[]
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
s6=[]
for i in df.index:
    if len((df['items'][i]))==1:
        spisok_items.append(df['items'][i][0])
        spisok_support.append(df['support'][i])
        s.append(i)
df=df.drop(s)
s=[]
for i in df.index:
    minimum=1
    maximum=0
    for j in df['items'][i]:
        value=spisok_support[spisok_items.index(j)]
        if value>=maximum:
            maximum=value
        if value<=minimum:
            minimum=value
    #if maximum-minimum<90:
    for j in df['ordered_statistics'][i]:
            if len(j['items_base'])>=1:
                #if (((len(j['items_base'])==1)&((j['items_base'][0]=='Kol_podernutih_anodov 0.0')|(j['items_base'][0]=='Kol_podernutih_anodov 1.0')))|
                #        ((len(j['items_add'])==1)&((j['items_add'][0]=='Kol_podernutih_anodov 0.0')|(j['items_add'][0]=='Kol_podernutih_anodov 1.0')))):
                if (((len(j['items_base'])==1)&(j['items_base'][0]== 'opisanie_konusa Otstavanie'))|
                      ((len(j['items_add'])==1)&(j['items_add'][0]== 'opisanie_konusa Otstavanie'))):
                    s.append(j['items_base'])
                    s1.append(j['items_add'])
                    s2.append(j['confidence'])
                    s3.append(j['lift'])
                    s4.append(df['support'][i])
                    s5.append(len(df['items'][i]))
                    s6.append(maximum-minimum)
df1 = pd.DataFrame(data={'items_base':s,'items_add':s1,'confidence':s2,'lift':s3,'support':s4,'len_of_trans':s5,'Raznica_v_support':s6})
df1.to_pickle('./base_not_base/Base_Otstavanie.pkl')
df1.to_excel('./base_not_base/Base_Otstavanie.xlsx')