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
    for x in lol:
    	omg = x.find_all("li")
    	for ok in omg:
    		print(data_loaded["faq"][ok.text.split("faq.")[1].split(" %}")[0]])

add_faq_to_index("","","")
```
