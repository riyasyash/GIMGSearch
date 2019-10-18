class Handler:

    @property
    def name(self):
        return self.__name

    @property
    def search_url_template(self):
        return self.__search_url_template

    @property
    def params(self):
        return self.__params

    def __init__(self, name, handle_dict):
        self.__name = name
        self.__search_url_template = handle_dict["search_url"]
        self.__params = handle_dict["params"]
        self.__formatter = None

    def __repr__(self):
        return {
            "name": self.name,
            "search_url_template": self.search_url_template,
            "params": self.params
        }

    def generate_search_url(self, *args):
        self.generate_formatter(*args)
        return self.search_url_template.format(self.__formatter)

    def generate_formatter(self, *args):
        self.__formatter = args
