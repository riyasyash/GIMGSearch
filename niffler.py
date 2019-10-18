from bs4 import BeautifulSoup
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
        soup = BeautifulSoup(page, 'html.parser').findall('div', {"id": "search"}, limit=1)[0]
        image_tags = soup.find_all('img', limit=self.count)
        image_urls = self.get_urls_from_parent(image_tags)
        # image_urls = [image_tag.get('src') for image_tag in image_tags]
        print(image_urls)
        return image_urls

    def get_urls_from_parent(self, img_tags):
        img_urls = []
        for img_tag in img_tags:
            parent = img_tag.parent
            while parent.name != 'a':
                parent = parent.parent
            img_urls.append(parent.get('href'))
        return img_urls
