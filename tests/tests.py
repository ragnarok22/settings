import os
import unittest

from language import translate


class TestLanguageClass(unittest.TestCase):
    def setUp(self):
        # write a language file
        try:
            with open('es.lng', 'w') as file:
                string = """hello:hola\nyou:tu"""
                file.write(string)
        except FileNotFoundError:
            pass

        # create a Language Class
        class Window(translate.Language):
            def __init__(self):
                super(Window, self).__init__()
                self.lang = 'es'
                self.btn = translate.gettext('hello', self)

        self.window = Window()

    def test_translate(self):
        self.assertEqual(self.window.btn, 'hola')

    def tearDown(self):
        """"
        Delete a language file
        """
        os.remove("es.lng")


class TestLanguageClassInherit(unittest.TestCase):
    def setUp(self):
        class Window(translate.Language):
            def __init__(self):
                super(Window, self).__init__()
                self.btn = translate.gettext('hello', self)

        self.window = Window()

    def test_not_translate(self):
        self.assertEqual(self.window.btn, 'hello')


if __name__ == '__main__':
    unittest.main()
