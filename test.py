# -*- coding: UTF-8 -*_
import re
import requests


respose = requests.get('http://www.xiaohuar.com/v/')


urls = re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)
url = urls[5]
result = requests.get(url)
mp4_url = re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]

video = requests.get(mp4_url)


with open('D:\\a.mp4','wb') as f:
    f.write(video.content)
