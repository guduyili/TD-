import pytest
import allure

data = [(1,1,2),
        (2,8,10),
        (19,19,810)
        ]

class Test_Deno():
    @pytest.mark.parametrize("a,b,result",data)
    def test_case1(self,a,b,result):
        print("\n开始执行测试用例1")
        assert a+b == result
if __name__ == '__main__':
    pytest.main()

