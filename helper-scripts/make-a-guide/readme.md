Python 3+
```
pip install yaml
pip install beautifulsoup4
```
## How? 

Place the python script in the same directory as your `monero-site` github folder      
Edit these lines:
```
category = "anonimizationnetworks"
title_text = "This is a new guidelol" 
title_key = "some-new-guides" #This will end up as the file name / url "some-new-guides.html" - so keep this short and to the point 
markdown_url = "https://raw.githubusercontent.com/plowsof/userguide-drafts/main/i2p/monero-gui-i2p-node.md"
```
The script will detect images in your markdown file, download them, do all the leg work of placing them in the correct folder / correct href links.    

Thats it.. your monero-site folder should be populated with all the files needed to make a PR with your guide

## What it does

Lets you create a guide on github. You can put images in it to because the script will find them, and put them in the correct monero-site folder for your guide. Simply point the script to the raw text version, and it will do the rest for you.
