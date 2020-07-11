from appium.webdriver.common.mobileby import MobileBy

from apptest.wework_test.page.addmenberpage import AddMemberPage
from apptest.wework_test.page.basepage import BasePage
from apptest.wework_test.page.person_info_page import PersonInfoPage

# 通讯录页面
class ContactsPage(BasePage):
    def goto_add_member(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return AddMemberPage(self.driver)
    def goto_person_info(self,username):
        self.find_by_scroll(username).click()
        return PersonInfoPage(self.driver)

    # def get_contacts(self):
    #     contact_list = []
    #     return contact_list
