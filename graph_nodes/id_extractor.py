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
        print(url)
#print(type(wikidata[0]))

count = 0
wikidata_id  = ""
for i in wikidata[0]:
 if i == 'Q' or i == '1' or i == '2' or i =='0' or i =='3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
  wikidata_id = wikidata_id + i
  

print(wikidata_id)