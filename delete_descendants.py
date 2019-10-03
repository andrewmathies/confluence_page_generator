import requests

from request_kwargs import *
from auth import encodeKey

url = 'https://geappliances.atlassian.net/wiki/rest/api/content/'

def main():
    email = input('Enter the email your Confluence account uses. Presumably this is your GE email.\n')
    apiKey = input('Enter the API key you made previously.\n')
    rootPageID = input('Enter the id of the Confluence page you want to delete the descendants of.\n')

    descendant_kwargs['headers']['Authorization'] = encodeKey(email, apiKey)
    resp = requests.get(url + rootPageID + '/descendant/page/', **descendant_kwargs)
    descendantsJson = resp.json()

    for page in descendantsJson['results']:
        id = page['id']
        name = page['title']

        delete_kwargs['headers']['Authorization'] = encodeKey(email, apiKey)
        resp = requests.delete(url + id, **delete_kwargs)

        try:
            deleteJson = resp.json()
            print('ERR, unexpected response')
            print(deleteJson)
            return
        except ValueError:
            print('Deleted page: ', name)

if __name__ == '__main__':
    main()