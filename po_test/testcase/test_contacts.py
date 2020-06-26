from po_test.page.contacts_page import ContactsPage
from po_test.page.home_page import HomePage


class TestContacts:

    def test_delete_member(self):
        """
        1.进入通讯录页面
        2.删除成员
        3.检查是否删除成功
        :return:
        """
        # 测试步骤
        HomePage().goto_add_member().add_member().delete_member("xiaodantest")
        # 断言zx
        assert "testxiaodan" not in ContactsPage().get_member_list()

    def test_import_contacts_from_home(self):
        """
        1.从首页点击导入通讯录--》进入导入通讯录页面
        2.点击导入文件
        3.检查导入是否成功
        :return:
        """
        # 操作步骤和断言
        assert "potest.xlsx" == HomePage().goto_import_contacts().import_contacts()
