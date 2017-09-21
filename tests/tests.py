import os
import unittest
import shutil

from language.translate import Language, gettext as _, read_lang_file, words_dic


class TestLanguageClass(unittest.TestCase):
    def setUp(self):
        # create a language folder
        try:
            os.mkdir('languages')
        except FileExistsError:
            pass
        # write a language file
        try:
            with open('languages/es.lng', 'w') as file:
                string = """# once upon a time three little pigs
hello:hola
you:tu # rock rules

"""
                file.write(string)
            with open('languages/en.lng', 'w') as file:
                string = """hola:hello"""
                file.write(string)
        except FileNotFoundError:
            pass

        # create a Language Class
        class Window(Language):
            def __init__(self):
                super(Window, self).__init__()
                self.lang = 'es'
                self.btn = _('hello', self)

        self.window = Window()

    def test_translate(self):
        self.assertEqual(self.window.btn, 'hola')

    def test_gettext_without_parent(self):
        self.assertEqual(_('hello', None), 'hello')

    def test_read_lang_file(self):
        string = "hello:hola\nyou:tu\n"
        self.assertEqual(read_lang_file('es'), string)

    def test_words_dic(self):
        dictionary = words_dic("hello:hola\nyou:tu\n")
        result = {'hello': 'hola', 'you': 'tu'}
        self.assertEqual(dictionary, result)

    def tearDown(self):
        """
        Delete a languages file
        """
        shutil.rmtree('languages')


class TestLanguageClassInherit(unittest.TestCase):
    def setUp(self):
        class Window(Language):
            def __init__(self):
                super(Window, self).__init__()
                self.btn = _('hello', self)

        self.window = Window()

    def test_not_translate(self):
        self.assertEqual(self.window.btn, 'hello')

    def test_gettext_without_parent_and_file(self):
        self.assertEqual(_('hello', None), 'hello')


if __name__ == '__main__':
    unittest.main()
