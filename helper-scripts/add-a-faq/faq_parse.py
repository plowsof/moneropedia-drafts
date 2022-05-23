from bs4 import BeautifulSoup
import yaml 
import shutil
import re
import pprint 
import requests
from urllib.parse import urlparse
import os
import sys
en_yaml = "./monero-site/_i18n/en.yml"

data_q = {}
yaml_data = {}
def parse_html(list_item,category):
    global data,yaml_data_q
    #print(list_item)
    anchor = list_item.find('a', href=True)['href'].split("#")[1]
    #print(anchor)
    #print(category)
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

def add_faq_to_index(new_key,new_text,category):
    global en_yaml,yaml_data,data_q,data_a
    data_q["general"] = []
    data_q["advanced"] = []
    data_q["nodeandwallet"] = []
    with open("faq_index.md", "r") as f:
        soup = BeautifulSoup(f, "html.parser")
    div = soup.find("ul")
    with open(en_yaml, 'r') as f:
        yaml_data = yaml.safe_load(f)
    toc = div.find_all("ul")
    for x in toc[0].find_all("li"):
        parse_html(x,"general")
    for x in toc[1].find_all("li"):
        parse_html(x,"advanced")
    for x in toc[2].find_all("li"):
        parse_html(x,"nodeandwallet")
    test = soup.find_all("div", {"class": "row faq"})[1]
    answers = test.find_all("div", {"class":"tab"})
    number = 0
    data_a = {}
    for a in answers:
        if number < len(data_q["general"]):
            category = "general"
        elif number < (len(data_q["general"]) + len(data_q["advanced"])):
            category = "advanced"
        else:
            category = "nodeandwallet"
        anchor = a["id"]
        raw_html = a
        data_a[anchor] = raw_html
        number += 1

    for category in data_q:
        alphabetic = sorted(data_q[category], key=lambda d: d['question']) 
        data_q[category] = alphabetic

in_16 = ""
in_20 = ""
in_24 = ""
in_28 = ""
for i in range(16):
    in_16 += " "
for i in range(20):
    in_20 += " "
for i in range(24):
    in_24 += " "
for i in range(28):
    in_28 += " "

add_faq_to_index("","","")

            

with open("template_faq_index.md", "r") as f:
    template_lines = f.readlines()

do_toc_thing = 0
do_other_thing = 0
div_open = 0
with open("new_faq.md","w+") as f:
    for line in template_lines:
        if "!_! toc_general !_!" in line:
            do_toc_thing = 1
            category = "general"
        elif "!_! toc_advanced !_!" in line:
            do_toc_thing = 1
            category = "advanced"
        elif "!_! toc_nodeandwallet !_!" in line:
            do_toc_thing = 1
            category = "nodeandwallet"
        elif "!_! general !_!" in line:
            do_other_thing = 1
            category = "general"
        elif "!_! advanced !_!" in line:
            do_other_thing = 1
            category = "advanced"
        elif "!_! nodeandwallet !_!" in line:
            do_other_thing = 1
            category = "nodeandwallet"
        else:
            f.write(f"{line}")

        if do_toc_thing == 1:
            for thing in data_q[category]:
                this = thing["raw_html"]
                f.write(f"{in_24}{this}\n")
            do_toc_thing = 0
        elif do_other_thing == 1:
            for x in data_q[category]:
                for l in str(data_a[x["anchor"]]).splitlines():
                    indent = ""
                    if '<div' in l:
                        if div_open == 0:
                            indent = in_16
                        else:
                            indent = in_20
                        div_open += 1
                    if "</div>" in l:
                        if div_open == 1:
                            indent = in_16
                        else:
                            indent = in_20
                        div_open -= 1
                    if "<h3" in l:
                        indent = in_20
                    if "<p>" in l or "ol>" in l:
                        indent = in_24
                    if "<li>" in l:
                        indent = in_28
                    l = str(indent) + l
                    f.write(f"{l}\n")
            do_other_thing = 0
                    