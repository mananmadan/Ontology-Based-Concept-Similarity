import stanfordcorenlp
from collections import defaultdict
from stanfordcorenlp import StanfordCoreNLP
import logging
import json


class StanfordNLP:
    def __init__(self, host='./', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000) #  , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))
    def __del__(self):
        self.nlp.close()

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

if __name__ == '__main__':
    sNLP = StanfordNLP()
    text = 'Coronaviruses are a group of related viruses that cause diseases in mammals and birds. In humans, coronaviruses cause respiratory tract infections that are typically mild, such as some cases of the common cold (among other possible causes, predominantly rhinoviruses), though rarer forms can be lethal, such as SARS, MERS, and COVID-19. Symptoms vary in other species: in chickens, they cause an upper respiratory tract disease, while in cows and pigs they cause diarrhea. There are yet to be vaccines or antiviral drugs to prevent or treat human coronavirus infections.😂'
   # print ("Annotate:", sNLP.annotate(text))
    print("\n\n\n")
    print ("POS:", sNLP.pos(text))
    print("\n\n\n")
    print ("Tokens:", sNLP.word_tokenize(text))
    print("\n\n\n")
    print ("NER:", sNLP.ner(text))
    print("\n\n\n")
    print ("Parse:", sNLP.parse(text))
    print("\n\n\n")
    print ("Dep Parse:", sNLP.dependency_parse(text))
