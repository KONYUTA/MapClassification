import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

# File Name
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/image/"+"1"+".png")

# set driver and url
driver = webdriver.Chrome()
url = 'http://localhost:8080/map?x=36.151&y=36.151'
#driver.get(url)

# get width and height of the page
#w = driver.execute_script("return document.body.scrollWidth;")
#h = driver.execute_script("return document.body.scrollHeight;")

# set window size
#driver.set_window_size(w,h)
driver.set_window_size(900,900)
driver.get(url)
time.sleep(1)

# Get Screen Shot
#driver.save_screenshot(FILENAME)
png = driver.find_element_by_id('map').screenshot_as_png
with open('data/image/1.png', 'wb') as f:
        f.write(png)

# Close Web Browser
driver.quit()
