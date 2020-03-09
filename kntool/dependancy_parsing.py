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
text = "Tableu was aquired by salesforce"
unicode_text = unicode(text,"utf-8")
doc = nlp(unicode_text)
displacy.serve(doc, style='dep')
