from bs4 import BeautifulSoup
#
# from almanac import Almanac
# from config import google_image_search_url
import requests
from almanac import Almanac


class Niffler():
    def __init__(self, keyword, count):
        self.keyword = keyword
        self.count = count
        self.almanac = Almanac()

    def sniff(self, handle_name):
        # search_url = google_image_search_url.format(search_key=self.keyword)
        search_url = self.almanac.get_image_search_url_and_params(handle_name, self.keyword)
        page = requests.get(search_url).content
        soup = BeautifulSoup(page, 'html.parser')
        image_tags = soup.find_all('img', limit=self.count)
        image_urls = [image_tag.get('src') for image_tag in image_tags]
        print(image_urls)
        return image_urls
