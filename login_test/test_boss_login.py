from selenium import webdriver
import pytest


class TestBoss:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def get_boss_cookie(self):
        self.driver.get("https://www.zhipin.com/")
