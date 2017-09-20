import os
import unittest

from language.translate import Language, gettext as _


class TestLanguageClass(unittest.TestCase):
    def setUp(self):
        # create a language folder
        try:
            os.mkdir('language')
        except FileExistsError:
            pass
        # write a language file
        try:
            with open('language/es.lng', 'w') as file:
                string = """hello:hola\nyou:tu"""
                file.write(string)
            with open('language/en.lng', 'w') as file:
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

    def tearDown(self):
        """"
        Delete a language file
        """
        os.remove("language/es.lng")
        os.remove('language/en.lng')
        os.removedirs('language')


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
