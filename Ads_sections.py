from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

class AdsSections():
    ##A class for ads sections on landing page
    def __init__(self, driver):
        self.driver = driver

        self.brand_search = "//span[@class='filter-option pull-left'][text()='Выберите марку авто']"
        self.brand_search_ddl = "//div[@id='content']//div[@class='select-wrapper box-wrapper']//li[3]"
        self.model_search = "//span[@class='filter-option pull-left'][text()='Выберите модель авто']"
        self.model_search_ddl = "//div[contains(@class,'btn-group bootstrap-select show-tick js-select-model-new dropup open')]//li[1]"
        self.year_from_search_empty = "//*[@class='select-wrapper box-wrapper year1']//button[@title='Год, от']"
        self.year_from_search_filled = "//span[contains(@class,'filter-option pull-left')][contains(text(),'2012 г.в')]"
        self.year_from_search_ddl = "//div[@class='select-wrapper box-wrapper year1']//div[@class='box-inner-wrapper']//li[9]"
        self.search_cars_btn = "//button[@class='new_form'][contains(text(), 'Найти')]"
        self.empty_search = "//p[contains(text(),'По вашему запросу не найдено ни одного объявления.')]"
        self.found_cars = "//div[@class='b-item_description']//a[contains(text(),'BMW')]"
        self.ads_lp = "//[@class='row row-no-paddings row-4 row-flex row-products']//[@class='simple-item-content-inner']"


    def select_brand(self):
        #user choose car's brand (BMW)
        brand_id = self.driver.find_element_by_xpath(self.brand_search)
        brand_id.click()
        self.driver.find_element_by_xpath(self.brand_search_ddl).click()
        return brand_id.text == 'BMW'

    def select_model(self):
        #user choose car's model
        model_id = self.driver.find_element_by_xpath(self.model_search)
        model_id.click()
        self.driver.find_element_by_xpath(self.model_search_ddl).click()
        return model_id.text == 'Любая'

    def select_year_from(self):
        #user choose car's year from
        year_from_id = self.driver.find_element_by_xpath(self.year_from_search_empty)
        year_from_id.click()
        self.driver.find_element_by_xpath(self.year_from_search_ddl).click()
        year_from_id = self.driver.find_element_by_xpath(self.year_from_search_filled)
        return year_from_id.text == '2012 г.в'

    def run_search(self):
        self.driver.find_element_by_xpath(self.search_cars_btn).click()

    def cars_search_not_empty (self):
        # check that search isn't empty
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located
                                                ((By.XPATH, "//title[contains(text(),'новый или б/у купить в Беларуси. Объявления')]")))
        except NoSuchElementException:
            print ('search results page is not opened')

        search_alert_numb = self.driver.find_elements_by_xpath(self.empty_search)
        return len(search_alert_numb) == 0


    def check_search_results(self):
        # check search results have keyword('BMW')
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located
                                                ((By.XPATH, "//title[contains(text(),'новый или б/у купить в Беларуси. Объявления')]")))
        except NoSuchElementException:
            print ('search results page is not opened')

        return len(self.driver.find_elements_by_xpath(self.found_cars)) > 0


