from selenium.webdriver import ActionChains

class Header():
    """A class for header page locators and methods."""
    def __init__(self, driver):
        self.driver = driver

        self.logo_css = "div.logo"
        self.news_css = 'a[class="top-menu-item js-top-menu-item"][href="/novosti/"]'
        self.forum_xpath = '//a[@class="top-menu-item"][text()="Форум"]'
        self.login_class = 'icon-login'
        self.create_adds_xpath = '//div[@class="navigation"]//a[@class="add-product"]'


        self.submenu_links = {'Лента новостей': 'https://www.abw.by/novosti/',
                         'Популярное': 'https://www.abw.by/novosti/top/',
                         'Обсуждаемое': 'https://www.abw.by/novosti/discuss/', 'Подписка': 'https://www.abw.by/rss/',
                         'Архив газеты': 'https://www.abw.by/archive/',
                         'Обсуждение новостей': 'https://www.abw.by/forum/forum27.html'}
        # login form locators
        self.login_form_class = 'mfp-content'
        self.username_xpath = '//*[@class="mfp-content"]//input[@id="login"]'
        self.password_xpath = '//*[@class="mfp-content"]//input[@id="pass"]'
        self.login_btn_xpath = '//*[@class="mfp-content"]//button[@type="submit"]'
        self.wrong_login = '//div[@class="js-error error-message"][contains(text(), "Некорректный логин или пароль: ")]'
        self.loggedin_form_class = 'login-navigation-inner'

        #search
        self.search_class = 'icon-search'
        self.search_field = '//div[@class="header-search-block js-search-tabs open-search-block"]//' \
                                  'input[@placeholder="Введите текст для поиска"]'
        self.search_res_empty = 'search-page-result__not-found'



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

    def login_click_not_loggedin(self):
        """user clicks login button"""
        self.driver.find_element_by_class_name(self.login_class).click()
        try:
            self.login_form = self.driver.find_element_by_class_name(self.login_form_class)
        except NoSuchElementException:
            print ('login form is not found')
        return self.login_form.value_of_css_property('hidden')

    def login_click_loggedin(self):
        """user clicks login button"""
        self.driver.find_element_by_class_name(self.login_class).click()
        return self.driver.find_element_by_class_name(self.loggedin_form_class)

    def enter_username(self, username):
        self.driver.find_element_by_xpath( self.username_xpath).clear()
        self.driver.find_element_by_xpath( self.username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_xpath).clear()
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()
        return self.driver.find_element_by_xpath (self.wrong_login)

    def click_search(self):
        # click magnifier icon
        self.driver.find_element_by_class_name(self.search_class).click()
        return self.driver.find_element_by_xpath(self.search_field)

    def run_search(self, keyword):
        search_field = self.driver.find_element_by_xpath(self.search_field)
        search_field.clear()
        search_field.send_keys(keyword)
        search_field.send_keys(u'\ue007')

    def search_results_general(self):
        search_results = self.driver.find_elements_by_class_name(self.search_res_empty)
        print (len(search_results))
        return len(search_results)


