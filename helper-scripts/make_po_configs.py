import os

folder = "user-guides"
resource_dir = f"./monero-site/resources/{folder}"
config_dir = f"./monero-site/po/{folder}"

for root, dirs, files in os.walk(resource_dir, topdown=False):
	for file_name in files:
		head = file_name.split(".")[0]
		save_as = os.path.join(config_dir,f"{head}.config")
		if not os.path.isfile(save_as):
			po_file = f"""[po4a_langs] es it pl fr ar ru de nl pt-br tr zh-cn zh-tw nb-no
[po4a_paths] ../_i18n/en/resources/user-guides/weblate/{head}.pot $lang:../_i18n/$lang/resources/user-guides/weblate/{head}.po

[options] opt:"--keep=0"
[options] opt:"--localized-charset=UTF-8"
[options] opt:"--master-charset=UTF-8"
[options] opt:"--master-language=en_US"
[options] opt:"--msgmerge-opt='--no-wrap'"
[options] opt:"--wrap-po=newlines"

[po4a_alias:markdown] text opt:"--option markdown"

[type: markdown] ../_i18n/en/resources/{folder}/{head}.md $lang:../_i18n/$lang/resources/{folder}/{head}.md"""
			with open(save_as, "w+") as f:
				f.write(po_file)
