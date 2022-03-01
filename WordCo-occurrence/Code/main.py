import requests, json

url = "http://dblp.dagstuhl.de/search/publ/api?q=retrieval&h=1000&format=json"
data = requests.get(url)
print(data.content)
open('temp2.json', 'w').write(data.content)
data = json.dumps(data.json())

#print(type(data))