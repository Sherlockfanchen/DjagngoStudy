from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_latter(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('TO-DO',self.browser.title)
        self.fail('Finish the test')


if __name__ =='__main__':
    unittest.main(warnings='ignore')


# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
#
# #assert 'None' in browser.title,
# "Browser title was" + browser.title