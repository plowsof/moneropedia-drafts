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
data_a = {}
yaml_data = {}

category = "advanced"
key = "plowsofs-faq-script"
q = "How do i make a script to make adding a FAQ easier?"
a = []
a.append("What a coincidence, im actually making a script to answer this question right now. One moment, let me just start a new paragraph.")
a.append("Thats better, i was starting to feel cramped. Basically, take a look at plowsofs script, you just need your question / key and , hold on, feeling cramped again.")
a.append("Sadly the script does not support adding 'additional' links at the bottom, (but its good enough right? im sure you can figure them out and paste a line into the html 8-) )")

def add_new_faq(key,q,a,category):
    global data_a,data_q,en_yaml,yaml_data
    anchor = f"anchor--{key}"
    q_key = f"q{key}"
    a_key = f"a{key}"
    if yaml_data.get(q_key) or yaml_data.get(a_key):
        print(f"Key in use, choose another: {key}")
        sys.exit(1)
    a_paragraphs = {}
    for i in range(len(a)):
        a_paragraphs[f"a{key}_{i}"] = {
            "raw_html": f"<p>{{% t faq.a{key}_{i} %}}</p>",
            "text": a[i],
            "key": key
        }

    # add a/q to yaml file
    with open(en_yaml,"r") as f:
        lines = f.readlines()
    at_faq = 0
    done = 0
    with open("faq_new_yaml.yml","w+") as f:
        for line in lines:
            if line == "faq:\n":
                at_faq = 1
            if line == "\n" and at_faq == 1:
                f.write(f"  {q_key}: {q}\n")
                for x in a_paragraphs:
                    f.write(f"  {x}: {a_paragraphs[x]['text']}\n")
                at_faq = 0
            f.write(line)
    # add to data_q
    list_item = f'<li><a href="#anchor--{key}">{{% t faq.q{key} %}}</a></li>'
    info = {
    "question": q,
    "key": key,
    "answer": [],
    "anchor": anchor,
    "raw_html": list_item
    }
    data_q[category].append(info)
    # add to data_a
    raw_html = ""
    raw_html += f'<div class="tab" id="anchor--{key}">\n'
    raw_html += f'<h3><a class="anchor" href="#anchor--{key}"></a>{{% t faq.q{key} %}}</h3>\n'
    raw_html += f'<div class="tab-answer">\n'
    for x in a_paragraphs:
        raw_html += f'<p>{{% t faq.{x} %}}</p>\n'
    raw_html += "</div>\n</div>"
    data_a[anchor] = raw_html

    # order list
    for category in data_q:
        alphabetic = sorted(data_q[category], key=lambda d: d['question']) 
        data_q[category] = alphabetic

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

def build_lists():
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

def create_index():    
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
        f.write("\n")

build_lists()
add_new_faq(key,q,a,category)
create_index()
