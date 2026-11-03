from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from dotenv import load_dotenv
import os 

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"
LOGIN_URL = f"{BASE_URL}/login"
SIMILAR_ACCOUNT = "chefsteps"
 
class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options = chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(BASE_URL)

    def login(self):
        sleep(0.5)
        self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(f"{USERNAME}")
        self.wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(f"{PASSWORD}", Keys.ENTER)
        sleep(0.5)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popup-save-login"]/div/div[2]'))).click()
       
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popup-notifications"]/div/button[2]'))).click()
        sleep(1)        

    def find_followers(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/button'))).click()
        sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/aside/div[2]/input'))).send_keys(SIMILAR_ACCOUNT)
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/aside/div[4]/a')))[0].click()
        # self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}")
        sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a'))).click()
        self.follower_count = int(self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a/b'))).text)
        
    
    def follow(self):
        scroll = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[3]')

        for _ in range(self.follower_count):
            follower_rows = self.driver.find_elements(By.XPATH, value='/html/body/div[2]/div/div[3]/div')
            for row in follower_rows:
                follow_btn = row.find_element(By.TAG_NAME, 'button')
                if follow_btn.text == 'Follow':
                    follow_btn.click()
                    sleep(0.2)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()