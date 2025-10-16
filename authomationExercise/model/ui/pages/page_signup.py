import allure
from playwright.sync_api import Page, expect


class SignupPage:
    def __init__(self, page: Page):
        self.page = page

    def expect_form_title_visible(self, title_form: str):
        with allure.step(f"Проверка того, что форма '{title_form}' видна"):
            heading = self.page.get_by_role("heading", name=title_form, exact=True)
            expect(heading).to_be_visible()
