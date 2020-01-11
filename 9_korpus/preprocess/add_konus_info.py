import pandas as pd
import numpy as np

df=pd.read_excel('KONUS_9_without.xls')
for i in df.index:
    df.loc[i,'Data']=df.Data[i].lstrip('0')
df ['Data1']='Data '
df ['Data1']+=df ['Data']
df ['Vanna1']='Vanna '
df ['Vanna1']+=df ['Vanna'].astype('str')
df ['opisanie_konusa1']='opisanie_konusa '
df ['opisanie_konusa1']+=df ['opisanie_konusa']
df ['№_anoda_with_konus1']='№_anoda_with_konus '
df ['№_anoda_with_konus1']+=df ['№_anoda_with_konus'].astype('str')
df=df.drop(columns=['Data', 'Vanna','№_anoda_with_konus','opisanie_konusa'])
df=df.rename(columns={"Data1": "Data", "Vanna1": "Vanna","№_anoda_with_konus1":"№_anoda_with_konus","opisanie_konusa1":"opisanie_konusa"})
df.Vanna[df.Vanna=='Vanna 9163']+=' (Откл. Кап.)'
df.Vanna[df.Vanna=='Vanna 9048']+=' (Пуск Кап.)'
df.Vanna[df.Vanna=='Vanna 9077']+=' (Пуск Кап.)'

df1=pd.read_excel('with_names.xlsx',index_col=0)
'''

#df1=df1.combine_first(df)
'''
k=0
df1['№_anoda_with_konus']= np.nan
df1['opisanie_konusa']= 'opisanie_konusa no_konus'
for i in df.index:
    Flag=1
    for j in df1.index:
        
        if df['Data'][i]==df1['Data'][j]:
          if df['Vanna'][i]==df1['Vanna'][j]: 
              df1.loc[j,'opisanie_konusa']=df.loc[i,'opisanie_konusa']
              df1.loc[j,'№_anoda_with_konus']=df.loc[i,'№_anoda_with_konus']
              k+=1
              Flag=0
              break
    if Flag==1:
        print(df.Data[i],df.Vanna[i])
print(k)
