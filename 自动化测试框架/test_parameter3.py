import pytest
import yaml

class Test_Demo():
    @pytest.mark.parametrize(["a","b","result"],yaml.safe_load(open("./data.yaml")))
    def test_case1(self, a, b, result):
        print("\n开始执行测试用例1")
        assert a + b == result