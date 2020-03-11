import nltk
from nltk.tokenize import word_tokenize
data = "Burning of fossil fuels, agriculture related activities, mining operations, exhaust from industries and factories, and household cleaning products entail air pollution"
words = word_tokenize(data)
print(words)
pos_tagged = nltk.pos_tag(words)
print(pos_tagged)
