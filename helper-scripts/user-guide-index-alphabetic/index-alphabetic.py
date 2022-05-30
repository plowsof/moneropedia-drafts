from bs4 import BeautifulSoup
import yaml 
import pprint
import sys
import subprocess

en_yaml = "./monero-site/_i18n/en.yml"
index = "./monero-site/resources/user-guides/index.md"
'''
Category:
general
mining
backup
nodesync
recovery
wallets
hardwarewallet
anonimizationnetworks

'''
template = """---
layout: custom
title: titles.userguides
---
{% t global.lang_tag %}
<div class="guides">
    <section class="container">
        <div class="row">
            <div class="left half no-pad-sm col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="info-block">
                    <div class="row">
                        <div class="col">
                            <h2>{% t user-guides.general %}</h2>
                            !_! general !_!
                        </div>
                    </div>
                </div>
            </div>
            <div class="right half col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="info-block">
                    <div class="row">
                        <div class="col">
                            <h2>{% t user-guides.mining %}</h2>
                            !_! mining !_!
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="container">
        <div class="row">
            <div class="left half no-pad-sm col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="info-block">
                    <div class="row">
                        <div class="col">
                            <h2>{% t user-guides.backup %}</h2>
                            !_! backup !_!
                        </div>
                    </div>
                </div>
            </div>
            <div class="right half col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="info-block">
                    <div class="row">
                        <div class="col">
                            <h2>{% t user-guides.nodesync %}</h2>
                            !_! nodesync !_!
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>    
    <section class="container">
        <div class="row">
            <div class="left half no-pad-sm col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="info-block">
                    <div class="row">
                        <div class="col">
                            <h2>{% t user-guides.recovery %}</h2>
                            !_! recovery !_!
                        </div>
                    </div>
                </div>
            </div>
            <div class="right half col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="info-block">
                    <div class="row">
                        <div class="col">
                            <h2>{% t user-guides.wallets %}</h2>
                            !_! wallets !_!
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="container">
        <div class="row">
            <div class="left half no-pad-sm col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="info-block">
                    <div class="row">
                        <div class="col">
                            <h2>{% t user-guides.hardwarewallet %}</h2>
                            !_! hardwarewallet !_!
                        </div>
                    </div>
                </div>
            </div>
            <div class="right half col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <div class="info-block">
                    <div class="row">
                        <div class="col">
                            <h2>{% t user-guides.anonimizationnetworks %}</h2>
                            !_! anonimizationnetworks !_!
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</div>
"""
with open(en_yaml, 'r') as stream:
    data_loaded = yaml.safe_load(stream)

#with open("./monero-site/resources/user-guides/index.md", "r") as f:
#    soup = BeautifulSoup(f, "html.parser")

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

if fine == 0:
    with open("is_alphabetic.md", "w+") as f:
        for line in template.splitlines():
            if "!_!" not in line:
                f.write(line + "\n")
            else:
                category = line.split("!_!")[1].strip()
                for thing in data[category]:
                    raw_data = thing["raw_data"]
                    indent = ""
                    for i in range(28):
                        indent += " "

                    f.write(f"{indent}{thing['raw_data']}\n")

    termbin_url = subprocess.check_output(["cat is_alphabetic.md | nc termbin.com 9999"],shell=True).decode("utf-8")
    print(f"Ordered version at: {termbin_url}")
    sys.exit(1)
