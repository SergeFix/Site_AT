from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class NewsSection():
    #A class for new sections on landing page
    def __init__(self, driver):
        self.driver = driver

        self.top_news_class = "top-news-item simple-item top-news-item"
        self.first_top_news = "//*[@class='top-news-item simple-item top-news-item-m']"
        self.first_top_news_descr = "//*[@class='top-news-item simple-item top-news-item-m']//" \
                                    "div[@class='top-news-item-inner']"
        self.news_on_own_page = "//*[@class='article__header article__header--image']"


    def top_news_counter(self):
        #return number of top news
        top_news_number = self.driver.find_elements_by_xpath("//div[contains(@class,'top-news-item simple-item top-news-item')]")
        return len(top_news_number)

    def click_top_news(self):
        #user clicks on top news
        news_id = self.driver.find_element_by_xpath(self.first_top_news)
        # get news title from top news section
        news_title = news_id.value_of_css_property('title')
        news_id.click()
        #check news page is loaded
        try:
            WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH, self.news_on_own_page)))
        except NoSuchElementException:
            print("link to news page is not correct")
        # get news title from news page
        news_title_2 = self.driver.find_element_by_xpath(self.news_on_own_page).value_of_css_property('title')
        return news_title == news_title_2