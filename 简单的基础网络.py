# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import random

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
'''
各类基础图的构建
'''
plt.figure(figsize=(8,8))
plt.subplot(221)
cg=nx.complete_graph(15)
pos=nx.circular_layout(cg)
nx.draw(cg,node_size=500,with_labels=True,pos=pos)
plt.subplot(222)
cycle_g=nx.cycle_graph(15)
pos=nx.circular_layout(cycle_g)
nx.draw(cycle_g,node_size=500,with_labels=True,pos=pos)
plt.subplot(223)
sg=nx.star_graph(15)
# pos=nx.circular_layout(sg)
nx.draw(sg,node_size=500,with_labels=True)
plt.subplot(224)
wsg=nx.watts_strogatz_graph(15,2,0)
pos=nx.circular_layout(wsg)
nx.draw(wsg,node_size=500,with_labels=True,pos=pos)
n=10
G1=nx.Graph()
G1.add_nodes_from(list(range(n)))
plt.figure(figsize=(16,8))
plt.subplot(121)
nx.draw(G1,with_labels=True,pos=nx.circular_layout(G1)
        ,node_size=500,node_color='r')

#二维方格图
G2=nx.grid_graph((5,5),periodic=False)
plt.subplot(122)
nx.draw(G2,node_size=500,node_color='m',with_labels=True)
plt.show()

