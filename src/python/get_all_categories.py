import urllib.request
import json
AVGLE_CATEGORIES_API_URL = 'https://api.avgle.com/v1/categories'
response = json.loads(urllib.request.urlopen(url).read().decode())
print(response)
if response['success']:
    categories = response['response']['categories']
    #do_something_with(categories)
