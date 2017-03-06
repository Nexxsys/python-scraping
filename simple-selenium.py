from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

#binary = FirefoxBinary('webdriver/geckodriver')
#driver = webdriver.Firefox(firefox_binary=binary)
driver = webdriver.Firefox()
driver.get("http://www.python.org")
driver.close()
