# Confluence Page Generator
This project creates lots of Confluence pages at once. It takes as input a document such as [Test Plan](https://geappliances.atlassian.net/wiki/spaces/VFJXJ/pages/664830837/Test+Plan) where the tree of pages you want to make is defined as a bunch of nested lists.

![alt text](https://github.com/andrewmathies/confluence_page_generator/raw/master/images/word_doc.PNG "Word Doc")
![alt text](https://github.com/andrewmathies/confluence_page_generator/raw/master/images/confluence.PNG "Confluence")

**IMPORTANT** You cannot make more than one page with a given name in a space. For example in the SWQA Automation: Avenger RC17 space on Confluence, I can only have one page named Oven. So, if you try to make a page that already exists or specify the same name twice in your document, this project will still make the page but append ' - DUPLICATE' to the end of the name.

## Instructions
1. You need to make an API key. Go to [Create API Tokens](https://id.atlassian.com/manage/api-tokens) and press the Create API token button.
1. Give your token a name and press the Create button.
1. Press the Copy to clipboard button and immediately paste and save the key somewhere.
1. If you haven't already, define your tree of pages as a set of nested lists in a Word document or Confluence page. If you use a Confluence page, export the page to a Word document.
1. Open the Word document and save it as an xml file in this projects directory.
1. Record the key for the space you want these pages to be made in. This can be found from the url in your browser while you are on any page in that space. (ex. https://geappliances.atlassian.net/wiki/spaces/SPACE-KEY-HERE/pages/PAGE-ID-HERE/PAGE-NAME-HERE)
1. Record the id of the page in confluence that will act as the root for all of the pages we're going to make. You can find the id in the url when you navigate to that page in your browser. (ex. https://geappliances.atlassian.net/wiki/spaces/SPACE-KEY-HERE/pages/PAGE-ID-HERE/PAGE-NAME-HERE)
1. In a terminal, naviage to this projecs directory then run ```python main.py```
1. Enter the email your Confluence account uses. Presumably this is your GE email.
1. Enter the API key you created previously.
1. Enter the space key your recorded previously.
1. Enter the page id you recorded previously.
1. Enter the file name for the xml file you saved previously.

## Deleting pages
**WARNING** delete_descendants.py will delete all of the descendants of a page on Confluence. That means all of the children pages and all of those childrens children pages etc. If you enter the wrong ID you can permenantly delete LOTS of Confluence pages. I'm not sure if pages deleted this way can be recovered, and I'm not responsible for any pages you accidentally delete this way.

1. In a terminal, run ```python delete_descendants.py```
1. Enter the email your Confluence account uses. Presumably this is your GE email.
1. Enter the API key you created previously.
1. Enter id of the page you'd like to delete the descendants of. BE CAREFUL and double check you have the correct id. You can find the id in the url when you navigate to that page in your browser.
1. If you notice the names of the pages being deleted are not what you expect, immediately press Control-c to cancel the process. Hopefully you will never need to do this.
