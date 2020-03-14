import nltk
import re
from nltk.tokenize import PunktSentenceTokenizer
pst = PunktSentenceTokenizer()
openfile = open("data.txt")
data = openfile.read()
tokenized_sentence = pst.tokenize(data)
for i in tokenized_sentence:
  try:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    chunkGram = r"""Chunk: {<JJ.?>*<NN.?>}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    print(chunked)
    chunked.draw()
  except Exception as e:
      print(str(e))
