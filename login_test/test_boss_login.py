import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBoss:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.zhipin.com/")

    def test_get_boss_cookie(self):

        self.driver.find_element(By.CSS_SELECTOR, ".btns a:nth-child(5)").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".scan-login-btn")))
        self.driver.find_element(By.CSS_SELECTOR, ".scan-login-btn").click()
        sleep(10)
        cookies = self.driver.get_cookies()
        with open("../datas/boss.json", "w") as f:
            json.dump(cookies, f)

    def test_login_cookies(self):
        with open("../datas/boss.json") as f:
            cookies = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 20).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".nav-figure>a")))
            if res is not None:
                break
        sleep(3)

    def teardown(self):
        self.driver.quit()
