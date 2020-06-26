from selenium.webdriver.common.by import By

from po_test.page.base_function import BaseFunction
from po_test.page.contacts_page import ContactsPage


class AddMemberPage(BaseFunction):
    _user_name = "xiaodantest"
    _acctid = "xiaodan"
    _phone = "17823232323"

    def add_member(self):
        self.find(By.ID, "username").send_keys(self._user_name)
        self.find(By.ID, "memberAdd_acctid").send_keys(self._acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(self._phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactsPage(self.driver)
