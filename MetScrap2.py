import json
with open ('Metdata.json') as data_file:
	data = json.load(data_file)



for x in data ['results']:

	if x["regularImage"].endswith (".png"):
		continue
		 
	print(x["regularImage"])
	print(x["title"])
	print(x["date"])
	print(x["medium"])



