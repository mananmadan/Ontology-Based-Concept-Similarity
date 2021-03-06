import urllib2
from urllib2 import urlopen
from cookielib import CookieJar
import time
import urllib
from collections import defaultdict
from SPARQLWrapper import SPARQLWrapper,JSON
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import requests
import wikipedia
import networkx as nx
#import matplotlib.pyplot as plt
Graph={}
levels=2
#limit=""
list_of_nodes=[]

def get_nodes():
    openfile=open("nodes.txt","r")
    t=openfile.readlines()
    for x in t:
        #print(x)
        x=x.encode("utf-8")
        x=re.sub(r"/[A-Z][A-Z][A-Z]*","",x)
        x=re.sub(r"/"," ",x)
        x=re.sub(r"\n","",x)
        list_of_nodes.append(x)

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#login_data = urllib.parse.urlencode({'login' : 'admin', 'pass' : '123'})

opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

#eachthing = wikipedia.page(city_tags[0]['value']).categories
#print(eachthing)

# for scraping informatin from wikipedia

wikipedia.set_lang("en")



def my_f(query):    #extracting wikipedia tags from a query
 #wikiterm = wikipedia.search(query)
 dx = 0
 # To eleminate exceptions in wikipedia categories
 try:
    page = wikipedia.page(query)
 except wikipedia.exceptions.DisambiguationError as e:
  dx=10
 except wikipedia.exceptions.PageError as e:
  #print e
  dx=10
 if dx == 0:
  if urllib.urlopen(wikipedia.page(query).url).getcode() == 200 :
   content = opener.open(wikipedia.page(query).url).read()
   soup2 = bs(content,'html.parser')
   cat1 = soup2.find_all("div",{'class':'mw-normal-catlinks'})
   cat2 = cat1[0].find_all('a')
   d=0
   list=[]
   for i in cat2:
    if d != 0:
     list.append(str(i.text.encode('utf8')))
    d=d+1
 else:
     return []
 return list

def id_extractor(search_string):
    #print(type(wikipedia.search(search_string)))
    query=""
    try:
        query = wikipedia.search(search_string)[0]
    except :
        return "-1","-1"

    #print(query)
    new_string = ""
    for i in query:
        if i == " ":
            new_string = new_string + '_'
        else:
            new_string = new_string + i
    #print("New string")
    print("****************************************************************************")
    print("Searching for {}".format(new_string))

    res = requests.get("https://en.wikipedia.org/wiki/"+new_string)
    soup = bs(res.text, "html.parser")
    wikidata = []
    for link in soup.find_all("a"):
        url = link.get("href", "")
        if "//www.wikidata.org/" in url:
            wikidata.append(url)
            #print(url)
    #print(wikidata)

    count = 0
    wikidata_id  = ""
    for i in wikidata[0]:
        if i == 'Q' or i == '1' or i == '2' or i =='0' or i =='3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            wikidata_id = wikidata_id + i
    res = requests.get(wikidata[0])
    soup = bs(res.text, "html.parser")
    #print(soup)
    node=""
    for hit in soup.findAll(attrs={'class' : 'wikibase-title-label'}):
        node= hit.text
    return wikidata_id.encode("utf-8"),node.encode("utf-8")


def result_gen_children(prop,id):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    q="""
    SELECT ?item ?itemLabel
    WHERE
    {
        ?item wdt:P361?/wdt:P279? wd:Q245652 .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
    }
    """
    q=re.sub(r"Q245652",id,q)
    #q=re.sub(r"P361",prop,q)

    sparql.setQuery(q)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results


def result_gen_parent(prop,id):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    q="""
    SELECT ?item ?itemLabel
    WHERE
    {
        wd:Q245652 wdt:P361?/wdt:P279? ?item   .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
    }
    """
    q=re.sub(r"Q245652",id,q)
    sparql.setQuery(q)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results


def chilldren(node,id,level):
    if level==levels:
        return

    results = result_gen_children("P361",id)
    results_df = pd.io.json.json_normalize(results['results']['bindings'])

    if node not in Graph.keys():
        Graph[node]=[]
    if not results_df.empty:
        for x,y in zip(results_df["item.value"] , results_df["itemLabel.value"] ) :
            x=x.encode("utf-8")
            y=y.encode("utf-8")
            #print(y)
            x=re.sub(r"http://www.wikidata.org/entity/","",x)
            if y not in Graph[node]:
                if y!=node:
                    Graph[node].append(y)
            if y not in Graph:
                chilldren(y,x,level+1)

