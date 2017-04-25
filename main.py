from selenium.webdriver.common.proxy import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#keep PhantomJs in home directory for no issues
driver = webdriver.PhantomJS()

driver.get("http://google.com")

driver.implicitly_wait(5)
time.sleep(5)

