import urllib.request
import json
AVGLE_LIST_COLLECTIONS_API_URL = 'https://api.avgle.com/v1/collections/{}?limit={}'
page = 0
limit = 2
response = json.loads(urllib.request.urlopen(url.format(page, limit)).read().decode())
print(response)
if response['success']:
    collections = response['response']['collections']
    #do_something_with(collections)
