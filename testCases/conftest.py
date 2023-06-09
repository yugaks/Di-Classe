import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
         driver=webdriver.Chrome(executable_path="C:\webdrivers.chromedriver.exe")
         return driver
    elif browser=="Edge":
        driver = webdriver.Edge(executable_path="C:\webdrivers.msedgedriver.exe")
    else:
        driver = webdriver.Chrome(executable_path="C:\webdrivers.chromedriver.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


####### Pytest html report #####
# It is hook for Adding Environmenet info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'ajay'

# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_matadata(matadata):
    matadata.pop("JAVA_HOME",None)
    matadata.pop("Plugins", None)


