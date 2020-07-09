import spacy
from spacy import displacy
nlp = spacy.load('en')
doc = nlp(u'machine learning algorithms build a mathematical model based on sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to do so.')
for tok in doc:
    print(tok.text,".....",tok.dep_)