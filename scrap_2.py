from flask import Flask, render_template, request, redirect
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.keys import Keys
import time
import uuid
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


chrome_driver_path = "C:\introduction\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument('--headless')

# Create a new instance of the Chrome driver
with webdriver.Chrome(service=service, options=options) as driver:

    try:
        url = 'https://www.maineprobate.net/search/'
        driver.get(url)
        time.sleep(5)
        # Find the dropdown element by its ID using the By class
        dropdown_element = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_ddlCounties')
        # Use the Select class to interact with the dropdown
        dropdown = Select(dropdown_element)

        # Select the option with value "York"
        dropdown.select_by_value('York')
        time.sleep(10)
        # Perform any additional actions if neede

        submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_btnSearch'))
        )
        case_input_element = driver.find_element(By.ID, 'ContentPlaceHolder1_tbCaseNumber')
        case_input_element.send_keys('2024')      
        submit_button.click()
        

    

    except Exception as e:
        print(f"An error occurred: {e}")
