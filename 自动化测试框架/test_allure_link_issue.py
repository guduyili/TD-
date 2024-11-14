# import allure

# @allure.link("http://www.baidu.com", name="baidu link")
# def test_with_link():
#     pass

# @allure.issue("140","this is a issue")
# def test_with_issue_link():
#     pass

# TEST_CASE_LINK = 'https://github.com'
# @allure.testcase(TEST_CASE_LINK, 'Test case title')
# def test_with_testcase_link():
#     pass


#关联bug需要在用例执行时添加参数：

#--allure-link-pattern=issue:[bug地址]{}

#例如：--allure-link-pattern=issue:http://www.bugfree.com/issue/{}

import allure

@allure.link("http://www.baidu.com",name="baidu link")
def test_with_link():
    pass

@allure.issue("140","this is a issue")
def test_with_issue_link():
    pass

TEST_CASE_LINK = 'https://github.com'
@allure.testcase(TEST_CASE_LINK,'Test case title')
def test_with_testcase_link():
    pass

