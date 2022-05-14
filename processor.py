import operator
import string
import urllib.request
import urllib.error
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from collections import OrderedDict


class Text:
    def __init__(self, content):
        self.content = content
        if self.__is_url():
            soup = BeautifulSoup(urllib.request.urlopen(self.content), features="html.parser")
            unwanted_tags = ['style', 'script']
            page_texts = [text for text in soup.find_all(string=True) if text.parent.name not in unwanted_tags]
            self.content = ''
            self.content = ' '.join(page_texts)
            self.words_by_count = self.__get_word_count()
        else:
            self.words_by_count = self.__get_word_count(translate=False)

    def __is_url(self):
        try:
            urllib.request.urlopen(self.content)
            return True
        except (urllib.error.URLError, ValueError) as err:
            print("Malformed URL; {err}".format(err=err))
            return False

    def __get_word_count(self, translate=True):
        if translate:
            text = self.content.casefold().translate(self.content.casefold().maketrans('', '', string.punctuation.replace("'", '')))
        else:
            text = self.content.casefold()
        words = [word.strip(string.punctuation) for word in text.split(' ')]
        word_count = {}
        while text.strip(' ') != '':
            word = text.split(' ')[0].strip(string.punctuation)
            if word.strip() != '':
                word_count[word] = words.count(word)
            text = ' '.join(text.split(' ')[1:])

        return word_count

    def sorted_wbc_by_count(self):
        '''
        wbc = self.words_by_count
        :return:
        self.words_by_count sorted by count (not in place); i.e. getting self.words_by_count after making a call to this function will return the unsorted version.
        '''
        sorted_wbc = sorted(self.words_by_count.items(), key=operator.itemgetter(1))
        return OrderedDict(sorted_wbc)

    def sorted_wbc_alphabetically(self):
        '''
        wbc = self.words_by_count
        :return:
        self.words_by_count sorted alphabetically (not in place) i.e. getting self.words_by_count after making a call to this function will return the unsorted version.
        '''
        sorted_wbc = sorted(self.words_by_count.items(), key=operator.itemgetter(0))
        return OrderedDict(sorted_wbc)


