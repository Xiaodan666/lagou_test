import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            try:
                using_headless = os.environ["using_headless"]
            except KeyError:
                using_headless = None
                print("using_headless 环境变量没有配置，使用有界面方式进行自动化执行")
            chrome_options = Options()
            if using_headless is not None and using_headless.lower() == "true":
                print("使用无界面方式运行")
                chrome_options.add_argument("--headless")


            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.maximize_window()
        else:
            self.driver = base_driver

        if self._base_url != "":
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(3)

    def find(self, by, value):
        """
        查找一个元素
        :param by:
        :param value:
        :return:
        """
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        """
        查找多个元素
        :param by:
        :param value:
        :return:
        """
        return self.driver.find_elements(by, value)

    def quit(self):
        self.driver.quit()
