# Python Learning Process
# Name:Ayanami_LJ
# Time:2023/3/16
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

'''
注：引入networks、numpy、matplotlib库
本篇主要包括：
1.创建一个空图
  1.1添加节点、添加边、可视化、将图转化为邻接矩阵
  1.2已知邻接矩阵，创建图
  1.3加权图
  1.4有向图
  
2.度、平均度以及度分布
  2.1获取网络G的度、平均度、度分布
  2.2绘制频率直方图
  
3.路径和距离
  3.1最短路径、最短路径长度
  3.2平均集聚系数、全局集聚系数
'''

# #1.1创建一个空图(不包括边、结点)
# G=nx.Graph()#无向图
# #添加节点
# G.add_nodes_from([1,2,3,4])
# #添加边
# G.add_edges_from([(1,2),(3,4),(1,3),(1,4)])
# #可视化
# nx.draw(G,node_size=500,with_labels=True) #这边with_labels是显示点序号与否
# #将图转化为邻接矩阵
# AdjMatrix=nx.to_numpy_array(G)
# print(AdjMatrix)
# plt.show()
#
#
# #1.2已知邻接矩阵，创建图
# AdjMatrix=np.random.randint(0,2,(3,3))
# print(AdjMatrix)
# G=nx.from_numpy_array(AdjMatrix)
# nx.draw(G,node_size=500,with_labels=True)
# plt.show()
#
# #1.3 加权图
# G=nx.Graph()
# G.add_nodes_from([1,2,3])
# G.add_weighted_edges_from([(1,2,4),(2,3,7.5),(1,3,2)])
# nx.draw(G,node_size=500,with_labels=True)
# AdjMatrix=nx.to_numpy_array(G)
# print(AdjMatrix)
# plt.show()
#

# #1.4有向图
# G=nx.DiGraph()
# G.add_nodes_from([1,2,3,4])#添加节点
# G.add_edges_from([(1,2),(3,4),(1,3),(1,4)])#添加边
# nx.draw(G,node_size=500,with_labels=True)#可视化
# AdjMatrix=nx.to_numpy_array(G)#将图转化为邻接矩阵
# print(AdjMatrix)
# plt.show()


#
# #2.度、平均度以及度分布
# #创建图
# G=nx.Graph()
# G.add_nodes_from([1,2,3,4])
# G.add_edges_from([(1,2),(3,4),(1,3),(1,4)])
# nx.draw(G,node_size=500,with_labels=True)
# AdjMatrix=nx.to_numpy_array(G)
# print(AdjMatrix)
# d=nx.degree(G)
# print(d)
# d=dict(nx.degree(G))
# print('各个结点的度为：',d)
# print('平均度为：',sum(d.values())/len(G.nodes))
# print(nx.degree_histogram(G))
# #此处nx.degree_histogram(G)的意思是拥有k个结点的节点数为nk，p（k）=nk/n
#
# x=list(range(max(d.values())+1)) #range(最大度+1),因为range不取最后一位，所以要+1
# y=[i/sum(nx.degree_histogram(G)) for i in nx.degree_histogram(G)]
# #这边是算度为k的结点的频率
# print('x',x)
# print('y',y)
# plt.figure()
# plt.bar(x,y,width=0.5,color='k') #绘制直方图
# plt.xlim([0,4])
# plt.xlabel('$k$')
# plt.ylabel('$P(k)$')
# plt.show()


#3.路径和距离

G=nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(3,4),(2,3),(4,5),(2,5)])
nx.draw(G,node_size=500,with_labels=True)
#求两点之间的所有最短路径
print('两点之间的所有最短路径为：',list(nx.all_shortest_paths(G,source=1,target=4)))
#求两点之间的最短路径长度
print('两点之间的最短路径长度为：',nx.shortest_path_length(G,source=1,target=4))
#求整个网络的平均距离
print('整个网络的平均距离为：',nx.average_shortest_path_length(G))#等效与下面的算法
plt.show()
# sum=0
# for i in range(2,len(G.nodes)+1):
#     sum+=nx.shortest_path_length(G,source=1,target=i)
#     pass
# print('平均距离为：',sum/len(G.nodes))
# plt.show()
# G.add_edges_from([(1,2,1),(3,4,5),(2,3,3),(4,5,7),(2,5,2)])

#平均集聚系数