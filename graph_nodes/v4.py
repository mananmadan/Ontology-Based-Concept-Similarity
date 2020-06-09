from SPARQLWrapper import SPARQLWrapper,JSON
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import pickle
import requests
import wikipedia
import plotly
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt
from numpy import array

Graph={}
levels=3
#limit=""
list_of_nodes=[]
renamed_nodes=['Scene', 'inference engine', 'Sequential analysis', 'MOVE', 'syntax', 'Tourette syndrome', 'Fender Wide Range', 'computer science', 'fact', 'video camera', 'vi', 'knowledge', 'thought', 'Applications of artificial intelligence', 'knowledge', 'computer', 'analog-to-digital converter', 'Input', 'Anwar Saifullah Khan', 'binary tree', 'Subfield', 'repetitive strain injury', 'speech recognition', 'Record', 'human intelligence', 'intelligent dance music', 'Manufacturing operations', 'Capability', 'cloud computing', 'software', 'computer', 'OpenAI', 'Method', 'intelligence', 'computer', 'mainframe computer', 'qualitative research', 'George H. W. Bush', 'sexual characteristics', 'Analog', 'B', 'Dan in Real Life', 'Disadvantaged', 'Lot', 'Decision', 'Kizuna AI', 'computer program', 'manipulator', 'computer', 'C', 'Ability', 'interaction', 'Process', 'Difficulty', 'Step', 'English', 'domain-specific language', 'Yahoo', 'computer', 'tongue', 'artificial intelligence', 'software', 'software development process', 'facility', 'thought', 'logic', 'Scene', 'Applications of artificial intelligence', 'artificial intelligence', 'corporation', 'for loop', 'SECD machine', 'intelligence', 'Particular', 'Programa', 'User', 'Lot', 'false alarm', 'artificial intelligence', "Search / Searching / Searchin'", 'B', 'Applications of artificial intelligence', 'ADC', 'knowledge base', 'quantitative easing', 'user interface design', 'communications protocol', 'Inferno', 'A Quiet Place: Part II', 'Trolley problem', 'Pashto', 'idea', 'goal', 'list of programming languages for artificial intelligence', 'knowledge base', 'A', 'English as a second language', 'DEC Alpha', 'video', 'arm', 'machine', 'Field', 'Procedure (disambiguation)', 'computer', 'chess', 'Programa', 'Development', 'image', '@', 'expert system', 'neuro-linguistic programming', 'Lisp', 'Apple Network Server', 'computer', 'problem solving', 'robot', 'C++', 'list of programming languages for artificial intelligence', 'Position', 'Device', 'Locations of Half-Life', 'data', 'Class', 'man', 'computer vision', 'artificial intelligence', 'algorithm', 'artificial intelligence', 'artificial intelligence', 'catalytic converter', 'hardware', 'person', 'Vision', 'mother!', 'organization', 'Order', 'artificial intelligence']
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
        ?item wdt:P361? wd:Q245652 .
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
        wd:Q245652 wdt:P361? ?item   .
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
    fin=open("graph1.txt","r")
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
        save_graph("prev_graph1.txt")
        id,node=id_extractor(node)
        if id!="-1":
            renamed_nodes.append(node)
            if node not in Graph:
                chilldren(node,id,0)
                parent(node,id,0)
                #print(Graph)
                save_graph("graph1.txt")


get_nodes()
list_of_nodes=list(dict.fromkeys(list_of_nodes))
renamed_nodes=list(dict.fromkeys(renamed_nodes))
load_graph() ## comment out if generating new graph..
##Graph_gen() ## comment out if loading previous graph
for x in Graph:
    Graph[x]=list(dict.fromkeys(Graph[x]))
##reduce_graph()## leaf nodes remove

print("***************")
#print(G)
source = []
target = []
for x in Graph:
    for y in Graph[x]:
        if x!=y:
            source.append(x)
            target.append(y)

kg_df = pd.DataFrame({'source':source, 'target':target})
# save_list("graphSource",source)
# save_list("graphTarget",target)
#print(kg_df)
G=nx.from_pandas_edgelist(kg_df, "source", "target",create_using=nx.DiGraph())
print(len(G))
##for searching convert into directed graph
H = G.to_undirected()
## Trying to analyze clustering 
print("clustering",nx.clustering(G))
'''
u = "organism"
v = "cell"
path=nx.shortest_path(H,u,v)
print("The path between "+u+" "+"and"+" "+v+" "+"===>",path)

print("Neighbours",H.neighbors("biology"))
'''

'''
m = "metabolism"
n = "cell"
path2=nx.shortest_path(H,m,n)
print("The path between "+m+" "+"and"+" "+n+" "+"===>",path2)
'''
'''
F = nx.Graph()
#E = F.to_undirected()
key = "load cell"
for neb in H.neighbors(key):
   F.add_edge(key,neb)
   for i in H.neighbors(neb):
    F.add_edge(i,neb)
'''


##path2=nx.shortest_path(H,"computer engineering","digital electronics")
##path3=nx.shortest_path(H,"electrical engineering","digital electronics")
##print("path3",path3)
##print("path2",path2)
#F.add_edges_from([(path[v],path[v+1]) for v in range(len(path)-1)])
#F.add_edges_from([(path2[v],path2[v+1]) for v in range(len(path2)-1)])
#F.add_edges_from([(path3[v],path3[v+1]) for v in range(len(path3)-1)])
#print(F.edges())
#print(F.nodes())


