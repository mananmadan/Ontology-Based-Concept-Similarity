#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:41:30 2020

@author: manan
"""
from SPARQLWrapper import SPARQLWrapper,JSON
import pandas as pd

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setQuery("""
SELECT ?item ?itemLabel
WHERE
{
    ?item wdt:P69 wd:Q160302 .
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
""")

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

results_df = pd.io.json.json_normalize(results['results']['bindings'])
print(results_df)
#print(results_df[['item.value', 'itemLabel.value']].head())
