from selenium import webdriver
from time import sleep
from logindetails import email, password
from selenium.webdriver.common.keys import Keys


class Tinderlikebot():
    def __init__(self):
        self.driver = webdriver.Chrome()



    def open_tinder(self):
        self.driver.get('https://tinder.com')
# Opens the tinder website

        sleep(2)

        login = self.driver.find_element('xpath',
                                         '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login.click()
# Fetches the login button code in order to execute an automated click action on button.

        sleep(1)
        self.fb_login()


        sleep(6)
        try:
            allow_location = self.driver.find_element('xpath',
                                                      '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
            allow_location.click()
        except:
            print("No location popup")

        sleep(2)
# looks out for any notiication pop up
        try:
            noti = self.driver.find_element('xpath',
                                            '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
            noti.click()
        except:
            print("no notfications")

        sleep(4)

        try:
            while True:
                sleep(1) #you can modify sleep timer to your likings.
                like = self.driver.find_element('xpath',
                                                '/html/body')
                like.send_keys(Keys.ARROW_RIGHT)
                # spams the like button until you stop the program or it reaches the max limit of likes per day
        except:
            print("Test")

    def fb_login(self):
        login_fb = self.driver.find_element('xpath',
                                            '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
        login_fb.click()

        sleep(2)
        main_window = self.driver.window_handles[0]
        fb_pop = self.driver.window_handles[1]

        self.driver.switch_to.window(fb_pop)

        cookies_window = self.driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]')
        cookies_window.click()


# input email and password from the logindetails.py file.
        email_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        password_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        login_btn = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_btn.click()
        self.driver.switch_to.window(main_window)


bot = Tinderlikebot()
bot.open_tinder()

while True:
    pass
open_tinder()
