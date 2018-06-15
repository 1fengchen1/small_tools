from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

url = 'http://10.1.58.44/koss/KJAF2/html/frame/frame.htm'
driver.get(url)

driver.find_element_by_xpath('//*[@id="kui-10"]/div[2]/div[2]/div[6]').click()




