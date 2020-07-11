from appium.webdriver.common.mobileby import MobileBy

from apptest.wework_test.page.basepage import BasePage
from apptest.wework_test.page.editmemberpage import EditMemberPage

# 点击添加成员后的页面
class AddMemberPage(BasePage):
    def goto_edit_member_page(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditMemberPage(self.driver)

    def get_add_result(self):
        return self.get_toast()
