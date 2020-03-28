from bs4 import BeautifulSoup as bs
import requests

res = requests.get("https://en.wikipedia.org/wiki/Ensemble_learning")
soup = bs(res.text, "html.parser")
wikidata = []
for link in soup.find_all("a"):
    url = link.get("href", "")
    if "//www.wikidata.org/" in url:
        wikidata.append(url)

#print(type(wikidata[0]))
count = 0
wikidata_id  = ""
for i in wikidata[0]:
 if i == '/':
  count = count + 1
 if count==5 and i != '/':
  wikidata_id = wikidata_id + i

print(wikidata_id)

