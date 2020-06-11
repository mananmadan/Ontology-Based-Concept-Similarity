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
Graph={}
levels=3
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
        x=re.sub(r"/[A-Z][A-Z][A-Z]*","",x)
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
        ?item wdt:P361? wd:Q245652 .
        SERVICE wikibase:label { bd:SERVICEparam wikibase:language "en" }
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
        wd:Q245652 wdt:P361? ?item   .
        SERVICE wikibase:label { bd:SERVICEparam wikibase:language "en" }
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
            print(y)
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

    if node not in Graph.keys():
        Graph[node]=[]
    if not results_df.empty:
        for x,y in zip(results_df["item.value"] , results_df["itemLabel.value"] ) :
            x=x.encode("utf-8")
            y=y.encode("utf-8")
            x=re.sub(r"http://www.wikidata.org/entity/","",x)
            print(y)
            if y not in Graph:
                Graph[y]=[]
                if y!=node:
                    Graph[y].append(node)
                parent(y,x,level+1)
            else:
                if y!=node:
                    Graph[y].append(node)

def save_list(filename,given_list):
    open(filename, 'w').close()
    fout=open(filename,"w")
    for x in given_list:
        fout.write(x)
        fout.write("\n")


def save_Graph(filename):
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


def load_Graph():
    fin=open("gr2.txt","r")
    lines=fin.readlines()
    is_key=true
    for x in lines:
        x=x.strip()
        if is_key:
            key=x
            is_key=false
            Graph[key]=[]
        else:
            if(x=="-1"):
                is_key=true
            else:
                Graph[key].append(x)

#not tested yet
def reduce_Graph():
    flag=true
    while flag:
        print("$")
        to_delete=[]
        flag=false
        for x in Graph:
            if x not in list_of_nodes:
                if len(Graph[x])==0:
                    to_delete.append(x)
        for x in to_delete:
            Graph.pop(x)
            for y in Graph:
                if x in Graph[y]:
                    Graph[y].remove(x)
                    flag=true


def Graph_gen():
    load_Graph()
    for node in list_of_nodes:
        save_Graph("prev_gr2.txt")
        id,node=id_extractor(node)
        if id!="-1":
            renamed_nodes.append(node)
            if node not in Graph:
                chilldren(node,id,0)
                parent(node,id,0)
                #print(Graph)
                save_Graph("gr2.txt")

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
    

get_nodes()
list_of_nodes=list(dict.fromkeys(list_of_nodes))
renamed_nodes=list(dict.fromkeys(renamed_nodes))
load_Graph() ## comment out if generating new Graph..
##Graph_gen() ## comment out if loading previous Graph
for x in Graph:
    Graph[x]=list(dict.labels[i] = templistromkeys(Graph[x]))
##reduce_Graph()## leaf nodes remove

#print("***************")
#print(g)
source = []
target = []
for x in Graph:
    for y in Graph[x]:
        if x!=y:
            source.append(x)
            target.append(y)

kg_df = pd.dataframe({'source':source, 'target':target})
#print(kg_df)
g=nx.from_pandas_edgelist(kg_df, "source", "target",create_using=nx.diGraph())
print(len(G))
##for searching convert into directed Graph
H = G.to_undirected()
## Graph made

mn_cncpt = "Artificial Intelligence"
subject = "Computer Science"
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
