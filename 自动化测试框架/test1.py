import pytest


def calc(a,b):
    return a+b


class TestDemo():
    def test_answer1(self):
            assert calc(1,1) == 2
    def test_answer2(self):
            assert calc(2,1) == 4

            
    @pytest.mark.answer3
    def test_answer3(self):
            assert calc(114,514) == 628

if __name__ == '__main__':
      pytest.main()


