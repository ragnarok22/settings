import sys
import warnings


class LanguageNotFoundError(FileNotFoundError):
    def __init__(self, message):
        super(LanguageNotFoundError, self).__init__()
        self.message = message


class Language(object):
    def __init__(self, lang='en'):
        self.lang = lang

    def get_lang(self):
        return self.lang

    def set_lang(self, lang):
        self.lang = lang


def read_lang_file(lang):
    """
    :return un str que solo contiene los valores del idioma y la traduccion
    """
    file = lang + '.lng'
    string = ""
    try:
        with open(file, 'r') as f:
            for w in f.readlines():
                temp = w.split('#')
                string += temp[0]
        return string
    except FileNotFoundError:
        raise LanguageNotFoundError('The language File \'{0}\' was not found on folder \'language\''.format(file))
    except:
        print('Error inesperado', sys.exc_info()[0])


def words_dic(str_file):
    """
    :param str_file: es un str, es el contenido del fichero
    :return: un diccionario con las palabras como llave y su traduccion como valor
    """
    result = {}
    current = str_file.split('\n')
    for i in current:
        temp = i.split(':')
        result[temp[0]] = temp[1]
    return result


def gettext(text, parent):
    try:
        lang_file = read_lang_file(parent.lang)
        words = words_dic(lang_file)
        result = words.get(text, None)
        if result:
            return result  # si la palabra se encuentra en el fichero se retorna
        else:
            return text  # sino se retorna el mismo texto
    except LanguageNotFoundError as e:
        warnings.warn("Language not found. {0}".format(e.message), UserWarning)
        return text  # el idioma especificado no se encontro y se retorna el mismo texto
