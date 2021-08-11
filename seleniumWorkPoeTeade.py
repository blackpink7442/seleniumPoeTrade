import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.pathofexile.com/trade/search/Expedition')
time.sleep(2)
def choose():
    item = browser.find_element_by_xpath('//*[@id="trade"]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/span/div[2]').click()
    chose = browser.find_element_by_xpath('//*[@id="trade"]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/span/div[2]/div[3]/ul/li[24]').click()

def socket():
    socketField = browser.find_element_by_xpath('//*[@id="trade"]/div[4]/div/div[2]/div/div[1]/div[4]').click()
    sockets = browser.find_element_by_xpath('//*[@id="trade"]/div[4]/div/div[2]/div/div[1]/div[4]/div[2]/div[1]/span/input[5]')
    SocketsNumber = 6
    sockets.send_keys(SocketsNumber)

def link():
    linkMin = browser.find_element_by_xpath('//*[@id="trade"]/div[4]/div/div[2]/div/div[1]/div[4]/div[2]/div[2]/span/input[5]')
    linkMax = browser.find_element_by_xpath('//*[@id="trade"]/div[4]/div/div[2]/div/div[1]/div[4]/div[2]/div[2]/span/input[6]')
    linkMinNumber = 3
    linkMaxNumber = 3
    linkMin.send_keys(linkMinNumber)
    linkMax.send_keys(linkMaxNumber)

def chick():
    for i in range(1,10):
        count = 0
        for x in range(1,10):
            socket = ["socketLink socketLink0","socketLink socketLink1","socketLink socketLink3","socketLink socketLink4"]
            try:
                if(browser.find_element_by_xpath('//*[@id="trade"]/div[6]/div[2]/div['+str(i)+']/div[1]/div/div/div[1]/div/div['+str(x)+']').get_attribute("class") in socket):
                    count = count + 1
                    if(count == 4):   
                        floor = i
                        return floor
                        break
            except:
                break
         
                        


choose()
socket()
link()
button = browser.find_element_by_xpath('//*[@id="trade"]/div[4]/div/div[3]/div[2]/button').click()
time.sleep(4)
floor = chick()
name = browser.find_element_by_xpath('//*[@id="trade"]/div[6]/div[2]/div['+str(floor)+']/div[3]/div/div[2]/span').text
print(name)

