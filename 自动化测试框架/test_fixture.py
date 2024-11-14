#fixture 作用范围：Scope¶
#fixture 作用范围可以为module、class、session和function，默认作用域为function。

# #function：每一个函数或方法都会调用

# #class：每一个类调用一次

# #module：每一个.py文件调用一次

# #session：是多个文件调用一次

# #fixture自动应用¶
# #autouse参数¶

# import pytest

# @pytest.fixture(autouse=True)
# def login():
#     print("登录")
#     return 8
# class Test_Demo():
#     def test_case1(self):
#         print("\n开始执行测试用例1")
    
#     def test_case2(self,login):
#         print("\n开始执行测试用例2")
    
#     def test_case3(self):
#         print("\n开始执行测试用例3")
#         assert 99+1 ==100

# if __name__ ==  '__main__':
#     pytest.main()

# #使用yert
# #使用yield关键字可以实现setup/teardown的功能，在yield关键字之前的代码在case之前执行，
# # yield之后的代码在case运行结束后执行
# import pytest

# @pytest.fixture()
# def login():
#     print("登录")
#     yield
#     print("退出登录")

# class Test_Demo():
#     def test_case1(self):
#         print("\n开始执行测试用例1")
#         assert 1 + 1 == 2

#     def test_case2(self, login):
#         print("\n开始执行测试用例2")
#         assert 2 + 8 == 10

#     def test_case3(self):
#         print("\n开始执行测试用例3")
#         assert 99 + 1 == 100


# if __name__ == '__main__':
#     pytest.main()
    


#addfinalizer方法¶
#addfinalizer也可以实现环境的清理，实现与yield方法相同的效果，跟yield不同的是需要注册作为终结器使用的函数。




import pytest

@pytest.fixture(scope="module", params=[
    [1, 1, 2],
    [2, 8, 10],
    [99, 1, 100]
])
def data(request):
    yield request.param

class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 2 + 8 == 10

    def test_case2(self, data):
        print("\n开始执行测试用例2")
        assert data[0] + data[1] == data[2]

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()