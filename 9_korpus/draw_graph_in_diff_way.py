# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:37:34 2020

@author: Dima
"""

from graphviz import Digraph
import pandas as pd
import numpy as np

def create_general_lifts(list_items,key_value,transactions):
    list_lifts=[]
    for i in list_items:
        key_list=[]
        key_list.append(key_value)
        full_transaction=i.copy()
        full_transaction.append(key_value)
        x_y=0
        x=0
        y=0
        for j in transactions:
            if set(full_transaction).issubset(j):
                x_y+=1
            if set(i).issubset(j):
                x+=1
            if set(key_list).issubset(j):
                y+=1
        x_y/=len(transactions)
        y/=len(transactions)
        x/=len(transactions)
        list_lifts.append((x_y)/(x*y))    
    return list_lifts
    
def plotting_graph(df_name,all_data,node_count=3):
    out1=all_data.values.tolist()
    transactions=[]
    for i in out1:
        transactions.append([x for x in i if str(x) != 'nan'])
    df=pd.read_pickle(df_name)
    key_value=df.items_add.value_counts().index[0][0]
    list1=[]
    for i in df.index:
        if df.items_add[i][0]!=key_value:
            list1.append(i)
    df=df.drop(list1)
    df=df.reset_index(drop=True)
    df=df.sort_values(by=['support'],ascending=False)
    list_items=[]
    list_supp=[]
    
    for j in range(2,max(df.len_of_trans)+1):
        list1=[]
        k=0
        for i in df.index:
            if df.len_of_trans[i]==j:
                list1.append(i)
                if k<node_count:
                    list_items.append(df.items_base[i])
                    list_supp.append(df.support[i])
                    k+=1
        df=df.drop(list1)
        df=df.reset_index(drop=True)
    list_lifts = create_general_lifts(list_items,key_value,transactions)
    #Построение графа
    dot = Digraph(comment='The Round Table', format='png')
    #Создание всех вершин, их индексов
    dot.node('-1', 'Base Value:\n'+key_value)
    for i in range(len(list_items)):
        len_items=len(list_items[i])
        supp=float('{:.3f}'.format(list_supp[i]*100))
        lift=float('{:.3f}'.format(list_lifts[i]))
        if len_items==1:
            dot.node(str(i), 'support = '+str(supp)+'\nlift = '+str(lift))
            dot.edge('-1', str(i), str(list_items[i][-1])+';')
        else:
            dot.node(str(i), 'support = '+str(supp)+'\nlift = '+str(lift))
    for i in range(len(list_items)): 
        if len(list_items[i])!=1:
            list_of_edges=[]
            list_num_edges=[]
            list_true_edges=[]
            list_labels=[]
            list_true_labels=[]
            #создание списка всех родительских вершин
            for j in list_items:
                if j!=list_items[i]:
                    if set(j).issubset(list_items[i]):
                        list_of_edges.append(j)
            #Определение пересекающихся вершин
            for j in range(len(list_of_edges)):
                for k in range(len(list_of_edges)):
                    if j!=k:
                        if set(list_of_edges[j]).issubset(list_of_edges[k]):
                            list_num_edges.append(j)

            list_num_edges=list(np.unique(list_num_edges))
            #Удаление пересекающихся вершин
            for j in range(len(list_of_edges)):
                if not(j in(list_num_edges)):
                    list_true_edges.append(list_of_edges[j])
            #построение списка всех "вышестоящих" элементов
            for j in list_items[i]:
                for k in list_true_edges:
                    if (j in k)&(not(j in list_labels)):
                        list_labels.append(j)
            #построение списка добавочных элементов            
            for j in list_items[i]:
                if not(j in list_labels):
                   list_true_labels.append(j) 
            label_str=''
            for j in list_true_labels:
                if label_str!='':
                    label_str+=', '
                label_str+=j
            label_str+=';'
            ####
            ####Построение вершин графа
            ####
            for j in list_true_edges:
                for k in range(len(list_items)):
                    if k!=i:
                        if j==list_items[k]:
                            if list_true_labels==[]:
                                dot.edge(str(k),str(i))
                            else:
                                dot.edge(str(k),str(i),label_str)
            #dot.edge(str(), str(i), constraint='false')     
        '''
        if len_items==1:
            dot.edge(key_value+' support = 100%','['+key_value+", '"+list_items[i][0]+"']",'support = '+str(supp)+'%, lift = '+str(lift)) 
        else:
            for j in range(len(list_items)):
                if ((len_items>len(list_items[j]))&(set(list_items[j]).issubset(list_items[i]))&(counter<len(list_items[j]))):
                    counter=len(list_items[j])
                    upper_level=(list_items[j])
            dot.edge('['+key_value+', '+str(upper_level)[1:-1]+']','['+key_value+', '+str(list_items[i])[1:-1]+']','support = '+str(supp)+'%, lift = '+str(lift))         
        '''
    print(dot.source)  
    dot.render(df_name[:-4], view=False) 
    


#all_data=pd.read_excel('9_korpus_data_with_konus.xlsx',index_col=0)
df_name='./base_not_base/Base_AE_0.pkl'
plotting_graph(df_name,all_data)
df_name='./base_not_base/Base_AE_1.pkl'
plotting_graph(df_name,all_data)
df_name='./base_not_base/Base_Konus.pkl'
plotting_graph(df_name,all_data)
df_name='./base_not_base/Base_Kozirek.pkl'
plotting_graph(df_name,all_data)
df_name='./base_not_base/Base_no_konus.pkl'
plotting_graph(df_name,all_data)
df_name='./base_not_base/Base_Otstavanie.pkl'
plotting_graph(df_name,all_data)
df_name='./base_not_base/Base_podern_anod_0.pkl'
plotting_graph(df_name,all_data)
df_name='./base_not_base/Base_podern_anod_1.pkl'
plotting_graph(df_name,all_data)
