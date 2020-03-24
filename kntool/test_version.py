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
from nltk.tokenize import PunktSentenceTokenizer



#reading the data:
pst = PunktSentenceTokenizer()
openfile = open("data.txt")
data = openfile.read()
data=data.decode('utf-8')

#tokenizing:
tokenized_sentence = pst.tokenize(data)

#making a list for storing pos vs original word
wordlist = []


#chunk formation and converting to a string:
stringlist = []
for i in tokenized_sentence:
  #try:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    count=0
    for i in words:#loop to map pos form to original word
        #print(tagged[count][0]+"/"+tagged[count][1])
        if len(tagged[count])==2:
         wordlist.append([tagged[count][0]+"/"+tagged[count][1]])
         count = count+1

    chunkGram = r"""Chunk: {<JJ.?>{0,2}<VBG>{0,1}<NN.?>{1,2}<VBG>{0,1}<NN..?>{0,2}<VBG>{0,1}}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    print(chunked)
    stringlist.append(chunked.pformat().encode('ascii','ignore'))
  #except Exception as e:
     # print(str(e))




#string extraction:
index = 0
listoflist = []
for f in stringlist:
 String = f
 chunklist = []
 iter = re.finditer(r"\Chunk\b", String)
 indices = [m.start(0) for m in iter]
 for x in indices:
  j=1
  temp =""
  while(stringlist[index][x+5+j]!=')'):
   temp = temp + stringlist[index][x+5+j]
   j = j+1
  chunklist.append(temp)
 index = index + 1
 listoflist.append(chunklist)
#print(listoflist)






#graph connection :
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




#putting data into the data frame and creating graph:
kg_df = pd.DataFrame({'source':final_source, 'target':final_target})
print("printing pandas data frame--------")
print(kg_df)
G=nx.from_pandas_edgelist(kg_df, "source", "target")



max = 0
final_k1=0
final_k2=0
final_k3=0
#doing data analysis:
for k1 in range(0,40):
    for k2 in range(0,40):
        for k3 in range(0,40):
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
                     somelist.append((k1*(conn_nodes)+k2*(temp_count)+k3*(len(i)),i))
                     done.append((i))
                #somelist.sort()
                #print("sort()")
                #for i in somelist:
                    #print(i)
                somelist.sort(reverse = True)
                #print("reverse_sort()")
                #for i in somelist:
                    #print(i)


                ##extract info for control loop
                output = []
                temp_somlist_count = 0
                for i in somelist:
                 if temp_somlist_count==10:
                     break
                 else :
                    output.insert(temp_somlist_count,i)
                    temp_somlist_count = temp_somlist_count+1

                print(output)

                #find if matching is possible:
                expected_output = ["artificial intelligence","computer","human intelligence","computer program","human being","expert system","specific domain","natural language","computer vision","real life scene"]
                final_count = 0
                for i in output:
                    for j in expected_output:
                       #print(j)
                       relist = re.split(r'\s',j)
                       #print(relist)
                       for temp in relist:
                           if re.search(temp,i[1]):
                               #print("finding in")
                               #print(i[1])
                               final_count = final_count+1

                if final_count>max:
                 max = final_count
                 print("improved:")
                 print(str(max)+str(":")+str(k1)+str(":")+str(k2)+str(":")+str(k3))
                 final_k1 = k1
                 final_k2 = k2
                 final_k3 = k3
print("final_values")
print(final_k1)
print(final_k2)
print(final_k3)
#plotting the graph:
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
#plt.show()
