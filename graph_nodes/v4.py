from SPARQLWrapper import SPARQLWrapper,JSON
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import pickle
import requests
import wikipedia
import plotly
import plotly.Graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt
from numpy import array

labels = {}
appeared = {}
cncpt_ls  = []
graph={}
levels=2
#limit=""
list_of_nodes=[]
renamed_nodes=['scene', 'inference engine', 'sequential analysis', 'move', 'syntax', 'tourette syndrome', 'fender wide range', 'computer science', 'fact', 'video camera', 'vi', 'knowledge', 'thought', 'applications of artificial intelligence', 'knowledge', 'computer', 'analog-to-digital converter', 'input', 'anwar saifullah khan', 'binary tree', 'subfield', 'repetitive strain injury', 'speech recognition', 'record', 'human intelligence', 'intelligent dance music', 'manufacturing operations', 'capability', 'cloud computing', 'software', 'computer', 'openai', 'method', 'intelligence', 'computer', 'mainframe computer', 'qualitative research', 'george h. w. bush', 'sexual characteristics', 'analog', 'b', 'dan in real life', 'disadvantaged', 'lot', 'decision', 'kizuna ai', 'computer program', 'manipulator', 'computer', 'c', 'ability', 'interaction', 'process', 'difficulty', 'step', 'english', 'domain-specific language', 'yahoo', 'computer', 'tongue', 'artificial intelligence', 'software', 'software development process', 'facility', 'thought', 'logic', 'scene', 'applications of artificial intelligence', 'artificial intelligence', 'corporation', 'for loop', 'secd machine', 'intelligence', 'particular', 'programa', 'user', 'lot', 'false alarm', 'artificial intelligence', "search / searching / searchin'", 'b', 'applications of artificial intelligence', 'adc', 'knowledge base', 'quantitative easing', 'user interface design', 'communications protocol', 'inferno', 'a quiet place: part ii', 'trolley problem', 'pashto', 'idea', 'goal', 'list of programming languages for artificial intelligence', 'knowledge base', 'a', 'english as a second language', 'dec alpha', 'video', 'arm', 'machine', 'field', 'procedure (disambiguation)', 'computer', 'chess', 'programa', 'development', 'image', '@', 'expert system', 'neuro-linguistic programming', 'lisp', 'apple network server', 'computer', 'problem solving', 'robot', 'c++', 'list of programming languages for artificial intelligence', 'position', 'device', 'locations of half-life', 'data', 'class', 'man', 'computer vision', 'artificial intelligence', 'algorithm', 'artificial intelligence', 'artificial intelligence', 'catalytic converter', 'hardware', 'person', 'vision', 'mother!', 'organization', 'order', 'artificial intelligence']
'''
test similarity function
'''
relations={}
def get_nodes():
    openfile=open("nodes.txt","r")
    t=openfile.readlines()
    for x in t:
        #print(x)
        x=x.encode("utf-8")
        x=re.sub(r"/[a-z][a-z][a-z]*","",x)
        x=re.sub(r"/"," ",x)
        x=re.sub(r"\n","",x)
        list_of_nodes.append(x)



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
    #print("new string")
    print("****************************************************************************")
    print("searching for {}".format(new_string))

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
        if i == 'q' or i == '1' or i == '2' or i =='0' or i =='3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            wikidata_id = wikidata_id + i
    res = requests.get(wikidata[0])
    soup = bs(res.text, "html.parser")
    #print(soup)
    node=""
    for hit in soup.findall(attrs={'class' : 'wikibase-title-label'}):
        node= hit.text
    return wikidata_id.encode("utf-8"),node.encode("utf-8")


def result_gen_children(prop,id):
    sparql = sparqlwrapper("https://query.wikidata.org/sparql")
    q="""
    select ?item ?itemlabel
    where
    {
        ?item wdt:p361? wd:q245652 .
        service wikibase:label { bd:serviceparam wikibase:language "en" }
    }
    """
    q=re.sub(r"q245652",id,q)
    #q=re.sub(r"p361",prop,q)

    sparql.setquery(q)

    sparql.setreturnformat(json)
    results = sparql.query().convert()
    return results


def result_gen_parent(prop,id):
    sparql = sparqlwrapper("https://query.wikidata.org/sparql")
    q="""
    select ?item ?itemlabel
    where
    {
        wd:q245652 wdt:p361? ?item   .
        service wikibase:label { bd:serviceparam wikibase:language "en" }
    }
    """
    q=re.sub(r"q245652",id,q)
    sparql.setquery(q)

    sparql.setreturnformat(json)
    results = sparql.query().convert()
    return results


