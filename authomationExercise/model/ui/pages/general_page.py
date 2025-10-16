import re

import allure
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from authomationExercise.model.ui.pages.header import Header


class GeneralPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self, path: str = '/'):
        with allure.step('Переход на главную страницу'):
            self.page.goto(self.base_url + path, wait_until='domcontentloaded')
            return self

    def expect_open(self):
        with allure.step('Проверка, что главная страница успешно открылась'):
            expect(self.page).to_have_url(re.compile(r"^" + re.escape(self.base_url) + r"/?$"))
            Header(self.page).expect_link_active(link_name="Home")
