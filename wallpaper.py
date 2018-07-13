#!/usr/bin/python

import os
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import datetime
import json

path = '/home/pol.naranjo/wallpaper/'
pics_path = '/home/pol.naranjo/wallpaper/pics/'
today = datetime.datetime.strftime(datetime.datetime.today(), '%Y-%m-%d')
#if 'wallpaper_{}.jpg'.format(today) not in os.listdir(pics_path):
url = 'https://www.nationalgeographic.com/photography/photo-of-the-day/'
f = urlopen(url)
soup = BeautifulSoup(f, 'lxml')
url_image = soup.find("meta",  property="og:image")['content']
urlretrieve(url_image, os.path.join(pics_path, 'wallpaper_{}.jpg'.format(today)))

a = soup.find_all(class_ = 'ad-template-type--pod')[0]
b = a.find_all('section', class_='main-section')[0]
c = b.find_all('article', class_='news__article sticky-box-ad-area')[0]
#d = c.find_all('div', id_='article__body__wrap')
d = c.find_all('div', class_='article-controller lead')[0]
e = d.find_all('div', class_='lead-component')[0]
f = e.find_all('script')[0]
text = f.get_text().rstrip().lstrip()
text_json=json.loads(text)
text = text_json['dek']['dek']['text'].replace('<p>','').replace('</p>','')
text_file = open(os.path.join(path, 'wallpaper.txt'), "w")
text_file.write(text)
text_file.close()


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open(os.path.join(pics_path, 'wallpaper_{}.jpg'.format(today)))
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
#font = ImageFont.truetype("sans-serif.ttf", 16)
font = ImageFont.truetype('/usr/share/fonts/gnu-free/FreeSerif.ttf', 48)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),text,(0,0,0))#,font=font)
img.save('sample-out.jpg')
