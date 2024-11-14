import pytest

##函数级别

# def setup_function(self):
#     print("初始化执行。。。")

# def teardown_function(self):
#     print("清理执行。。。")
    
# def test_case1(self):
#         print("开始执行测试用例1")
#         assert 1 + 1 == 2

# def test_case2(self):
#         print("开始执行测试用例2")
#         assert 2 + 8 == 10

# def test_case3(self):
#         print("开始执行测试用例3")
#         assert 99 + 1 == 100

# #类型级别
# class Test_Demo():
#     def setup_class(self):
#         print("初始化。。。")

#     def teardown_class(self):
#         print("清理。。。")

#     def test_case1(self):
#         print("开始执行测试用例1")
#         assert 1 + 1 == 2

#     def test_case2(self):
#         print("开始执行测试用例2")
#         assert 2 + 8 == 10

#     def test_case3(self):
#         print("开始执行测试用例3")
#         assert 99 + 1 == 100

# #方法级别
# class Test_Demo():
#     def setup_method(self):
#         print("初始化。。。")

#     def teardown_method(self):
#         print("清理。。。")

#     def test_case1(self):
#         print("开始执行测试用例1")
#         assert 1 + 1 == 2

#     def test_case2(self):
#         print("开始执行测试用例2")
#         assert 2 + 8 == 10

#     def test_case3(self):
#         print("开始执行测试用例3")
#         assert 99 + 1 == 100

#模块级别
def setup_module():
    print("初始化。。。")

def teardown_module():
    print("清理。。。")

class Test_Demo():
    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("开始执行测试用例3")
        assert 99 + 1 == 100

if __name__ == '__main__':
      pytest.main()
