from selenium.webdriver.common.by import By

from po_test.page.add_member_page import AddMemberPage
from po_test.page.base_function import BaseFunction
from po_test.page.contacts_page import ContactsPage
from po_test.page.import_page import ImportPage


class HomePage(BaseFunction):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contacts(self):
        """
        点击导航上的通讯录，跳转到通讯录页面
        :return: 通讯录页面
        """
        self.find(By.ID, "menu_contacts").click()
        return ContactsPage()

    def goto_import_contacts(self):
        """
        点击下方的导入通讯录，跳转到导入通讯录页面
        :return: 导入通讯录页面
        """
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        return ImportPage(self.driver)

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)
