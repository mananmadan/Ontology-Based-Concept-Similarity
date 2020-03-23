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
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.show()
