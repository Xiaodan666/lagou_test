from appium.webdriver.common.mobileby import MobileBy

from apptest.wework_test.page.basepage import BasePage

# 添加成员信息页面
class EditMemberPage(BasePage):
    def input_name(self, username):
        self.find(MobileBy.XPATH, "//*[@text='姓名　']/../android.widget.EditText").send_keys(username)
        return self

    def set_gender(self, gender):
        self.find(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()
        return self

    def input_phone(self, phone_num):
        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone_num)
        return self

    def save(self):
        from apptest.wework_test.page.addmenberpage import AddMemberPage
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        return AddMemberPage(self.driver)
