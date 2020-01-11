# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:06:24 2019

@author: Dima
"""
import pandas as pd
import numpy as np
def date_normalize(df):
    year="2014"
    month="01"
    for i in range(len(df['Sutki'])):
        k=df['Sutki'].loc[i].find(' ')
        if int(df['Sutki'].loc[i][k+1:])<int(month):
            year=str(int(year)+1)
        month=df['Sutki'].loc[i][k+1:]
        df['Sutki'].loc[i]=df['Sutki'].loc[i][0:k]+"."+month+"."+year
    return df
def date_append(df):
    date=date_creation()
    date=pd.Series(date)
    new_df=pd.DataFrame({'Sutki':date})
    for i in df.columns[1:]:
        new_df[i]=np.nan
    for i in range(len(df['Sutki'])):
        for j in range(len(new_df['Sutki'])):
            if df['Sutki'][i]==new_df['Sutki'][j]:
                new_df.loc[j]=df.loc[i]
                break
    return new_df
def date_creation():
    date=[]
    #2014
    for i in range(1,32):
        date.append(str(i)+".01.2014")
    for i in range(1,29):
        date.append(str(i)+".02.2014")
    for i in range(1,32):
        date.append(str(i)+".03.2014")
    for i in range(1,31):
        date.append(str(i)+".04.2014")
    for i in range(1,32):
        date.append(str(i)+".05.2014")
    for i in range(1,31):
        date.append(str(i)+".06.2014")
    for i in range(1,32):
        date.append(str(i)+".07.2014")
    for i in range(1,32):
        date.append(str(i)+".08.2014")
    for i in range(1,31):
        date.append(str(i)+".09.2014")
    for i in range(1,32):
        date.append(str(i)+".10.2014")
    for i in range(1,31):
        date.append(str(i)+".11.2014")
    for i in range(1,32):
        date.append(str(i)+".12.2014")
    #2015
    for i in range(1,32):
        date.append(str(i)+".01.2015")
    for i in range(1,29):
        date.append(str(i)+".02.2015")
    for i in range(1,32):
        date.append(str(i)+".03.2015")
    for i in range(1,31):
        date.append(str(i)+".04.2015")
    for i in range(1,32):
        date.append(str(i)+".05.2015")
    for i in range(1,31):
        date.append(str(i)+".06.2015")
    for i in range(1,32):
        date.append(str(i)+".07.2015")
    for i in range(1,32):
        date.append(str(i)+".08.2015")
    for i in range(1,31):
        date.append(str(i)+".09.2015")
    for i in range(1,32):
        date.append(str(i)+".10.2015")
    for i in range(1,31):
        date.append(str(i)+".11.2015")
    for i in range(1,32):
        date.append(str(i)+".12.2015")
    #2016
    for i in range(1,32):
        date.append(str(i)+".01.2016")
    for i in range(1,30):
        date.append(str(i)+".02.2016")
    for i in range(1,32):
        date.append(str(i)+".03.2016")
    for i in range(1,31):
        date.append(str(i)+".04.2016")
    for i in range(1,32):
        date.append(str(i)+".05.2016")
    for i in range(1,31):
        date.append(str(i)+".06.2016")
    for i in range(1,32):
        date.append(str(i)+".07.2016")
    for i in range(1,32):
        date.append(str(i)+".08.2016")
    for i in range(1,31):
        date.append(str(i)+".09.2016")
    for i in range(1,32):
        date.append(str(i)+".10.2016")
    for i in range(1,31):
        date.append(str(i)+".11.2016")
    for i in range(1,32):
        date.append(str(i)+".12.2016")
    #2017
    for i in range(1,32):
        date.append(str(i)+".01.2017")
    for i in range(1,29):
        date.append(str(i)+".02.2017")
    for i in range(1,32):
        date.append(str(i)+".03.2017")
    for i in range(1,31):
        date.append(str(i)+".04.2017")
    for i in range(1,32):
        date.append(str(i)+".05.2017")
    for i in range(1,31):
        date.append(str(i)+".06.2017")
    for i in range(1,32):
        date.append(str(i)+".07.2017")
    for i in range(1,32):
        date.append(str(i)+".08.2017")
    for i in range(1,31):
        date.append(str(i)+".09.2017")
    for i in range(1,32):
        date.append(str(i)+".10.2017")
    for i in range(1,31):
        date.append(str(i)+".11.2017")
    for i in range(1,32):
        date.append(str(i)+".12.2017")
    #2018
    for i in range(1,32):
        date.append(str(i)+".01.2018")
    for i in range(1,29):
        date.append(str(i)+".02.2018")
    for i in range(1,32):
        date.append(str(i)+".03.2018")
    for i in range(1,31):
        date.append(str(i)+".04.2018")
    for i in range(1,32):
        date.append(str(i)+".05.2018")
    for i in range(1,31):
        date.append(str(i)+".06.2018")
    for i in range(1,32):
        date.append(str(i)+".07.2018")
    for i in range(1,32):
        date.append(str(i)+".08.2018")
    for i in range(1,31):
        date.append(str(i)+".09.2018")
    for i in range(1,32):
        date.append(str(i)+".10.2018")
    for i in range(1,31):
        date.append(str(i)+".11.2018")
    for i in range(1,32):
        date.append(str(i)+".12.2018")
    #2019
    for i in range(1,32):
        date.append(str(i)+".01.2019")
    for i in range(1,29):
        date.append(str(i)+".02.2019")
    for i in range(1,32):
        date.append(str(i)+".03.2019")
    for i in range(1,31):
        date.append(str(i)+".04.2019")
    for i in range(1,32):
        date.append(str(i)+".05.2019")
    for i in range(1,31):
        date.append(str(i)+".06.2019")
    for i in range(1,32):
        date.append(str(i)+".07.2019")
    for i in range(1,32):
        date.append(str(i)+".08.2019")
    for i in range(1,4):
        date.append(str(i)+".09.2019")
    return date