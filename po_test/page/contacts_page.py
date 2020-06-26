from time import sleep

from selenium.webdriver.common.by import By

from po_test.page.base_function import BaseFunction
from po_test.page.import_page import ImportPage


class ContactsPage(BaseFunction):

    def delete_member(self, member_name):
        """
        选择一个成员，点击删除，返回删除成功的提示
        :return:
        """
        # 获取列表中所有的成员信息-->父元素
        members = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_tr_Inactive")
        # 遍历父元素，找到想要删除的成员
        for member in members:
            if member.find_elements(By.TAG_NAME, "td")[1].text == member_name:
                checkbox = member.find_elements(By.TAG_NAME, "td")[0]
                checkbox.click()
        self.find(By.CSS_SELECTOR, ".js_delete").click()
        sleep(3)
        self.driver.execute_script("$('.ww_dialog_foot > a')[0].click()")
        return ContactsPage(self.driver)

    def goto_import_contacts(self):
        self.find(By.CSS_SELECTOR, ".ww_btn_PartDropdown_left").click()
        return ImportPage(self.driver)

    def get_member_list(self):
        member_list = []
        member_names = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        for name in member_names:
            member_list.append(name.text)
        return member_list
