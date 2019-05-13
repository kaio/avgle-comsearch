import urllib.request
import urllib.parse
import json

# Only works with 'jav', but seems this query may run through all categories.
AVGLE_SEARCH_JAV_API_URL = 'https://api.avgle.com/v1/jav/{}/{}?limit={}'
query = '巨乳'
page = 10
limit = 100000
response = json.loads(urllib.request.urlopen(AVGLE_SEARCH_JAV_API_URL.format(urllib.parse.quote_plus(query), page, limit)).read().decode())
#print(response)
if response['success']:
    videos = response['response']['videos']
    for v in videos:
        if v.get('channel') == '3' and v.get('hd') == True and v.get('framerate') >= 59:
            print(v.get('title') + v.get('video_url'))
    print(response['response']['current_offset'])
    print(response['response']['total_videos'])

    #do_something_with(videos)
