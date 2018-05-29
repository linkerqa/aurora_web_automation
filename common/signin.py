import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class SignIn(object):

    def sign_in(self):

        # Use disk cache to load large size of .bundle.js
        option = webdriver.ChromeOptions()
        prefs = {'disk-cache-size': 40960}
        option.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=option)
        base_url = "https://aurora-staging.linkernetworks.co/"
        driver.get(base_url + "signin.html#/")
        driver.maximize_window()
        driver.refresh()
        driver.refresh()

        with open("../config/aurora_locator.yaml") as f:
            locator = yaml.load(f)
        with open("../config/test_data.yaml") as f:
            test_data = yaml.load(f)

        email = (By.ID, locator["signin_email_id"])
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(email))
        except NoSuchElementException as e:
            print (e)

        driver.find_element_by_id(locator["signin_email_id"]).clear()
        driver.find_element_by_id(locator["signin_email_id"]).send_keys(test_data["email"])
        driver.find_element_by_xpath(locator["signin_submit_xpath"]).click()
        time.sleep(2)
        driver.find_element_by_id(locator["signin_password_id"]).clear()
        driver.find_element_by_id(locator["signin_password_id"]).send_keys(test_data["password"])
        driver.find_element_by_xpath(locator["signin_submit_xpath"]).click()

        check_element = (By.XPATH, locator["signin_checkelement_xpath"])
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(check_element))
        except NoSuchElementException as e:
            print (e)
        else:
            print ("Sign in successfully.")

        return driver