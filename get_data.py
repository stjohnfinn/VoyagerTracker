from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import webbrowser
from bs4 import BeautifulSoup
import time

is_metric = True

def get_data():

    print("updating data...")
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(PATH, options = chrome_options)
    driver.get("https://voyager.jpl.nasa.gov/mission/status/")

    if is_metric:
        driver.find_element_by_class_name("slider").click()

    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "lxml")

    # driver.close()

    return soup
