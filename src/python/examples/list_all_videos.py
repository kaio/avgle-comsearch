import urllib.request
import json
AVGLE_LIST_VIDEOS_API_URL = 'https://api.avgle.com/v1/videos/{}?limit={}'
page = 0
limit = 10
response = json.loads(urllib.request.urlopen(AVGLE_LIST_VIDEOS_API_URL.format(page, limit)).read().decode())
print(response)
if response['success']:
    videos = response['response']['videos']
    #do_something_with(videos)
