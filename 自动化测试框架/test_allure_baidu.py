import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        options = Options()
        service = Service("C:/Testing_tools/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("http://www.baidu.com")

    with allure.step("搜索关键词"):
        driver.find_element(By.ID, "kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element(By.ID, "su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        screenshot_path = "./result/b.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body>首页</body>', 'Attach with HTML type', allure.attachment_type.HTML)

    with allure.step("退出浏览器"):
        driver.quit()
