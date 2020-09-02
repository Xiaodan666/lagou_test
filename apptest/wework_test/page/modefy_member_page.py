from appium.webdriver.common.mobileby import MobileBy

from apptest.wework_test.page.basepage import BasePage
from po_test.page.contacts_page import ContactsPage


# 编辑成员页面（可点击删除按钮）
class ModefyMemberPage(BasePage):
    def delete_member(self):
        # 点击删除成员
        # 滚动查找没有找到元素，后面再看下
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        # 点击确定
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        return ContactsPage(self.driver)
