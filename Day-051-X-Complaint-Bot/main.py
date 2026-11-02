from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

PROMISED_UP = 1000
PROMISED_DOWN = 1000
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        privacy_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        privacy_button.click()
        sleep(3)
        go_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')))
        go_button.click()
        sleep(60)
        self.down = self.driver.find_element(
        By.XPATH,
        value='//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/h3'        ).text

        self.up = self.driver.find_element(
        By.XPATH,
        value='//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/h3'
        ).text

        print(f"Download Speed: {self.down} Mbps")
        print(f"Upload Speed: {self.up} Mbps")

        

    def twitter_at_provider(self):
        
        sleep(1)
        self.driver.get(LOGIN_URL)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.y-login-card #email'))).send_keys(LOGIN_EMAIL)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.y-login-card #password'))).send_keys(LOGIN_PASSWORD, Keys.ENTER)
        if float(self.down) < float(PROMISED_DOWN) and float(self.up) < float(PROMISED_UP) or float(self.down) < float(PROMISED_DOWN) or float(self.up) < float(PROMISED_UP):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tweet-compose"]'))).send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
            self.wait.until(EC.element_to_be_clickable((By.ID, 'post-btn'))).click()
        else:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tweet-compose"]'))).send_keys(f"Hey Internet Provider, the internet is working properly.")
            self.wait.until(EC.element_to_be_clickable((By.ID, 'post-btn'))).click()
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.twitter_at_provider()
# //*[@id="onetrust-accept-btn-handler"]