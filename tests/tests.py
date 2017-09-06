import unittest
from language import translate


class TestLanguageClass(unittest.TestCase):
    def setUp(self):
        class Window(translate):
            def __init__(self):
                super(Window, self).__init__()
                self.lang = 'es'
                self.btn = translate.gettext('setting', self)

        self.window = Window()

    def test_translate(self):
        self.assertEqual(self.window.btn, 'configuraci�n')


class TestLanguageClassInherit(unittest.TestCase):
    def setUp(self):
        class Window(translate.Language):
            def __init__(self):
                super(Window, self).__init__()
                self.btn = translate.gettext('setting', self)

        self.window = Window()

    def test_translate(self):
        self.assertEqual(self.window.btn, 'setting')


if __name__ == '__main__':
    unittest.main()
