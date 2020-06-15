import pytest

from python_file.cal import Calculator


class TestPlugin:
    def setup(self):
        self.cal = Calculator()

    @pytest.mark.dependency(name='add')
    @pytest.mark.run(order=0)
    def test_add(self):
        print("加法")
        assert 2 == self.cal.add(1, 1)
        raise NameError

    @pytest.mark.dependency(depends=["add"])
    @pytest.mark.run(order=1)
    def test_sub(self):
        print("减法")
        assert 2 == self.cal.sub(4, 2)

    @pytest.mark.dependency(name='mul')
    @pytest.mark.run(order=2)
    def test_mul(self):
        print("乘法")
        assert 4 == self.cal.mul(2, 2)

    @pytest.mark.dependency(depends=["mul"])
    @pytest.mark.run(order=3)
    def test_div(self):
        print("除法")
        assert 3 == self.cal.div(6, 2)


if __name__ == '__main__':
    pytest.main()
