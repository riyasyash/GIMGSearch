from bs4 import BeautifulSoup

from config import google_image_search_url
import requests

class IMGSearch():
    def __init__(self):
        pass

    def search(self,keyword,no_images):
        search_url = google_image_search_url.format(search_key = keyword)
        params = {
            'tbm':'isch',
            'q':keyword
        }
        page = requests.get(search_url, params).content
        soup = BeautifulSoup(page, 'html.parser')
        image_tags = soup.find_all('img',limit=no_images)
        image_urls = [image_tag.get('src') for image_tag in image_tags]
        return image_urls
