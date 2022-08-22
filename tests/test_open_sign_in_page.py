import allure
import pytest
from selene.support.conditions import be
from selene.support.shared.jquery_style import s
from selene.support.shared import browser


class TestOpenSigninPage:

    @allure.link("https://github.com", name="QA GURU 12 Lesson")
    @allure.label("owner", "uraniumcore238")
    @allure.severity('Blocker')
    @allure.story('Checking visibility signin page')
    @pytest.mark.parametrize('browser_size', [('1920', '1080'), ('1280', '720')], indirect=True)
    def test_open_signin_page_desktop(self, browser_management, browser_size):
        with allure.step('Open main page'):
            browser.open('')
        with allure.step('Click on signin button'):
            s(".HeaderMenu [href='/login']").click()
        with allure.step('Auth form header should be visible'):
            s(".auth-form-header").should(be.visible)

    @allure.link("https://github.com", name="QA GURU 12 Lesson")
    @allure.label("owner", "uraniumcore238")
    @allure.severity('Blocker')
    @allure.story('Checking visibility signin page')
    @pytest.mark.parametrize('browser_size', [('390', '844'), ('375', '667')], indirect=True)
    def test_open_signin_page_mobile(self, browser_management, browser_size):
        with allure.step('Open main page'):
            browser.open('')
        with allure.step('Click on navigation button'):
            s(".octicon-three-bars").click()
        with allure.step('Navigation menu should be visible'):
            s(".HeaderMenu").should(be.visible)
        with allure.step('Click on signin button'):
            s(".HeaderMenu [href='/login']").click()
        with allure.step('Auth form header should be visible'):
            s(".auth-form-header").should(be.visible)
