import time
from Screenshot import Screenshot_Clipping

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

options = Options()
#options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('--headless')

ob=Screenshot_Clipping.Screenshot()

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.google.co.jp/')

ob.full_Screenshot(driver, save_path=r'.', image_name='gazou.png')

driver.close()
driver.quit()
