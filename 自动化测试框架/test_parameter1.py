import pytest
import allure

class Test_Deno():
    @pytest.mark.parametrize("a,b,result",[(1,1,2),(114,514,628)])
    def test_case1(self,a,b,result):
        print("\n开始执行测试用例1")
        assert a+b == result