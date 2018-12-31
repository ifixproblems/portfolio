from selenium import webdriver
import unittest
import os



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver.exe'))
        self.browser = webdriver.Firefox(executable_path = gecko)
        self.browser.implicitly_wait(3)
      
    def tearDown(self):     
        self.browser.quit()
  
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')     
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
  
if __name__ == '__main__':
    unittest.main()  