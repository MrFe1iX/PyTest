import allure
import time

from selenium import webdriver
from allure_commons.types import AttachmentType

exec_path = 'driver/chromedriver.exe'

class TestPageSearch:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)

    def teardown(self):
        self.driver.quit()


    def test_google(self):
        self.driver.get('https://google.com')
        assert self.driver.title == 'Google'
        self.driver.find_element_by_name('q').send_keys('Тестовый поиск')
        self.driver.find_element_by_name('btnK').click()