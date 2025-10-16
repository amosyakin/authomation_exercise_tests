import allure
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_form = page.locator(".signup-form")
        self.input_signup_name = self.signup_form.locator('[data-qa="signup-name"]')
        self.input_signup_email = self.signup_form.locator('[data-qa="signup-email"]')
        self.button_signup = self.signup_form.locator('[data-qa="signup-button"]')

    def expect_form_title_visible(self, title_form: str):
        with allure.step(f"Проверка того, что форма '{title_form}' видна"):
            heading = self.page.get_by_role("heading", name=title_form, exact=True)
            expect(heading).to_be_visible()

    def fill_signup(self, name: str, email: str):
        with allure.step("Ввод name и email"):
            self.input_signup_name.fill(name)
            self.input_signup_email.fill(email)
            return self

    def click_signup_button(self):
        with allure.step("Нажать кнопку 'Signup'"):
            self.button_signup.click()
