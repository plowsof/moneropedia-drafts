from bs4 import BeautifulSoup
import yaml 
import sys

en_yaml = "_i18n/en.yml"
index = "resources/user-guides/index.md"

with open(en_yaml, 'r') as stream:
    data_loaded = yaml.safe_load(stream)
with open(index, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

divs = soup.find_all("div", {"class": "col"})
data = {}
for div in divs:
    category = str(div.find("h2"))
    category = category.split(".")[1].split(" ")[0]
    data[category] = []
    p = div.find_all("p")
    for lol in p:
        title_key = lol.text.split(".")[1].split(" ")[0]
        title_yaml = data_loaded["user-guides"][title_key]
        info = { 
                    "title_key": title_key,
                    "title_yaml": title_yaml,
                    "raw_data": lol
                }
        data[category].append(info)
try:
    for category in data:
        original = data[category]
        alphabetic = sorted(data[category], key=lambda d: d['title_yaml']) 
        data[category] = alphabetic
        fine = 1
        if original == alphabetic:
            print(f"--> Category: {category} [ OK ]")
        else:
            print(f"--> Category: {category} [ FAIL ]")
            fine = 0
except:
    print("huh?")

if fine == 0:
    sys.exit(1)
