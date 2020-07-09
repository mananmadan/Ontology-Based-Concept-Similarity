#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:12:38 2020
@author: manan
"""
import nltk
import re
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import spacy
from nltk.tokenize import PunktSentenceTokenizer
nlp = spacy.load('en')

def get_nodes(x):
    ##openfile=open("nodes.txt","r")
    ##t=openfile.readlines()
    ##for x in t:
        #print(x)
        try:
          x=x.encode("utf-8")
          x=re.sub(r'/[^\s]+','',x)
          print("removed",x)
        except:
          print("not able to do on",x)
        
        return x 
  

pst = PunktSentenceTokenizer()
openfile = open("data.txt")
data = openfile.read()
data=data.decode('utf-8')
rootlist = []
print (data)

tokenized_sentence = pst.tokenize(data)
stringlist = []
for i in tokenized_sentence:
  try:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    chunkGram = r"""Chunk: {<JJ.?>{0,2}<VBG>{0,1}<NN.?>{1,2}<VBG>{0,1}<NN..?>{0,2}<VBG>{0,1}}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    print(chunked)
    ##let's also store the roots
    doc = nlp(i)
    for tok in doc:
      if tok.dep_== "ROOT":
        rootlist.append(tok.text)
    #chunked.draw()
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
   temp_source.append(get_nodes(j))
   temp_target.append(get_nodes(j))
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
  temp_count = 0
  for j in final_target:
   try:
    temp_sum = temp_sum + nx.shortest_path_length(G,i,j)
    if nx.shortest_path_length(G,i,j) == 1 :
     conn_nodes = conn_nodes + 1#directly connected nodes
    for temp in final_source :
       if temp == i :
        temp_count = temp_count+1
   except:
    temp_sum = temp_sum + 0
  if i not in done :
     somelist.append((2*(conn_nodes)+0*(temp_count)+1*(len(i)),i))
     done.append((i))
somelist.sort(reverse = True)
output = []
temp_somlist_count = 0
for i in somelist:
 if temp_somlist_count==15:
     break
 else :
    output.insert(temp_somlist_count,i)
    temp_somlist_count = temp_somlist_count+1
print("printing list")
unique = []
for i in final_target :
 if i not in unique:
  unique.append(i)
for j in final_target:
 if j not in unique:
   unique.append(j)
for i in unique:
 print(i)
print("B")
for i in unique:
  temp_count = 0 
print(rootlist)
'''
  for j in final_source:
     if nx.shortest_path_length(G,i,j) == 1:
        temp_count = temp_count + 1
  print(temp_count)      
print("output")
for i in output:
 print(i[1])
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.show()
'''