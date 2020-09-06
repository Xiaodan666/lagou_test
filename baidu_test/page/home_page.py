from selenium.webdriver.common.by import By

from baidu_test.page import search_detail_page
from baidu_test.page.base_page import BasePage
from baidu_test.page.search_detail_page import SearchDetailPage


class HomePage(BasePage):
    _base_url = "https://www.baidu.com"

    def go_to_search_details_page(self, search_text):
        self.find(By.ID, "kw").send_keys(search_text)
        return SearchDetailPage(self.driver)
