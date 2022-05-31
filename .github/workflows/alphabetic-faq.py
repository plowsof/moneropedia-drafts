from bs4 import BeautifulSoup
import yaml 
import sys
en_yaml = "_i18n/en.yml"
faq_index = "get-started/faq/index.md"
data_q = {}
yaml_data = {}

def parse_html(list_item,category):
    global data,yaml_data_q
    anchor = list_item.find('a', href=True)['href'].split("#")[1]
    key = list_item.text.split("faq.")[1].split(" %}")[0]
    question = yaml_data["faq"][key]
    info = {
    "question": question,
    "key": key,
    "answer": [],
    "anchor": anchor,
    "raw_html": list_item
    }
    data_q[category].append(info)


data_q["general"] = []
data_q["advanced"] = []
data_q["nodeandwallet"] = []

with open(faq_index, "r") as f:
    soup = BeautifulSoup(f, "html.parser")
with open(en_yaml, 'r') as f:
    yaml_data = yaml.safe_load(f)
div = soup.find("ul")
toc = div.find_all("ul")
for x in toc[0].find_all("li"):
    parse_html(x,"general")
for x in toc[1].find_all("li"):
    parse_html(x,"advanced")
for x in toc[2].find_all("li"):
    parse_html(x,"nodeandwallet")

fine = 1
for category in data_q:
    original = data_q[category]
    alphabetic = sorted(data_q[category], key=lambda d: d['question']) 
    if original == alphabetic:
        print(f"--> Category: {category} [ OK ]")
    else:
        print(f"--> Category: {category} [ FAIL ]")
        fine = 0
if fine == 0:
    sys.exit(1)
