
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#create firefox window
driver = webdriver.Firefox()

#navgate to google.co.uk
driver.get("http://www.google.co.uk")

#find element by ID - lst-ib = google search box
elem = driver.find_element_by_id("lst-ib")

#type python in google search
elem.send_keys("python")

#press enter
elem.send_keys(Keys.RETURN)
assert "No Results Found" not in driver.page_source

#wait 600 seconds
driver.implicitly_wait(600)

#close browser
driver.close()
