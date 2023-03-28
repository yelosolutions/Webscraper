from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(executable_path="C:/Users/Jay/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://www.selenium.dev/")

driver.quit()