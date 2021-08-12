from selenium import webdriver 
import time

def job():
    while 1:
        time.sleep(0.005)
        app.click()
        
driver = webdriver.Chrome('your chrome driver path')
url = 'https://popcat.click/'
driver.get(url)
app = driver.find_element_by_id('app')
job()




