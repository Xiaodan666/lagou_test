from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, value):
        return self.driver.find_element(by,value)

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("{text}").instance(0));')

    def get_toast(self):
        return self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text

    def back(self, num=1):
        for i in range(num):
            self.driver.back()
