from selenium import webdriver
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

    def test_login_failed(self):
        """login attempt with incorrect data"""
        header_obj = header.Header(self.driver)
        # try to open login form
        assert not header_obj.login_click_not_loggedin(), "login frame is not displayed"
        # fill in form with incorrect data
        header_obj.enter_username("test_user")
        header_obj.enter_password("test_password")
        #check alert about incorrect logon/password
        assert header_obj.click_login_btn(), "alert about incorrect logon/password is absent"
        #check user is not logged in
        assert header_obj.login_click_loggedin(), "user with incorrect credentials are logged in"

    def test_search(self):
        """test search"""
        header_obj = header.Header(self.driver)
        #open search form
        assert header_obj.click_search(), "search form is unavailable"
        #try to search by keyword having not empty results
        header_obj.run_search('renault')
        #check search found specific article
        assert (header_obj.search_results_general() == 0) , 'nothing found, expected several news in results'

    def test_(self):
        """"""
        header_obj = header.Header(self.driver)




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()