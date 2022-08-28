import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

print('地図の収集をはじめます(´･ω･`)\n')
index = 1
with open('../data/jinshin_zahyou_short.csv') as f_in:
    for line in f_in:
        coord = line.split(',')
        # File Name
        FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/image/"+str(index)+".png")

        #オプションの設定
        options = Options()
        options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        options.add_argument('--headless')

        # set driver and url
        driver = webdriver.Chrome(options=options)
        url = 'http://localhost:8080/map?x='+coord[0]+'&y='+coord[1]

        # get width and height of the page
        #w = driver.execute_script("return document.body.scrollWidth;")
        #h = driver.execute_script("return document.body.scrollHeight;")
        #driver.set_window_size(w,h)

        # set window size
        driver.set_window_size(900,900)
        driver.get(url)
        time.sleep(3)

        # Get Screen Shot
        png = driver.find_element_by_id('map').screenshot_as_png
        with open('../data/image/'+str(index)+'.png', 'wb') as f:
                f.write(png)

        driver.quit()
        print(str(index)+'番目の地点周辺マップを保存しましたよ(´・ω・)')
        index+=1
print('(´・ω・)(´･ω･`)(´・ω・)(´・ω・)'\n終わりますよ(´・ω・)')
