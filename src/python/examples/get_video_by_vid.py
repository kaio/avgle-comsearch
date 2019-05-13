import urllib.request
import json
AVGLE_GET_VIDEO_API_URL = 'https://api.avgle.com/v1/video/{}'
vid = '285917'
response = json.loads(urllib.request.urlopen(AVGLE_GET_VIDEO_API_URL.format(vid)).read().decode())
print(response)
if response['success']:
    video = response['response']['video']
    #do_something_with(video)
