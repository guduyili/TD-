import pytest
import allure

#@allure.feature(‘功能名称’)：相当于 testsuite
@allure.feature("登录")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("登录成功")
        pass

     #@allure.story(’子功能名称‘)：对应这个功能或者模块下的不同场景，相当于 testcase
    @allure.story("密码错误")
    def test_login_failure(self):
        #@allure.step('步骤')：测试过程中的每个步骤，放在具体逻辑方法中
            #allure.step('步骤') 只能以装饰器的形式放在类或者方法上面
            #with allure.step：可以放在测试用例方法里面
        with allure.step("输入用户名"):
            print("输入用户名")
        with allure.step("输入密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("登陆失败"):
            assert '1' == 1
            print("登陆失败")
        pass
    
    @allure.story("用户名密码错误!")
    def test_login_failure_a(self):
        print("用户名密码错误!登录失败")
        pass


@allure.feature("注册")
class TestRegister():
    @allure.story("注册成功")
    def test_register_success(self):
        print("测试用例：注册成功")
        pass

    @allure.story("注册失败")
    def test_register_failure(self):
        with allure.step("输入用户名"):
            print("输入用户名")
        with allure.step("输入密码"):
            print("输入密码")
        with allure.step("再次输入密码"):
            print("再次输入密码")
        print("点击注册")
        with allure.step("注册失败"):
            assert 1+1 == 2
            print("注册失败")
        pass
    
# @allure.attach('具体文本信息')
# 附加信息：数据，文本，图片，视频，网页