from bs4 import BeautifulSoup

with open("testing.md", "r") as f:
	soup = BeautifulSoup(f, "html.parser")
# 5. Create a Beautiful Soup Object

divs = soup.find_all("div", {"class": "col"})

for div in divs:
	print(div.find("h2"))
	ps = div.find_all("p")
	for p in ps:
		print(p)
	print("*******************************")
	
'''
with open("test.yaml","r") as f:
	lines = f.readlines()

new_lines = []
for line in lines:
	new_lines.append(line)
	if "user-guides" in line:
		new_lines.append("  DEBUG: This is the way\n")

with open("test.yaml", "w") as f:
	for line in new_lines:
		f.write(line)
'''

'''output
<h2>{% t user-guides.general %}</h2>
<p><a href="{{site.baseurl}}/resources/user-guides/securely_purchase.html">{% t user-guides.purchasing-storing %}</a></p>
<p><a href="{{site.baseurl}}/resources/user-guides/make-payment.html">{% t user-guides.make-payment %}</a></p>
<p><a href="{{site.baseurl}}/resources/user-guides/prove-payment.html">{% t user-guides.prove-payment %}</a></p>
*******************************
<h2>{% t user-guides.mining %}</h2>
<p><a href="{{site.baseurl}}/resources/user-guides/mine-to-pool.html">{% t user-guides.mine-on-pool %}</a></p>
<p><a href="{{site.baseurl}}/resources/user-guides/solo_mine_GUI.html">{% t user-guides.solo-mine %}</a></p>
*******************************
'''
