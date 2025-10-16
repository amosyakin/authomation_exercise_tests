import config
from authomationExercise.model.ui.pages.general_page import GeneralPage
from authomationExercise.model.ui.pages.header import Header
from authomationExercise.model.ui.pages.page_login import LoginPage
from authomationExercise.model.ui.pages.page_signup import SignupPage

BASE_URL = config.domain_url


def test_register_user(page):
    general_page = GeneralPage(page, base_url=BASE_URL)
    general_page.open().expect_open()

    header = Header(page)
    header.click_sign_in_login_button()

    login_page = LoginPage(page)
    login_page.expect_form_title_visible("New User Signup!")

    login_page.fill_signup(name="TestA_1610_2", email='testa_1610_2@mail.com')
    login_page.click_signup_button()

    signup_page = SignupPage(page)
    signup_page.expect_form_title_visible('Enter Account Information')
