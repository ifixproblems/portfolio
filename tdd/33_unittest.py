from selenium import webdriver
import os
import unittest

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver.exe'))
browser = webdriver.Firefox(executable_path = gecko)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
			
	def test_django_title(self):
		browser.get('http://localhost:8000')
		assert 'Django' in browser.title


if __name__ == '__main__':
    unittest.main()