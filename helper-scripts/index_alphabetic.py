from bs4 import BeautifulSoup
import pprint
import yaml 

en_yaml = "./monero-site/_i18n/en.yml"

# Read YAML file
with open(en_yaml, 'r') as stream:
    data_loaded = yaml.safe_load(stream)

with open("testing.md", "r") as f:
	soup = BeautifulSoup(f, "html.parser")

divs = soup.find_all("div", {"class": "col"})
data = {}
for div in divs:
	category = str(div.find("h2"))
	category = category.split(".")[1].split(" ")[0]
	data[category] = []
	p = div.find_all("p")
	for lol in p:
		#link = lol.find_all("a",href=True)[0]
		#print(link['href'])
		title_key = lol.text.split(".")[1].split(" ")[0]
		title_yaml = data_loaded["user-guides"][title_key]
		info = { 
					"title_key": title_key,
					"title_yaml": title_yaml,
					"raw_data": lol
				}
		data[category].append(info)
		
for category in data:
	alphabetic = sorted(data[category], key=lambda d: d['title_yaml']) 
	data[category] = alphabetic

pprint.pprint(data)
pprint.pprint(data)
