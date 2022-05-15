When adding a new 'user guide' the new title must be added to all the language .yml files.      
a yaml library to read/add/write will work but the entire structure of the file gets changed / huge diffs.    
a simple 'find what we're looking for' and 'add the new thing' will suffice    
e.g.    
```Python
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
```


Po config file script ~ all guides need a 'po' file which has the layout:    
a script to loop all files in a folder and create the matching po file will help    
will save a minute or two of time (see `make_po_configs.py`) :
```
[po4a_langs] es it pl fr ar ru de nl pt-br tr zh-cn zh-tw nb-no
[po4a_paths] ../_i18n/en/resources/user-guides/weblate/{TITLE OF GUIDE}.pot $lang:../_i18n/$lang/resources/user-guides/weblate/{TITLE OF GUIDE}.po

[options] opt:"--keep=0"
[options] opt:"--localized-charset=UTF-8"
[options] opt:"--master-charset=UTF-8"
[options] opt:"--master-language=en_US"
[options] opt:"--msgmerge-opt='--no-wrap'"
[options] opt:"--wrap-po=newlines"

[po4a_alias:markdown] text opt:"--option markdown"

[type: markdown] ../_i18n/en/resources/user-guides/{TITLE OF GUIDE}.md $lang:../_i18n/$lang/resources/user-guides/{TITLE OF GUIDE}.md
```
