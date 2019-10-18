from image_search import Niffler


class GIMGSearch():
    '''
    Library to scrape Google images for the submitted key word and returns submitted number of image urls
    '''

    def __init__(self):
        self.number_of_images_to_be_returned = 1  # by default setting the images to be returned as one.
        self.key_word_to_be_searched = None

    def search(self, key_word_to_be_searched=None,number_of_images_to_be_returned=None ):
        '''

        :param key_word_to_be_searched:
        :param number_of_images_to_be_returned:
        :return: image urls matching the submitted key_word
        '''
        if key_word_to_be_searched is None:
            raise Exception('key word to sniff is not submitted')
        self.key_word_to_be_searched = key_word_to_be_searched
        if number_of_images_to_be_returned:
            self.number_of_images_to_be_returned = number_of_images_to_be_returned

        return Niffler().sniff(self.key_word_to_be_searched, self.number_of_images_to_be_returned)
