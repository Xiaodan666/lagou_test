from time import sleep

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from apptest.wework_test.page.basepage import BasePage
from apptest.wework_test.page.home_page import HomePage


class App(BasePage):
    driver: WebDriver

    def start_app(self):
        if self.driver is None:
            desire_cap = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": True
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
            sleep(10)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(5)
        return self

    def close_app(self):
        self.driver.quit()

    def restart_app(self):
        pass

    def goto_main(self):
        return HomePage(self.driver)
