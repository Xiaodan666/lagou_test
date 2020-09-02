from appium.webdriver.common.mobileby import MobileBy

from apptest.wework_test.page.basepage import BasePage
from apptest.wework_test.page.modefy_member_page import ModefyMemberPage


# 个人信息页面
class PersonInfoPage(BasePage):
    def modefy_member(self):
        # 点击右上角
        self.find(MobileBy.XPATH, "//*[@text='个人信息']/../../../../../android.widget.LinearLayout[2]").click()
        # 点击编辑成员
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return ModefyMemberPage(self.driver)
