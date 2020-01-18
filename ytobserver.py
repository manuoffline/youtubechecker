# Url lib accede a la api de youtube y comprueba el video mas reciente
import datetime
import json
import os
import time
import urllib
import urllib.request

from selenium import webdriver

import constants

CHECK_TIME = 10


def new_video():
    api = "AIzaSyCFGkta5WvXE6P7gV1LIZFmfhluIMozg1Y"
    channel = "UCPu5nstS7cbx_GUiH-kxwVw"  # pantomima channel

    url = constants.SEARCH_URL + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(constants.API,
                                                                                                      channel)
    jsu = urllib.request.urlopen(url)
    resp = json.load(jsu)

    videoId = resp['items'][0]['id']['videoId']
    print(datetime.datetime.now(), " :", videoId)

    is_new_video = True

    if not os.path.exists('video.json'):
        f = open('video.json', 'w+')
        f.write('{"videoId": "null"}')

    with open('video.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != videoId:
            # driver = webdriver.Firefox(executable_path=r'path')
            # driver.get(constants.VIDEO_URL + videoId)
            is_new_video = True

    if is_new_video:
        with open('video.json', 'w', encoding='utf8') as json_file:
            data = {'videoId': videoId}
            json.dump(data, json_file)


try:
    while True:
        new_video()
        time.sleep(renew_time)
except KeyboardInterrupt:
    print("stopped")
