from time import sleep

from selenium.webdriver.common.by import By

from baidu_test.page.base_page import BasePage


class SearchDetailPage(BasePage):
    def check_title(self):
        self.find(By.ID, "su").click()
        sleep(10)
        return self.driver.title
