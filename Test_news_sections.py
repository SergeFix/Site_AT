from selenium import webdriver
import unittest
import News_sections

class NewsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://www.abw.by/")

    def test_top_news_number(self):
        """check number of news in top news section """
        news_obj = News_sections.NewsSection(self.driver)
        assert (news_obj.top_news_counter()==4), "number of news in top new section is abnormal"

    def test_click_top_news(self):
        """user clicks on top news"""
        news_obj = News_sections.NewsSection(self.driver)
        assert news_obj.click_top_news(), "Link in top news title is incorrect"



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()