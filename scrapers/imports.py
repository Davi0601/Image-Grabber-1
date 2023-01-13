from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("enable-automation")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome("/home/davit/Desktop/Image-Grabber/scrapers/chromedriver")   # linux
