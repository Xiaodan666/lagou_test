import yaml
import pytest

from python_file.cal import Calculator


class TestCal:
    def setup(self):
        self.cal = Calculator()

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../datas/cal.yml')).get("add"))
    def check_add(self, a, b, result):
        print("加法")
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../datas/cal.yml')).get("sub"))
    def check_sub(self, a, b, result):
        print("减法")
        assert result == self.cal.sub(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../datas/cal.yml')).get("mul"))
    def test_mul(self, a, b, result):
        print("乘法")
        assert result == self.cal.mul(a, b)

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../datas/cal.yml')).get("div"))
    def test_div(self, a, b, result):
        print("除法")
        assert result == self.cal.div(a, b)


if __name__ == '__main__':
    pytest.main()
