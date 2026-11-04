from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://forms.gle/REe8u7rxMjxBTssC7"

response = requests.get(ZILLOW_URL)
print(response.status_code)
content = response.text

soup = BeautifulSoup(content, "html.parser")

# Price of Property
prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
price_list = [price.getText().replace("/","+").split("+") for price in prices]
price = [amount[0] for amount in price_list]

# Address of Property
addresses = soup.find_all(name="address")
address_list = [address.getText().replace(",", "").replace(" |", "").strip() for address in addresses]

#Link of Property
links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
link_list = [link.get("href") for link in links]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get(FORM_URL)

for index in range(len(price)):
    sleep(0.1)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.click()
    address_input.send_keys(f"{address_list[index]}")
    sleep(0.2)
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.click()
    price_input.send_keys(f"{price[index]}")
    sleep(0.2)
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.click()
    link_input.send_keys(f"{link_list[index]}")
    sleep(0.2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))).click()
    sleep(0.5)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))).click()
    sleep(0.5)

driver.quit()