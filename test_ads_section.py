from selenium import webdriver
import unittest
import Ads_sections

class NewsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://www.abw.by/")

    def test_search_cars(self):
        """user search cars using filters"""
        ads_obj = Ads_sections.AdsSections(self.driver)
        # select brand
        assert ads_obj.select_brand(), "some issue with brand drop-down"
        # select model
        assert ads_obj.select_model(), "some issue with model drop-down"
        # select year(from)
        assert ads_obj.select_year_from(), "some issue with year from drop-down"
        # run cars search
        ads_obj.run_search()
        # check that search isn't empty
        assert ads_obj.cars_search_not_empty(), "search can't find cars"
        # check search results
        assert ads_obj.check_search_results(), "cars are not found"



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()