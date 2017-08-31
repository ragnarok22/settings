import unittest
import language


class TestLanguageClass(unittest.TestCase):
	def setUp(self):
		class Window(language.Language):
			def __init__(self):
				super(Window, self).__init__()
				self.lang = 'es'
				self.btn = language.gettext('setting', self)
		self.window = Window()
	
	def test_translate(self):
		self.assertEqual(self.window.btn, 'configuración')

		
class TestLanguageClassInherit(unittest.TestCase):
	def setUp(self):
		class Window(language.Language):
			def __init__(self):
				super(Window, self).__init__()
				self.btn = language.gettext('setting', self)
		self.window = Window()
	
	def test_translate(self):
		self.assertEqual(self.window.btn, 'setting')
		
		
if __name__ == '__main__':
	unittest.main()
