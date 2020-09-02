import json
from time import sleep

import xlwt as xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By

#  将数据写入新文件
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet

    # 将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i, j, data[j])
        i = i + 1

    f.save(file_path)  # 保存文件


def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, "w")
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


class TestGetAudio:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.tuke88.com/peiyue/o1010/zonghe_0_1.html")
        # sleep(5)

    def test_get_cookie(self):
        sleep(10)
        cookies = self.driver.get_cookies()
        with open("audio_cookies.json", "w") as f:
            json.dump(cookies, f)

    def test_1(self):
        with open("audio_cookies.json") as f:
            cookies = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.CLASS_NAME, "auser")))
            if res is not None:
                break
        titles = []
        audios = []
        for i in range(2):
            title_elements = self.driver.find_elements(By.XPATH, "//div[@class='cbox audio-box']//a[1]")
            audio_elements = self.driver.find_elements(By.XPATH, "//div[@class='cbox audio-box']//source")
            for i in title_elements:
                titles.append(i.text)

            for j in audio_elements:
                audios.append(j.get_attribute("src"))
            self.driver.find_element(By.XPATH, "//a[contains(text(),'下一页')]").click()
        text_save("audios.txt", audios)
        text_save("title.txt", titles)

    def teardown(self):
        self.driver.quit()
