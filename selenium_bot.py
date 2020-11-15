from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get("https://www.sleepfoundation.org/bedtimecalculator")

print(browser.title)
