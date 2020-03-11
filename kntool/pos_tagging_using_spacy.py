import spacy

nlp = spacy.load('en_core_web_sm')
string = "The 22-year-old recently won ATP Challenger tournament."
unicode_string = unicode(string,"utf-8")
doc = nlp(unicode_string)

for tok in doc:
  print(tok.text, "...", tok.pos_)
