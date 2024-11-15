import pytest
import allure

def test_attach_text():
    allure.attach("纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>显示一块HTNL的body块</body>","HTML页面",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("test.jpg",attachment_type=allure.attachment_type.JPG)



# allure.attach()¶
# 可以在报告中附加文本、图片以及html网页，用来补充测试步骤或测试结果，比如错误截图或者关键步骤的截图。