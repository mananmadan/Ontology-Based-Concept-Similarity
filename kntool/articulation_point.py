import nltk
import spacy
import re
import pandas as pd
#import bs4
#import requests
#from spacy import displacy
#from nltk.tokenize import sent_tokenize
#nlp = spacy.load('en_core_web_sm')
#from spacy.matcher import Matcher
from spacy.tokens import Span
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
from nltk.tokenize import PunktSentenceTokenizer
pst = PunktSentenceTokenizer()
openfile = open("data.txt")
data = openfile.read()
data=data.decode('UTF-8','ignore')

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
print(source)
print(target)
kg_df = pd.DataFrame({'source':source, 'target':target})
print("printing pandas data frame--------")
print(kg_df)
G=nx.from_pandas_edgelist(kg_df, "source", "target")

temp_list=list(nx.articulation_points(G))

somelist = [[0,""]]
for i in source :
  temp_sum = 0
  conn_nodes = 0
  for j in target:
   try:
    temp_sum = temp_sum + nx.shortest_path_length(G,i,j)
    if(nx.shortest_path_length(G,i,j)==1):
      conn_nodes = conn_nodes + 1
   except:
    temp_sum = temp_sum + 0
  somelist.append((temp_sum/conn_nodes,i))
somelist.sort()
print("sort()") #For Testting
flag=0 #For Testting
#print(len(somelist))
answer_list=[]
for i in somelist:
    if(i[1] in temp_list):
        if(i[1].find("NN")!=-1):
            answer_list.append(i)
            flag+=1
#answer_list=list(dict(answer_list))

res = [] 
[res.append(x) for x in answer_list if x not in res] 
for x in res:
    print(x)

#print(flag) #For Testting
#print(len(res)) #For Testting
answer_list=[]
res=[]

print("reverse_sort()") #For Testting
somelist.sort(reverse = True)
for i in somelist:
    if(i[1] in temp_list):
        if(i[1].find("NN")!=-1):
            answer_list.append(i)
#res = [] 
[res.append(x) for x in answer_list if x not in res] 
for x in res:
    print(x)


plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.show()
