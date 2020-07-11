import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from apptest.wework_test.page.APP import App


class TestWework:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start_app().goto_main()

    @pytest.mark.parametrize('username,gender,phone_num',
                             yaml.safe_load(open('../../../datas/testdatas/appium.yml', encoding='UTF-8')).get("add"))
    def test_add_member(self, username, gender, phone_num):
        result = self.main.goto_contacts_page().goto_add_member().goto_edit_member_page().input_name(
            username
        ).set_gender(gender).input_phone(phone_num).save().get_add_result()
        assert result == "添加成功"
        self.main.back(num=1)

    @pytest.mark.parametrize('username',
                             yaml.safe_load(open('../../../datas/testdatas/appium.yml', encoding='UTF-8')).get("delete"))
    def test_delete_member(self, username):
        self.main.goto_contacts_page().goto_person_info(username).modefy_member().delete_member()
        WebDriverWait(self.main.driver, 15).until_not(lambda x: x.find_element_by_xpath(f"//*[@text='{username}']"))

    def teardown_class(self):
        self.app.close_app()
