#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:12:38 2020

@author: manan
"""
import nltk
#import spacy
import re
import pandas as pd
import plotly
import plotly.plotly as py

#mport plotly.io as pio
from plotly.graph_objs import *
#import chart_studio
plotly.tools.set_credentials_file(username='mananmadan', api_key='UhMT29mjWxk9tBh2cnYB')
import networkx as nx
import matplotlib.pyplot as plt
from nltk.tokenize import PunktSentenceTokenizer
pst = PunktSentenceTokenizer()
openfile = open("data.txt")
data = openfile.read()
data=data.decode('utf-8')

print (data)
tokenized_sentence = pst.tokenize(data)
stringlist = []
for i in tokenized_sentence:
  try:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    chunkGram = r"""Chunk: {<JJ.?>*<NN.?>{0,1}<NN..?>{0,1}}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    print(chunked)
    stringlist.append(chunked.pformat().encode('ascii','ignore'))
  except Exception as e:
      print(str(e))
#print(len(stringlist[1]))
#String = stringlist[1]
index = 0
listoflist = []
for f in stringlist:
 String = f
 #print(len(String))
 chunklist = []
 iter = re.finditer(r"\Chunk\b", String)
 indices = [m.start(0) for m in iter]
 #print(indices)
 for x in indices:
#print(stringlist[1][x+5])#space
#get the word from space till /
#print(x)
  j=1
  temp =""
  while(stringlist[index][x+5+j]!=')'):
   temp = temp + stringlist[index][x+5+j]
   j = j+1
 # print(temp)
  chunklist.append(temp)
 index = index + 1
 listoflist.append(chunklist)
print(listoflist)
#make a source list and make a target list
#first n-1 in a list are source and last n-1 are in the target list
#add them to pandas data frame
#form the graph
source = []
target = []
for i in listoflist:
 temp_source = []
 temp_target = []
 for j in i:
   temp_source.append(j)
   temp_target.append(j)
 if len(temp_source)!=0 and len(temp_target)!=0:
  temp_source.pop(len(temp_source)-1)
  temp_target.pop(0)
 for x in temp_source:
     source.append(x)
 for y in temp_target:
     target.append(y)
final_source = []
final_target = []
for i in source:
  final_source.append('('+ i +')')
  
for i in target:
  final_target.append('('+ i + ')')
  
print(source)
print(target)  
kg_df = pd.DataFrame({'source':final_source, 'target':final_target})
print("printing pandas data frame--------")
print(kg_df)
G=nx.from_pandas_edgelist(kg_df, "source", "target")
edge_x = []
edge_y = []
for edge in G.edges():
    print("hello")
    x0, y0 = G.nodes[edge[0]]
    x1, y1 = G.nodes[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    #print(node)
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))
node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text
        
fig = Figure(data = Data([edge_trace, node_trace]),
             layout = Layout(
                 title = 'Knowledge Graph',
                 titlefont = dict(size = 16),
                 showlegend = True,
                 margin = dict(b = 20, l = 5, r = 5, t = 40),
                 annotations = [dict(
                     text = "sub title text",
                     showarrow = False,
                     xref = "paper", yref = "paper",
                     x = 0.005, y = -0.002)],
                 xaxis = XAxis(showgrid = False, 
                               zeroline = False, 
                               showticklabels = False),
                 yaxis = YAxis(showgrid = False, 
                               zeroline = False, 
                               showticklabels = False)))
print("no err")
py.plot(fig, username = 'mananmadan',filename = 'networkx')
#pio.show(fig)
somelist = [[0,""]]
done = []
for i in final_source :
  temp_sum = 0
  conn_nodes = 0
  for j in final_target:
   try:
    temp_sum = temp_sum + nx.shortest_path_length(G,i,j)    
    if nx.shortest_path_length(G,i,j) == 1 :
     conn_nodes = conn_nodes + 1#directly connected nodes
   except:
    temp_sum = temp_sum + 0
  if i not in done :
     somelist.append((temp_sum/conn_nodes,i))
     done.append((i))
somelist.sort()
print("sort()")
for i in somelist:
    print(i)
somelist.sort(reverse = True)
print("reverse_sort()")
for i in somelist:
    print(i)    
plt.figure(figsize=(12,12))
random = []
count =0
for i in final_source:
 count=count+1 
 if count%2==0 :
   random.append(i)
pos = nx.bipartite_layout(G,random)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.show()
