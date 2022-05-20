## How? 

Place the python script in the same directory as your `monero-site` folder.    
Edit these lines:
```
category = "anonimizationnetworks"
title_text = "This is a new guidelol"
title_key = "some-new-guides"
markdown_url = "https://raw.githubusercontent.com/plowsof/userguide-drafts/main/i2p/monero-gui-i2p-node.md"
```
The script will detect images in your markdown file, download them, do all the leg work of placing them in the correct folder / correct href links.    

Thats it.. your monero-site folder should be populated with all the files needed to make a PR with your guide
