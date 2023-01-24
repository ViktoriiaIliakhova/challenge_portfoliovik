from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    remind_pass_btn_xpath = "//*[text()='Remind password']"
    language_select_listbox = "//div [@role='button']"	

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
