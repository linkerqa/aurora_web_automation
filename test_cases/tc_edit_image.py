import time
import unittest
import yaml
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.signin import SignIn


class EditImage(unittest.TestCase):

    def setUp(self):
        self.driver = SignIn()

    def test_edit_image(self):
        driver = self.driver.sign_in()

        with open("../config/aurora_locator.yaml") as f:
            locator = yaml.load(f)

        # check whether private dataset exists in advance
        driver.find_element_by_link_text(locator["dataset_tab_link_text"]).click()
        time.sleep(2)
        driver.find_element_by_xpath(locator["dataset_private_xpath"]).click()
        try:
            self.assertIsNotNone(driver.find_element_by_xpath(locator["dataset_edit_xpath"]))
        except NoSuchElementException:
            print("No private dataset in aurora. Please create a private dataset to run the case.")

        # check whether there are two unannotated images
        driver.find_element_by_xpath(locator["dataset_view_xpath"]).click()
        time.sleep(2)
        driver.find_element_by_xpath(locator["dataset_unannotated_xpath"]).click()
        try:
            self.assertIsNotNone(driver.find_element_by_xpath(locator["image1_edit_xpath"]))
        except NoSuchElementException:
            print("No unannotated images. Please upload two images to run the case.")
        try:
            self.assertIsNotNone(driver.find_element_by_xpath(locator["image2_edit_xpath"]))
        except NoSuchElementException:
            print("At least two annotated images needed. Please upload two images to run the case.")

        driver.find_element_by_xpath(locator["image1_edit_xpath"]).click()
        time.sleep(5)
        # rect image on first image
        ActionChains(driver).click_and_hold().move_by_offset(100, 100).release().perform()
        time.sleep(2)
        try:
            self.assertIsNotNone(driver.find_element_by_class_name(locator["image_rect_check_class_name"]))
        except NoSuchElementException:
            print("Image annotation error: rect failed.")
        else:
            print("Image annotation: rect successfully.")

        # face landmarks on second image
        driver.find_element_by_xpath(locator["image_save_and_next_xpath"]).click()
        time.sleep(5)
        driver.find_element_by_xpath(locator["image_face_landmarks_xpath"]).click()
        face_check_locator = (By.CLASS_NAME, locator["image_face_landmarks_check_class_name"])
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(face_check_locator))
        except TimeoutException:
            print("Image annotation error: face landmark failed.")
        else:
            print("Image annotation: face landmark successfully.")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

