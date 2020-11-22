from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
browser.get("https://www.sleepfoundation.org/bedtimecalculator")

print(browser.title)

# select dropdown menu
sleep_amount = Select(browser.find_element_by_id('bedtime-hours-number'))
# select by visible text
sleep_amount.select_by_visible_text('7 hours')

awake_hour = Select(browser.find_element_by_class_name('bedtime-hour'))
awake_hour.select_by_visible_text('9')

awake_minute = Select(browser.find_element_by_class_name('bedtime-minute'))
awake_minute.select_by_visible_text('30')

calculate = browser.find_element_by_id("b-w")
calculate.click()

# this is to ensure the page is loaded
time.sleep(5)
# this renders the JS code and stores
# all of the info in static html code
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')
wake_up_time = soup.find_all('span', class_='bedtime-number')[0].text

print(f"""
!!!!!!!!!!!!!!!!!!!!
!!!{wake_up_time}!!!
!!!!!!!!!!!!!!!!!!!!
""")

