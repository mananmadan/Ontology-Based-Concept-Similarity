import nltk
import spacy
import re
import pandas as pd
import bs4
import requests
from spacy import displacy
from nltk.tokenize import sent_tokenize
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import Matcher
from spacy.tokens import Span
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
def get_relation(sent):

  doc = nlp(sent)

  # Matcher class object
  matcher = Matcher(nlp.vocab)

  #define the pattern
  pattern = [{'DEP':'ROOT'},
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},
            {'POS':'ADJ','OP':"?"}]

  matcher.add("matching_1", None, pattern)

  matches = matcher(doc)
  k = len(matches) - 1

  span = doc[matches[k][1]:matches[k][2]]

  return(span.text)

def get_entities(sent):
  ## chunk 1
  ent1 = ""
  ent2 = ""

  prv_tok_dep = ""    # dependency tag of previous token in the sentence
  prv_tok_text = ""   # previous token in the sentence

  prefix = ""
  modifier = ""

  #############################################################

  for tok in nlp(sent):
    ## chunk 2
    # if token is a punctuation mark then move on to the next token
    if tok.dep_ != "punct":
      # check: token is a compound word or not
      if tok.dep_ == "compound":
        prefix = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "compound":
          prefix = prv_tok_text + " "+ tok.text

      # check: token is a modifier or not
      if tok.dep_.endswith("mod") == True:
        modifier = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "compound":
          modifier = prv_tok_text + " "+ tok.text

      ## chunk 3
      if tok.dep_.find("subj") == True:
        ent1 = modifier +" "+ prefix + " "+ tok.text
        prefix = ""
        modifier = ""
        prv_tok_dep = ""
        prv_tok_text = ""

      ## chunk 4
      if tok.dep_.find("obj") == True:
        ent2 = modifier +" "+ prefix +" "+ tok.text

      ## chunk 5
      # update variables
      prv_tok_dep = tok.dep_
      prv_tok_text = tok.text
  #############################################################

  return [ent1.strip(), ent2.strip()]
data_string = ""
opentext = open("data.txt")
readtext = opentext.read()
sentences = sent_tokenize(readtext)
count = 0
entities = []
relations = []
for i in sentences:
 print(count)
 count= count+1
 print(i)
 string = i
 unicode_string = unicode(string,"utf-8")
 doc = nlp(unicode_string)
 #print("data")
 print(get_entities(unicode_string))
 entities.append(get_entities(unicode_string))
 print(get_relation(unicode_string))
 relations.append(get_relation(unicode_string))
#for denpendency structure #for tok in doc:
#  print(tok.text, "...", tok.dep_)
print("printing list------")
print(entities)
print(relations)
source = [i[0] for i in entities]
target = [i[1] for i in entities]
print(source)
print(target)
kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})
print("printing pandas data frame--------")
print(kg_df)
G=nx.from_pandas_edgelist(kg_df, "source", "target",edge_attr=True, create_using=nx.MultiDiGraph())
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.show()
