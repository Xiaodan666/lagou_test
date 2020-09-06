import os

from baidu_test.page.home_page import HomePage


class TestSearchResult():
    def setup(self):
        self.home_page = HomePage()



    def test_search1(self):
        assert "今日头条" in self.home_page.go_to_search_details_page("今日头条").check_title()

    def test_search2(self):
        assert "王者荣耀" in self.home_page.go_to_search_details_page("王者荣耀").check_title()

    def teardown(self):
        self.home_page.quit()