'''
below is the code for drawing the graph of the neighbours of a particular nodes
'''
'''
labels = {}
for idx, node in enumerate(F.nodes()):
      labels[node] = node
#plt.figure()
pos = nx.spring_layout(F, k=0.5, iterations=50)
##pos = nx.fruchterman_reingold_layout(F)
print(type(pos))
#for n, p in pos.items():
#    F.node[n]['pos'] = p
#pos=nx.spring_layout(F)

nx.draw_networkx(F,pos,labels)
plt.axis('off')
plt.show()
'''

'''
Analysis on the graph
'''
'''
## H is the undirected version of the whole graph G

## Finding number of compnonents in the undirected graph
print("Number of connected components in the graph is:::" ,  nx.number_connected_components(H))
print("connected components are :: ",list(nx.connected_components(H)))
l = list(nx.connected_components(H))
for i in range(0,85):
 print("List ",i," :",len(l[i]))
 if len(l[i]) > 10:
      if len(l[i]) < 70:
          print(l[i])
'''

'''
Testing similarity
'''
#print(simrank_similarity_numpy(H,"computer science","electronic circuit"))
#print((nx.flow_hierarchy(G)))

'''
### plotly
edge_x = []
edge_y = []
for edge in F.edges():
    x0, y0 = F.nodes[edge[0]]['pos']
    x1, y1 = F.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in F.nodes():
    x, y = F.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
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

## color node points
node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(F.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_adjacencies
node_trace.text = node_text

## plot the graph
fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>F graphs',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()
'''
## after this the aim was to make the graph shorter ##
'''
edges=[]
main_nodes=[]
relation_nodes=[]
for x in renamed_nodes:
    for y in renamed_nodes:
        if x!=y:
            if x in G and y in G:
                path=[]
                try:
                    path=nx.shortest_path(G,x,y)
                except:
                    t=[]
                if len(path)>0 :
                    temp_str=""
                    relation_edge=[]
                    flag =True
                    for element in path:
                        if flag:
                            temp_str+=element+" -> "
                            relation_edge.append(element)
                        if flag and element!=x and element!= y and element in renamed_nodes:
                            flag=False
                            print("$$$$$$$$$$$$$$$$$$$$$$$4")
                            y=element

                    print ("relation between {} and {} is: {}".format(x,y,temp_str))
                    i =0
                    main_nodes.append(x)
                    main_nodes.append(y)
                    while i+1< len(relation_edge):
                        if(i!=0):
                            relation_nodes.append(relation_edge[i])
                        edge=[]
                        edge.append(relation_edge[i])
                        edge.append(relation_edge[i+1])
                        edges.append(edge)
                        i=i+1
                    # edge=[]
                    # edge.append(x)
                    # edge.append(y)
                    # edges.append(edge)
                    # edge_labels[(x,y)]=temp_str

print(edges)
open("sources.txt", 'w').close()
fout=open("sources.txt","w")
for x in source:
     fout.write(x)
     fout.write("\n")
templist=[]
templist.extend(source)
templist.extend(target)
open("target.txt", 'w').close()
fout=open("target.txt","w")
for x in target:
     fout.write(x)
     fout.write("\n")

templist=list(dict.fromkeys(templist))
open("allnodes.txt", 'w').close()
fout=open("allnodes.txt","w")
for x in target:
     fout.write(x)
     fout.write("\n")

main_nodes=list(dict.fromkeys(main_nodes))
relation_nodes=list(dict.fromkeys(relation_nodes))
color_map=[]

G=nx.DiGraph()
G.add_edges_from(edges)
# G=nx.read_edgelist("edgelist",create_using=nx.DiGraph)
#nx.write_edgelist(G, "edgelist.txt")


# print("---------------------------------------------------------------------------------------------")
# print dg.edges()
#with open("edgelist.txt","wb") as f:
    #pickle.dump(G, f)

dg=nx.DiGraph()
#with open("/home/aditya/Improvising-wordnet/improviser/edgelist.txt","rb") as f:
    #dg = pickle.load(f)
#print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#print(dg.nodes())

#######################################################
for x in G.nodes():
    if x in main_nodes:
        color_map.append("yellow")
    else:
        color_map.append("pink")
pos = nx.spring_layout(G)
for x in G.nodes():
   val=nx.predecessor(G,x)
   for child in val:
       if len(val[child])>0:
           print([child,"---->",val[child][0] ])
           print("\n")
    #print("****************************")
#pos = nx.spring_layout(G,k=0.25,iterations=10)
plt.figure()
nx.draw_networkx(G,pos,edge_color='black',width=1,linewidths=1,node_color=color_map)
# nx.draw(G,pos,edge_color='black',width=1,linewidths=1,\
# node_size=500,node_color=nx.get_node_attributes(G,'val'),alpha=0.9,\
# labels={node:node for node in G.nodes()})
plt.axis('off')
plt.show()




# max=0
# root=[]
# for x in G:
#     if G.degree(x)> max:
#         max=G.degree(x)
#         root=[]
#         root.append(x)
#     el  if G.degree(x)== max:
#         root.append(x)
# print(max,root)
'''
print("Done ... ")
