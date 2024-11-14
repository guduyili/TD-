import pytest
from pytest import assume

def calc(a,b):
    return a+b

class TestDemo():
    def test_answer1(self):
        assert calc(1,1) ==2
    
    def test_answer2(self):
        #执行多种断言
        with assume: assert calc(2,1) ==4
        with assume: assert calc(2, 1)==3
        with assume: assert calc(2, 2)==3

    @pytest.mark.answer3
    def test_answer3(self):
        assert calc(6,6) ==12

if __name__ == '__main__':
    pytest.main()
    pytest.main(['-v', 'test2.py'])