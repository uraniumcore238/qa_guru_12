import allure
import pytest
from selene.support.conditions import be
from selene.support.shared.jquery_style import s
from selene.support.shared import browser


class TestOpenSigninPageDifFixture:

    @allure.link("https://github.com", name="QA GURU 12 Lesson")
    @allure.label("owner", "uraniumcore238")
    @allure.severity('Blocker')
    @allure.story('Checking visibility signin page')
    def test_open_signin_page_desktop_only(self, desktop_browser_management):
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
    def test_open_signin_page_mobile_only(self, mobile_browser_management):
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
