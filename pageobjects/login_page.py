from framework.base_page import BasePage


class LoginPage(BasePage):
    input_box_user = "xpath=>//*[@id='app']/div/div[2]/div[3]/div/div[1]/input"
    input_box_paswd = "xpath=>//*[@id='app']/div/div[2]/div[3]/div/div[2]/input"
    login_button = "xpath=>//*[@id='app']/div/div[2]/div[3]/div/button"
    Base = "xpath=>//*[@id='app']/div/div[2]/div[1]/div/div/div[2]/div[1]/span[1]"
    Role = "xpath=>//*[@id='app']/div/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/a/span"
    insert = "xpath=//*[@id='role']/div[1]/div/div[3]/div/button/span"

    # app > div > div.al-main > div.alm-form-wrap > div > button
    def type_search_user(self, text):
        self.type(self.input_box_user, text)

    def type_search_paswd(self, text):
        self.type(self.input_box_paswd, text)

    def click_button(self):
        self.click(self.login_button)
        self.sleep(2)

    def baedata(self):
        self.click(self.Base)
        self.click(self.Role)
        self.sleep(2)

    def switch(self):
        self.switch_to_frame("http://bus.123cx.com")
        print("切换框架")
        self.click(self.insert)