def parent(node,id,level):
    if level==levels:
        return

    results = result_gen_parent("P361",id)
    results_df = pd.io.json.json_normalize(results['results']['bindings'])
    Graph[node]=[]
    if node not in Graph.keys():
     if not results_df.empty:
        for x,y in zip(results_df["item.value"] , results_df["itemLabel.value"] ) :
            x=x.encode("utf-8")
            y=y.encode("utf-8")
            x=re.sub(r"http://www.wikidata.org/entity/","",x)
            #print(y)
            if y not in Graph:
                Graph[y]=[]
                if y!=node:
                    Graph[y].append(node)
                parent(y,x,level+1)
            else:
                if y!=node:
                    Graph[y].append(node)
    list_of_query = my_f(node)
    if  len(list_of_query)>0:
        print(level,[node,list_of_query])
        for y in list_of_query:
            id,new_node=id_extractor(y)
            if(id!="-1"):
                if new_node not in Graph:
                    Graph[new_node]=[]
                    if new_node!=node:
                        Graph[new_node].append(node)
                    parent(new_node,id,level+1)
                else:
                    if new_node!=node:
                        Graph[new_node].append(node)
            #wikipidea_s(level+1,x)

def save_graph(filename):
    open(filename, 'w').close()
    fout=open(filename,"w")
    for x in Graph:
        #x=x.encode("utf-8")
        fout.write(x)
        fout.write("\n")
        for y in Graph[x]:
            #y=y.encode("utf-8")
            fout.write(y)
            fout.write("\n")
        fout.write("-1\n")
    fout.close()


def load_graph():
    fin=open("graph.txt","r")
    lines=fin.readlines()
    is_key=True
    for x in lines:
        x=x.strip()
        if is_key:
            key=x
            is_key=False
            Graph[key]=[]
        else:
            if(x=="-1"):
                is_key=True
            else:
                Graph[key].append(x)

#Not Tested Yet
def reduce_graph():
    flag=True
    while flag:
        print("$")
        to_delete=[]
        flag=False
        for x in Graph:
            if x not in list_of_nodes:
                if len(Graph[x])==0:
                    to_delete.append(x)
        for x in to_delete:
            Graph.pop(x)
            for y in Graph:
                if x in Graph[y]:
                    Graph[y].remove(x)
                    flag=True




def Graph_gen():
    load_graph()
    for node in list_of_nodes:
        save_graph("prev_graph.txt")
        id,node=id_extractor(node)
        if id!="-1":
            if node not in Graph:
                chilldren(node,id,0)
                parent(node,id,0)
                #print(Graph)
                save_graph("graph.txt")

get_nodes()
list_of_nodes=list(dict.fromkeys(list_of_nodes))


#save_graph("temp.txt")
Graph_gen()
load_graph()
for x in Graph:
    Graph[x]=list(dict.fromkeys(Graph[x]))
count=0
 #reduce_graph()
for x in Graph:
     if len(Graph[x])==1:
         for y in Graph[x]:
             if y in Graph[x]:
                 count+=1
print(count)
#
# print("***************")
source = []
target = []
for x in Graph:
     for y in Graph[x]:
         if x!=y:
             source.append(x)
             target.append(y)
kg_df = pd.DataFrame({'source':source, 'target':target})

G=nx.from_pandas_edgelist(kg_df, "source", "target",create_using=nx.DiGraph())
print(G)
H = G.to_undirected()
print(G["computer science"])

print("Main Concepts.....")




# #which subject you want to find
sub1  = "electronics"
sub2 =  "computer science"
#
# ## which concept you want to find
concept = "neuroinformatics"
#
print("main concepts",G[sub1])
print("main concepts",G[sub2])
# ##check if this the main concept in any of the subjects
is_main = 0
ans = " "
for i in G[sub1]:
    if i == concept:
        is_main = 1
        ans = sub1

if is_main == 1:
    print(ans)

if is_main == 0:
    for i in G[sub2]:
       if i == concept:
           is_main = 1
           ans = sub2

if is_main == 1:
 print(ans)
# ##check how many main concept is this topic related

count1 = 0
count2 = 0
if is_main == 0:
    for i in G[sub1]:
        if nx.has_path(G,i,concept):
            count1 = count1 + 1
if is_main == 0:
    for i in G[sub2]:
        if nx.has_path(G,i,concept):
            count2 = count2 + 1

print(count1,count2)
# '''
# temp_source = []
# temp_target = G["electronics"]
# for i in range(len(temp_target)):
#     temp_source.append("electronics")
# kg_df_neb = pd.DataFrame({'source':temp_source,'target':temp_target})
# temp = nx.from_pandas_edgelist(kg_df_neb, "source", "target",create_using=nx.DiGraph())
# plt.figure(figsize=(12,12))
# pos = nx.spring_layout(temp)
# nx.draw(temp, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
# plt.show()
#
# # # Spectral
# nx.draw(temp, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos=nx.spectral_layout(temp))
# plt.title("spectral")
# plt.show()