def chilldren(node,id,level):
    if level==levels:
        return

    results = result_gen_children("p361",id)
    results_df = pd.io.json.json_normalize(results['results']['bindings'])

    if node not in graph.keys():
        graph[node]=[]
    if not results_df.empty:
        for x,y in zip(results_df["item.value"] , results_df["itemlabel.value"] ) :
            x=x.encode("utf-8")
            y=y.encode("utf-8")
            print(y)
            x=re.sub(r"http://www.wikidata.org/entity/","",x)
            if y not in graph[node]:
                if y!=node:
                    graph[node].append(y)
            if y not in graph:
                chilldren(y,x,level+1)

def parent(node,id,level):
    if level==levels:
        return

    results = result_gen_parent("p361",id)
    results_df = pd.io.json.json_normalize(results['results']['bindings'])

    if node not in graph.keys():
        graph[node]=[]
    if not results_df.empty:
        for x,y in zip(results_df["item.value"] , results_df["itemlabel.value"] ) :
            x=x.encode("utf-8")
            y=y.encode("utf-8")
            x=re.sub(r"http://www.wikidata.org/entity/","",x)
            print(y)
            if y not in graph:
                graph[y]=[]
                if y!=node:
                    graph[y].append(node)
                parent(y,x,level+1)
            else:
                if y!=node:
                    graph[y].append(node)

def save_list(filename,given_list):
    open(filename, 'w').close()
    fout=open(filename,"w")
    for x in given_list:
        fout.write(x)
        fout.write("\n")


def save_graph(filename):
    open(filename, 'w').close()
    fout=open(filename,"w")
    for x in graph:
        #x=x.encode("utf-8")
        fout.write(x)
        fout.write("\n")
        for y in graph[x]:
            #y=y.encode("utf-8")
            fout.write(y)
            fout.write("\n")
        fout.write("-1\n")
    fout.close()


def load_graph():
    fin=open("gr2.txt","r")
    lines=fin.readlines()
    is_key=true
    for x in lines:
        x=x.strip()
        if is_key:
            key=x
            is_key=false
            graph[key]=[]
        else:
            if(x=="-1"):
                is_key=true
            else:
                graph[key].append(x)

#not tested yet
def reduce_graph():
    flag=true
    while flag:
        print("$")
        to_delete=[]
        flag=false
        for x in graph:
            if x not in list_of_nodes:
                if len(graph[x])==0:
                    to_delete.append(x)
        for x in to_delete:
            graph.pop(x)
            for y in graph:
                if x in graph[y]:
                    graph[y].remove(x)
                    flag=true


def graph_gen():
    load_graph()
    for node in list_of_nodes:
        save_graph("prev_gr2.txt")
        id,node=id_extractor(node)
        if id!="-1":
            renamed_nodes.append(node)
            if node not in graph:
                chilldren(node,id,0)
                parent(node,id,0)
                #print(graph)
                save_graph("gr2.txt")

def label_w(i,H):
    templist = []
    for j in cncpt_ls:
        ##is there a path between i and j
       if nx.has_path(H,i,j):
          templist.append(j)
          print("found match,adding")
    labels[i] = templist
def add_concept(main_concept):
    f = open("cncp.txt","a")
    f.write(main_concept)
    f.write("\n")
    f.close()

    f = open("cncp.txt","r")
    for x in f :
        cncpt_ls.append(x)
        print(x)

'''
get_nodes()
list_of_nodes=list(dict.fromkeys(list_of_nodes))
renamed_nodes=list(dict.fromkeys(renamed_nodes))
load_graph() ## comment out if generating new graph..
##graph_gen() ## comment out if loading previous graph
for x in graph:
    graph[x]=list(dict.f             labels[i] = templistromkeys(graph[x]))
##reduce_graph()## leaf nodes remove

#print("***************")
#print(g)
source = []
target = []
for x in graph:
    for y in graph[x]:
        if x!=y:
            source.append(x)
            target.append(y)

kg_df = pd.dataframe({'source':source, 'target':target})
#print(kg_df)
g=nx.from_pandas_edgelist(kg_df, "source", "target",create_using=nx.digraph())
print(len(G))
##for searching convert into directed Graph
H = G.to_undirected()
## graph made
'''
mn_cncpt = "test"
subject = " "
H.add_edge("mn_cncpt",subject)
##also save grph here

'''main concept '''
add_concept(mn_cncpt)

##after this step cncpt list is updated and mn_cncpt is also added to the list to get the ans
'''Now go to each node and then label it '''
for i in  G.nodes():
    label_w(i,H) ## label and write into the file
    if len(appeared[i]) == 0:
        appeared[i].append(mn_cncpt)

##what concept do you require
concept = " "
for i in labels[concept]:
    print(i)##maybe also print the predecessor of i
for i in appeared[concept]:
    print(i)##maybe also print the predecessor of i

print("done")
