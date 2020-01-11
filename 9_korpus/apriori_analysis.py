# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:53:37 2019

@author: Dima
"""

import apyori 
import pandas as pd
from io import StringIO
import json

df=pd.read_excel('9_korpus_data_with_konus.xlsx',index_col=0)
df=df[df.opisanie_konusa=='opisanie_konusa Kozirek']
out1=df.values.tolist()
transactions=[]
for i in out1:
    transactions.append([x for x in i if str(x) != 'nan'])

results = list(apyori.apriori(transactions,min_support = 0.001))


output = []
for RelationRecord in results:
    o = StringIO()
    apyori.dump_as_json(RelationRecord, o)
    output.append(json.loads(o.getvalue()))
data_df = pd.DataFrame(output)
data_df.to_excel('associative_analysis_Kozirek_supp_0_1%.xlsx')
data_df.to_pickle('associative_analysis_Kozirek_supp_0_1.pkl')