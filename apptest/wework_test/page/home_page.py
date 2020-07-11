from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from apptest.wework_test.page.basepage import BasePage
from apptest.wework_test.page.contacts_page import ContactsPage


class HomePage(BasePage):
    def goto_contacts_page(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        sleep(5)
        return ContactsPage(self.driver)
