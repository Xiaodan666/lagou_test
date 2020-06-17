import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    def test_get_cookie(self):
        sleep(10)
        cookies = self.driver.get_cookies()
        with open("../datas/cookies.json", "w") as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        with open("../datas/cookies.json") as f:
            cookies = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.CLASS_NAME, "frame_nav_item_title")))
            if res is not None:
                break
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "js_upload_file_input")))
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("G:\Code\lagou_test.xlsx")

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "upload_file_name")))
        act_value = self.driver.find_element(By.ID, "upload_file_name").text

        assert act_value == "lagou_test.xlsx"

    def teardown(self):
        self.driver.quit()
