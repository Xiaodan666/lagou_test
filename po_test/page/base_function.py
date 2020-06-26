from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BaseFunction:
    _base_url = ""

    def __init__(self, base_driver: WebDriver = None):
        """
        初始化方法，判断调用该方法时是否有传入driver,如果有，则不再进行实例化driver,直接使用传入的driver
        :param base_driver:
        """
        if base_driver is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
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
