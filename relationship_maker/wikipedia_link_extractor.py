from bs4 import BeautifulSoup as bs
import requests
import wikipedia

search_string = "Ensemble Learning"
#print(type(wikipedia.search(search_string)))
print("Searching for .........")
query = wikipedia.search(search_string)[0]
#print(query)
new_string = ""
for i in query:
 if i == " ":
  new_string = new_string + '_'
 else:
  new_string = new_string + i
#print("New string")
print(new_string)

res = requests.get("https://en.wikipedia.org/wiki/"+new_string)
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

