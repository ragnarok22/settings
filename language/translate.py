import os
import sys
import warnings

LANG_FOLDER_NAME = 'languages'
EXTENSION = '.lng'


class LanguageNotFoundError(FileNotFoundError):
    def __init__(self, message):
        super(LanguageNotFoundError, self).__init__()
        self.message = message

    def __str__(self):
        return self.message


class Language(object):
    def __init__(self, lang='en'):
        self.lang = lang

    def get_lang(self):
        return self.lang

    def set_lang(self, lang):
        self.lang = lang


def read_lang_file(lang):
    """
    read the language file and erase the comments
    :param lang: the language
    :return: a string with only the word and the translation
    """
    file = lang + EXTENSION
    string = ""
    # noinspection PyBroadException
    try:
        with open('{0}/{1}'.format(LANG_FOLDER_NAME, file), 'r') as f:
            for w in f.readlines():
                temp = w.split('#')
                string += temp[0].strip(' ')
        return string
    except FileNotFoundError:
        raise LanguageNotFoundError('The language File \'{0}\' was not found on \'{1}\' folder'.
                                    format(file, LANG_FOLDER_NAME))
    except:
        print('Unexpected error', sys.exc_info()[0])


def write_lang_file():
    try:
        os.mkdir(LANG_FOLDER_NAME)
    except FileExistsError:
        pass


def words_dic(str_file):
    """
    :param str_file: a file content
    :return: a dictionary with the words as key and his translation as value
    """
    result = {}
    current = str_file.split('\n')
    for i in current:
        if i == '':
            continue
        temp = i.split(':')
        result[temp[0]] = temp[1]
    return result


def gettext(text, parent):
    if not parent:
        parent = Language('en')
    try:
        lang_file = read_lang_file(parent.lang)
        words = words_dic(lang_file)
        result = words.get(text, None)
        if result:
            return result  # if the word is found in the file, it returns him
        else:
            return text  # else it returns the same text
    except LanguageNotFoundError as e:  # the idiom specified is not found and returns the same text
        warnings.warn("Language not found. {0}".format(e.message), UserWarning)
        return text
