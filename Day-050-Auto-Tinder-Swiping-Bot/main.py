from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10) 
driver.get("https://app.100daysofpython.dev/services/tindog/u/t8rX1-49TbelrJWES5ts3a9snwFbTC20")

sleep(2)
driver.find_element(By.CLASS_NAME, value="btn-tindog-login").click()
sleep(1)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-facebark"))).click()

wait.until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[-1])

wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("alishamarinadsouza@gmail.com", Keys.ENTER)
driver.find_element(By.ID, value="pass").send_keys("alishamarinadsz@692005", Keys.ENTER)

wait.until(EC.number_of_windows_to_be(1))
driver.switch_to.window(driver.window_handles[-1])

sleep(1)
driver.find_element(By.CLASS_NAME, value="btn-primary").click()
sleep(1)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-secondary"))).click()
sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/form/button'))).click()

for n in range(20):
    sleep(1)
    try:
        driver.find_element(By.CLASS_NAME, value = "btn-like").click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value = ".match-popup a").click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        sleep(2)

driver.quit()