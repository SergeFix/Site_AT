# from selenium import webdriver
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# import time

class Header():
    """A class for header page locators and methods."""
    def __init__(self, driver):
        self.driver = driver

        self.logo_css = "div.logo"
        self.news_css = 'a[class="top-menu-item js-top-menu-item"][href="/novosti/"]'
        self.forum_xpath = '//a[@class="top-menu-item"][text()="Форум"]'
        self.login_class = 'icon-login'
        self.create_adds_xpath = '//div[@class="navigation"]//a[@class="add-product"]'
        self.search_class = 'icon-search'

        self.submenu_links = {'Лента новостей': 'https://www.abw.by/novosti/',
                         'Популярное': 'https://www.abw.by/novosti/top/',
                         'Обсуждаемое': 'https://www.abw.by/novosti/discuss/', 'Подписка': 'https://www.abw.by/rss/',
                         'Архив газеты': 'https://www.abw.by/archive/',
                         'Обсуждение новостей': 'https://www.abw.by/forum/forum27.html'}

    def logo_click(self):
        """user clicks Logo button"""

        self.driver.find_element_by_css_selector (self.logo_css).click()
        return "Продажа и покупка автомобилей в Беларуси, Автобизнес ABW.BY:" \
               " объявления о покупке и продаже новых и б/у машин" in self.driver.title

    def newsbtn_click(self):
        """user clicks news button"""
        self.driver.find_element_by_css_selector(self.news_css).click()
        return "Автоновости:" in self.driver.title

    def newsbtn_mouse_on(self):
        """user hover mouse on Новости button"""
        news_btn = self.driver.find_element_by_css_selector(self.news_css)
        actions = ActionChains(self.driver)
        actions.move_to_element(news_btn).perform()

    def news_submenu_click(self, xploc):
        """user clicks on news submenu button"""
        self.submenu_btns_xpath = '//div[@class="submenu js-submenu"]//a[contains(text(), "' + xploc + '")]'
        self.driver.find_element_by_xpath(self.submenu_btns_xpath).click()
        return self.driver.current_url

