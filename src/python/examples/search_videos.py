import urllib.request
import urllib.parse
import json
AVGLE_SEARCH_VIDEOS_API_URL = 'https://api.avgle.com/v1/search/{}/{}?limit={}'
query = '三上悠亜'
page = 0
limit = 2
response = json.loads(urllib.request.urlopen(AVGLE_SEARCH_VIDEOS_API_URL.format(urllib.parse.quote_plus(query), page, limit)).read().decode())
print(response)
if response['success']:
    videos = response['response']['videos']
    #do_something_with(videos)
