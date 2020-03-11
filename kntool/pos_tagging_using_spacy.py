import spacy

nlp = spacy.load('en_core_web_sm')
string = "Burning of fossil fuels, agriculture related activities, mining operations, exhaust from industries and factories, and household cleaning products entail air pollution."
unicode_string = unicode(string,"utf-8")
doc = nlp(unicode_string)

for tok in doc:
  print(tok.text, "...", tok.pos_)
