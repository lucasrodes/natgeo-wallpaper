import os
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import datetime
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class NatGeoImageWallpaper(object):

    def __init__(self, url_natgeo):
        # Path of project
        self.pwd = os.getcwd()
        # Path to picture archive
        self.pictures_path = os.path.join(self.pwd, 'pics')
        self.assets_path = os.path.join(self.pwd, 'assets')
        # URL Nat Geo Photo of the Day
        self.url_natgeo = url_natgeo
        # Today's date
        self.today = datetime.datetime.strftime(datetime.datetime.today(),
                                                '%Y-%m-%d')
        self.soup = None

    def get_set_soup(self):
        """ Get web soup, i.e. xml and stuff.
        """
        f = urlopen(self.url_natgeo)
        self.soup = BeautifulSoup(f, 'lxml')

    def download_image(self):
        """ Downloads the NatGeo's Photo of the Day using the soup extracted
            from the website. Stores the image under the folder 'pics' with name
            `wallpaper_<today's date>.jpg`.
        """
        url_image = self.soup.find("meta", property="og:image")['content']
        print(self.pictures_path)
        urlretrieve(url_image,
                    os.path.join(self.pictures_path,
                                 'wallpaper_{}.jpg'.format(self.today)))

    def get_image_description(self):
        # TODO: Work in progress
        a = self.soup.find_all(class_='ad-template-type--pod')[0]
        b = a.find_all('section', class_='main-section')[0]
        c = b.find_all('article', class_='news__article sticky-box-ad-area')[0]
        # d = c.find_all('div', id_='article__body__wrap')
        d = c.find_all('div', class_='article-controller lead')[0]
        e = d.find_all('div', class_='lead-component')[0]
        f = e.find_all('script')[0]
        text = f.get_text().rstrip().lstrip()
        text_json = json.loads(text)
        text = text_json['dek']['dek']['text'].replace('<p>', '').\
            replace('</p>', '')
        text_file = open(os.path.join(self.assets_path, 'wallpaper.txt'), "w")
        text_file.write(text)
        text_file.close()

        return "Work in Progress"

    def generate_final_image(self, text_overlay=False):
        # Load image
        img = Image.open(os.path.join(self.pictures_path,
                                      'wallpaper_{}.jpg'.format(self.today)))
        draw = ImageDraw.Draw(img)

        if text_overlay:
            # Load font
            fontname = '/usr/share/fonts/gnu-free/FreeSerif.ttf'
            font = ImageFont.truetype(fontname, 48)
            # font = ImageFont.truetype(<font-file>, <font-size>)
            # font = ImageFont.truetype("sans-serif.ttf", 16)

            # Insert text on image
            text = self.get_image_description()
            draw.text((0, 0), text, (0, 0, 0))

        # Generate new image with text
        img.save(os.path.join(self.pictures_path, 'wallpaper.jpg'))

    def update(self):
        self.get_set_soup()
        self.download_image()
        self.generate_final_image()

# URL to NatGeo's photo of the day
url_natgeo = \
    'https://www.nationalgeographic.com/photography/photo-of-the-day/'
# Declare instance
ngiw = NatGeoImageWallpaper(url_natgeo=url_natgeo)
ngiw.update()
