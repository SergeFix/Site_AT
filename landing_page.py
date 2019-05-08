from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class LandingPage():
    """A class for landing page locators and methods."""
    def __init__(self, driver):
        self.driver = driver

        self.