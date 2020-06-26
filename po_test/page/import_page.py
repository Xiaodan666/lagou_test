from selenium.webdriver.common.by import By

from po_test.page.base_function import BaseFunction


class ImportPage(BaseFunction):
    def import_contacts(self):
        self.find(By.ID, "js_upload_file_input").send_keys("E:\lagou_test\datas\testdatas\potest.xlsx")
        file_name=self.find(By.ID, "upload_file_name").text
        return file_name
