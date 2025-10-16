import allure
from playwright.sync_api import Page, expect


class Header:

    def __init__(self, page: Page):
        self.page = page
        self.navigator_bar = page.locator("header .navbar-nav")
        self.signup_login_button = page.locator("a[href='/login']")

    def link_by_name(self, link_name: str):
        return self.navigator_bar.get_by_role('link', name=link_name)

    def expect_link_active(self, link_name: str = "Home"):
        with allure.step(f"Проверка, что ссылка '{link_name}' выделена оранжевым"):
            link = self.link_by_name(link_name)
            expect(link).to_be_visible()
            color = link.evaluate("el => getComputedStyle(el).color")
            assert color in ("rgb(255, 165, 0)", "rgba(255, 165, 0, 1)", "orange"), \
                f"Ссылка {link} не выделена оранжевым! Выделена {color}"

    def click_sign_in_login_button(self):
        with allure.step("Нажать кнопку 'SignUp / Login'"):
            return self.signup_login_button.click()
