# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:32:22 2019

@author: Dima
"""

import pandas as pd

df=pd.read_excel('9_korpus.xlsx')

quantile_write=df.quantile([.25,.5,.75,1])
'''
quantile_write.to_excel('quantiles.xlsx')
'''
i='Kol_rab_el_ov'
res=df[i][df[i].isna()]
first=df[i][(df[i]=='обж.')]
for j in first.index:
    first.at[j]=0
first+=2
second=df[i][(df[i]=='раб.')]
for j in second.index:
    second.at[j]=0
second+=1
third=df[i][(df[i]=='откл.')]
for j in third.index:
    third.at[j]=0
res=res.combine_first(first)
res=res.combine_first(second)
res=res.combine_first(third)
'''
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df1 = pd.DataFrame(res)
df['C'] = [7, 8, 9]
'''
df1 = pd.DataFrame(res)
df[i]=res
for i in quantile_write.columns:
    q1=quantile_write[i][.25]
    q2=quantile_write[i][.5]
    q3=quantile_write[i][.75]
    q4=quantile_write[i][1]
    res=df[i][df[i].isna()]
    if q1==q2==q3==0:
        print ('3=0',i)
        first=df[i][(df[i]==0)]
        first*=0
        second=df[i][(df[i]!=0)]
        second*=0
        second+=1
        res=res.combine_first(first)
        res=res.combine_first(second)
        df1[i]=res
        df[i]=res
        continue
    if q1==q2==0:
        print ('2=0',i)
        first=df[i][(df[i]==0)]
        first*=0
        second=df[i][(df[i]<=q3)]
        second*=0
        second+=1
        third=df[i][(df[i]>q3)]
        third*=0
        third+=2
        res=res.combine_first(first)
        res=res.combine_first(second)
        res=res.combine_first(third)
        df1[i]=res
        df[i]=res
        continue
    first=df[i][(df[i]<=q1)]
    first*=0
    second=df[i][(df[i]>q1)&(df[i]<=q2)]
    second*=0
    second+=1
    third=df[i][(df[i]>q2)&(df[i]<=q3)]
    third*=0
    third+=2
    forth=df[i][(df[i]>q3)&(df[i]<=q4)]
    forth*=0
    forth+=3
    res=res.combine_first(first)
    res=res.combine_first(second)
    res=res.combine_first(third)
    res=res.combine_first(forth)
    df1[i]=res
    df[i]=res
df=df.replace(-0,0)
df1=df1.replace(-0,0)
df1.to_excel('quantile_9_k_df1.xlsx')
df.to_excel('quantile_9_k_df.xlsx')

'''
    df[i]=df[i].replace(df[i][(df[i].dropna()<=quantile_write[i][.25])].values,0)
                        df[i][(df[i].dropna()>quantile_write[i][.25])&(df[i].dropna()<=quantile_write[i][.5])].values ,
                        df[i][(df[i].dropna()>quantile_write[i][.5]) &(df[i].dropna()<=quantile_write[i][.75])].values,
                        df[i][(df[i].dropna()>quantile_write[i][.75])&(df[i].dropna()<=quantile_write[i][1])].values ],
                        [0,1,2,3])
'''    