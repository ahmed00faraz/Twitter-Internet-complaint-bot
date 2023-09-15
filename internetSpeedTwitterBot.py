from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

PROMISED_UP = 30
PROMISED_DOWN = 30
TWITTER_EMAIL = "YOUREMAIL@gmail.com"
TWITTER_PASSWORD = "PASSWORD"
TWITTER_LOGIN_PAGE = "https://twitter.com/i/flow/login"
SPEED_TEST_PAGE = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.UP = 0
        self.DOWN = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_PAGE)
        sleep(5)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        sleep(2)
        start = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start.click()
        sleep(45)
        speeds = self.driver.find_elements(By.CLASS_NAME, "result-data-large")
        self.UP, self.DOWN = speeds[0].text, speeds[1].text
        return self.UP, self.DOWN

    def tweet_at_provider(self):
        message = (f"Hey Internet Provider , why is my Internet speed {self.DOWN}down/{self.UP}up "
                   f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up")
        self.driver.get(TWITTER_LOGIN_PAGE)
        sleep(10)
        email_label = self.driver.find_element(By.TAG_NAME, "input")
        email_label.send_keys(TWITTER_EMAIL)
        email_label.send_keys(Keys.ENTER)
        sleep(10)
        password_label = self.driver.find_element(By.NAME, "password")
        password_label.send_keys(TWITTER_PASSWORD)
        password_label.send_keys(Keys.ENTER)
        sleep(10)
        try:
            tweet_box = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']")
            tweet_box.click()
            tweet_box.send_keys(message)
        except NoSuchElementException:
            sleep(20)
        post_button = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='tweetButtonInline']")
        post_button.click()
        sleep(20)


bot = InternetSpeedTwitterBot()
print(bot.get_internet_speed())
if bot.UP < PROMISED_UP or bot.DOWN < PROMISED_DOWN:
    bot.tweet_at_provider()
