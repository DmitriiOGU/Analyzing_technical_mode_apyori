# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:37:34 2020

@author: Dima
"""

from graphviz import Digraph
dot = Digraph(comment='The Round Table', format='png')
for i in range(20):
            dot.edge(str(i),str(i-1))
print(dot.source)  
dot.render('round-table', view=True) 