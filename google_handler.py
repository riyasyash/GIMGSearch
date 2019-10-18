from handler import Handler


class GoogleHandler(Handler):
    name = 'Google'

    def generate_formatter(self, *args):
        self.__formatter = "{},{}".format(args, args)
