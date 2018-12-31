from selenium import webdriver
import os

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver.exe'))
browser = webdriver.Firefox(executable_path = gecko)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
