### "A step by step guide would be too complex to follow."

Lets change that, and organise everything in alphabetic order too    

first impressions of parsing the html:

```Python
def add_faq_to_index(new_key,new_text,category):
    global en_yaml
    with open("faq_index.md", "r") as f:
        soup = BeautifulSoup(f, "html.parser")
    div = soup.find("ul")
    with open(en_yaml, 'r') as f:
        data_loaded = yaml.safe_load(f)
    lol = div.find_all("ul")
    print("general")
    for x in lol[0].find_all("li"):
        print(x)
    print("advanced")
    for x in lol[1].find_all("li"):
        print(x)
    print("nodeandwallet")
    for x in lol[2].find_all("li"):
        print(x)
add_faq_to_index("","","")
```
```
general
<li><a href="#anchor-word">{% t faq.qword %}</a></li>
<li><a href="#anchor-contribute">{% t faq.qcontribute %}</a></li>
<li><a href="#anchor-value">{% t faq.q1 %}</a></li>
<li><a href="#anchor-buy">{% t faq.q2 %}</a></li>
<li><a href="#anchor-different">{% t faq.q4 %}</a></li>
<li><a href="#anchor-btc-difference">{% t faq.q7 %}</a></li>
<li><a href="#asic-resistance">{% t faq.qasicresistance %}</a></li>
<li><a href="#anchor-fungibility">{% t faq.q11 %}</a></li>
<li><a href="#anchor-magic">{% t faq.q13 %}</a></li>
<li><a href="#anchor-anonymous">{% t faq.q14 %}</a></li>
<li><a href="#vulnerabilities">{% t faq.qvuln %}</a></li>
<li><a href="#antivirus">{% t faq.qantivirus %}</a></li>
<li><a href="#monero-meaning">{% t faq.qmoneromeaning %}</a></li>
<li><a href="#hardforks">{% t faq.qhf %}</a></li>
<li><a href="#videos">{% t faq.qvideos %}</a></li>
advanced
<li><a href="#anchor-thin-air">{% t faq.q12 %}</a></li>
<li><a href="#anchor-light-normal">{% t faq.q6 %}</a></li>
<li><a href="#anchor-block-limit">{% t faq.q8 %}</a></li>
<li><a href="#anchor-mixing">{% t faq.q15 %}</a></li>
<li><a href="#import-blockchain">{% t faq.qimporting %}</a></li>
<li><a href="#max-supply">{% t faq.qmaxsupply %}</a></li>
nodeandwallet
<li><a href="#anchor-wallet">{% t faq.qwallet %}</a></li>
<li><a href="#anchor-lost-funds">{% t faq.qnofunds %}</a></li>
<li><a href="#long-time-move">{% t faq.qlongtimemove %}</a></li>
<li><a href="#anchor-tor-node">{% t faq.qnodetor %}</a></li>
<li><a href="#anchor-long-sync">{% t faq.q5 %}</a></li>
<li><a href="#anchor-full-pruned">{% t faq.qfullpruned %}</a></li>
<li><a href="#anchor-block-size">{% t faq.qblocksize %}</a></li>
<li><a href="#anchor-block-space">{% t faq.qblockspace %}</a></li>
<li><a href="#anchor-avoid-bc">{% t faq.qavoidbc %}</a></li>
<li><a href="#anchor-scanned-wallet">{% t faq.qscanned %}</a></li>
<li><a href="#anchor-danger-node">{% t faq.qdangernode %}</a></li>
<li><a href="#anchor-danger-rnode">{% t faq.qdangerrnode %}</a></li>
```
