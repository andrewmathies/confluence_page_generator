import parse_xml
import requests
import datetime
import re

from auth import encodeKey
from node import Node
from request_kwargs import *

url = 'https://geappliances.atlassian.net/wiki/rest/api/content/'
spaceKey = ''
apiKey = ''
email = ''

def getNodesAtDepth(curDepth, maxDepth, node, nodes):
    if curDepth == maxDepth:
        nodes.append(node)
        return

    for child in node.children:
        getNodesAtDepth(curDepth + 1, maxDepth, child, nodes)

# TODO: get parent node id, use API to get children, check if the page is in the children
def pageExists(node):
    return False

def buildPage(node):
    if not node.parent:
        print('ERR, ', node, ' has no parent!!')
        return -1

    parentID = node.parent.id

    if not parentID:
        print('ERR, ', node.parent, ' has no id!!')
        return -1
    
    # POST request to Confluence API to make the new page
    post_kwargs['headers']['Authorization'] = encodeKey(email, apiKey)
    post_kwargs['json']['title'] = node.name
    post_kwargs['json']['ancestors'][0]['id'] = parentID
    post_kwargs['json']['space']['key'] = spaceKey
    post_kwargs['json']['body']['storage']['value'] = '<p>Created by Andrew\'s script at: ' + str(datetime.datetime.now()) + '</p>'

    resp = requests.post(url, **post_kwargs)
    json = ''

    try:
        json = resp.json()
    except ValueError:
        print('ERR, didn\'t get a response. Check the credentials you entered.')
        return -1
    
    if 'id' in json:
        node.id = json['id']
        print('Created page: ', node.name)
    elif 'message' in json:
        message = json['message']
        pattern = 'com.atlassian.confluence.api.service.exceptions.BadRequestException: A page with this title already exists:'
        matches = re.findall(pattern, message)

        if len(matches):
            # page already exists. retry with modified title
            node.name += ' - DUPLICATE'
            buildPage(node)
    else:
        print('ERR, bad response!!')
        print(json)
        return -1

def main():
    global spaceKey, apiKey, email

    if not email:
        email = input('Enter the email your Confluence account uses. Presumably this is your GE email.\n')
    if not apiKey:
        apiKey = input('Enter the API key you made previously.\n')
    if not spaceKey:
        spaceKey = input('Enter the key for the space in Confluence these pages will made in.\n')
    rootPageID = input('Enter the id of the Confluence page you want these pages to made under.\n')

    root = parse_xml.buildTree()
    root.id = rootPageID
    level = 1

    while True:
        levelNodes = []
        getNodesAtDepth(0, level, root, levelNodes)

        if not len(levelNodes):
            break

        for node in levelNodes:
            if not pageExists(node):
                result = buildPage(node)
                if result == -1:
                    return
        
        level += 1

if __name__ == '__main__':
    main()