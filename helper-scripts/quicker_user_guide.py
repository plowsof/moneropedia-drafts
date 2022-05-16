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
