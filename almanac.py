import config
from handler import Handler


class Almanac:

    def __init__(self):
        self.__handlers = list()
        self.load()

    def load(self):
        for handle_key in config.handle_keys:
            handle = Handler(handle_key, getattr(config, handle_key, {}))
            self.load_handle(handle)

    def load_handle(self, handle):
        self.__handlers.append(handle)

    def get_image_search_url_and_params(self, handle, *args):
        handler = self.__get_handle_by_name(handle)
        search_url = self.__get_search_url(handler, args)

    def __get_search_url(self, handler, *args):
        return handler.generate_search_url(*args)

    def __get_handle_by_name(self, handle):
        for handler in self.__handlers:
            if handler.name == handle:
                return handler
