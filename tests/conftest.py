import os
import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(390, 844), (375, 667), (1920, 1080), (1024, 768)])
def browser_size(request):
    return request


@pytest.fixture(scope='function')
def browser_management(browser_size):
    browser.config.window_width = browser_size.param[0]
    browser.config.window_height = browser_size.param[1]
    browser.config.base_url = os.getenv('selene.base_url', 'https://github.com/')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    yield
    browser.close()
    browser.quit()


@pytest.fixture(scope='function', params=[(1920, 1080), (1024, 768)])
def desktop_browser_management(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.config.base_url = os.getenv('selene.base_url', 'https://github.com/')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    yield
    browser.close()
    browser.quit()


@pytest.fixture(scope='function', params=[(390, 844), (375, 667)])
def mobile_browser_management(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.config.base_url = os.getenv('selene.base_url', 'https://github.com/')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    yield
    browser.close()
    browser.quit()
