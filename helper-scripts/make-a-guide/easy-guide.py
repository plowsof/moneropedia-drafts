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
guide_category = "anonimizationnetworks"
title_text = "This is a new guidelol"
title_key = "some-new-guides"
markdown_url = "https://raw.githubusercontent.com/plowsof/userguide-drafts/main/i2p/monero-gui-i2p-node.md"


def add_title_to_yaml(title_key,title_text):
    # sort the yaml file out
    global en_yaml
    yaml_contents = check_yaml(title_key)
    if yaml_contents:
        wait_for_end = 0
        with open("new_yaml.yml", "w+") as f:
            for line in yaml_contents:
                if line == "user-guides:\n":
                    wait_for_end = 1
                if wait_for_end == 1:
                    if line == "\n":
                        f.write(f"  {title_key}: {title_text}\n")
                        wait_for_end = 0
                f.write(line)
        shutil.move("new_yaml.yml",en_yaml)
    else:
        print(f"[ title key is in use ] {title_key}")
        sys.exit()

# sort the index file out
def add_title_to_index(new_key,new_text,guide_category):
    global en_yaml
    with open("./monero-site/resources/user-guides/index.md", "r") as f:
        soup = BeautifulSoup(f, "html.parser")
    with open(en_yaml, 'r') as f:
        data_loaded = yaml.safe_load(f)
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
    # add our new entry before sorting
    raw_html = f'<p><a href="{{{{site.baseurl}}}}/resources/user-guides/{new_key}.html">{{% t user-guides.{new_key} %}}</a></p>'
    info = {
            "title_key": new_key,
            "title_yaml": new_text,
            "raw_data": raw_html
    }
    data[guide_category].append(info)
    for category in data:
        alphabetic = sorted(data[category], key=lambda d: d['title_yaml']) 
        data[category] = alphabetic

    with open("index_template.md", "r") as f:
        lines = f.readlines()

    with open("new_index.md", "w+") as f:
        for line in lines:
            if "!_!" not in line:
                f.write(line)
            else:
                category = line.split("!_!")[1].strip()
                for thing in data[category]:
                    raw_data = thing["raw_data"]
                    indent = ""
                    for i in range(28):
                        indent += " "

                    f.write(f"{indent}{thing['raw_data']}\n")
    shutil.move("new_index.md","./monero-site/resources/user-guides/index.md")
# check that the key has not been used
def check_yaml(title_key):
    global en_yaml
    with open(en_yaml, 'r') as f:
        data_loaded = yaml.safe_load(f)
    if not data_loaded["user-guides"].get(title_key):
        with open(en_yaml, 'r') as f:
            lines = f.readlines()
        return lines

def handle_markdown_file(furl,title_key,title_text):
    r = requests.get(furl)
    with open("first.md", "wb") as ff:
        ff.write(r.content)
    with open("first.md", "r") as f:
        lines = f.readlines()
    with open("first_mod.md","w+") as f:
        f.write(r'{% include disclaimer.html translated="no" translationOutdated="no" %}')
        f.write("\n\n")
        for line in lines:
            # https://stackoverflow.com/a/44227600 [regex to parse markdown images]
            p = re.compile('!\[[^\]]*\]\((.*?)\s*("(?:.*[^"])")?\s*\)')
            m = p.search(line)
            if m:
                #print(m.group(0))
                url = m.group(1)
                a = urlparse(url)
                img_fname = os.path.basename(a.path)
                img_desc = str(m.group(0)).split("[")[1].split("]")[0]
                r = requests.get(url)
                with open(img_fname, "wb") as fpic:
                    fpic.write(r.content)
                
                # str replace group(0) with our new one 
                tail = f"/img/resources/user-guides/en/{title_key}"
                replaced= f"![{img_desc}]({tail}/{img_fname})"
                if not os.path.isdir(f"./monero-site/{tail}"):
                    os.makedirs(f"./monero-site/{tail}")
                # mv the picture somewhere
                if os.path.isfile(f"./monero-site/{tail}"):
                    os.remove(f"./monero-site/{tail}")
                shutil.move(img_fname,f"./monero-site/{tail}/{img_fname}")
                line = line.replace(str(m.group(0)),replaced)
            f.write(line)
    new_guide_md = f"./monero-site/_i18n/en/resources/user-guides/{title_key}.md"
    if os.path.isfile(new_guide_md):
        os.remove(new_guide_md)
    shutil.move("first_mod.md",new_guide_md)

    not_sure_what_this_is = f"""---
layout: user-guide
title: {title_text}
permalink: /resources/user-guides/{title_key}.html
outdated: False
---
{{% t global.lang_tag %}}
<h1>{{% t user-guides.{title_key} %}}</h1>
{{% tf resources/user-guides/{title_key}.md %}}
"""

    with open(f"./monero-site/resources/user-guides/{title_key}.md", "w+") as f:
        f.write(not_sure_what_this_is)

def main():
    global guide_category,title_key,title_text,markdown_url
    add_title_to_yaml(title_key,title_text)
    add_title_to_index(title_key,title_text,guide_category)
    handle_markdown_file(markdown_url,title_key,title_text)

if __name__ == "__main__":
    main()
