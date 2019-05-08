from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
import header

class HeaderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://www.abw.by/")

    def test_header_logo (self):
        """check user navigates on landing page after click Logo button"""
        self.driver.get('https://www.abw.by/novosti/')
        header_obj = header.Header(self.driver)
        assert header_obj.logo_click(), "wrong logo link or logo is not found"

    def test_header_news_button_click(self):
        """check user navigates on news page after click news button"""
        header_obj = header.Header(self.driver)
        assert header_obj.newsbtn_click(), "wrong news link or news button is not found"

    def test_header_news_dd_menu(self):
        """check news submenu and part of buttons in it"""
        header_obj = header.Header(self.driver)
        for i in header_obj.submenu_links:
            header_obj.newsbtn_mouse_on()
            assert header_obj.news_submenu_click(i) == header_obj.submenu_links[i]




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()