import pytest
import yaml


def pytest_addoption(parser, pluginmanager):
    mygroup = parser.getgroup("xiaodan")
    mygroup.addoption(
        "--env",
        default="test",
        dest="xiaodantest",
        help="choose your test env"
    )


@pytest.fixture(scope='session')
def cmdoption(request):
    datas = None
    myenv = request.config.getoption("--env", default="test")
    if myenv == "test":
        print("测试环境")
        with open("../datas/testdatas/test.yml") as f:
            datas = yaml.safe_load(f)
    elif myenv == "dev":
        print("开发环境")
        with open("../datas/testdatas/dev.yml") as f:
            datas = yaml.safe_load(f)
    elif myenv == "st":
        print("集成环境")
        with open("../datas/testdatas/st.yml") as f:
            datas = yaml.safe_load(f)
    return datas