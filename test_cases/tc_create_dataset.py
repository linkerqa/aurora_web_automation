# -*- coding: utf-8 -*-

import time
import unittest
import yaml
from common.signin import SignIn


class CreateDataset(unittest.TestCase):

    def setUp(self):
        self.driver = SignIn()

    def test_create_dataset(self):
        driver = self.driver.sign_in()

        with open("../config/aurora_locator.yaml") as f:
            locator = yaml.load(f)
        with open("../config/test_data.yaml") as f:
            test_data = yaml.load(f)

        # create a new dataset
        driver.find_element_by_link_text(locator["dataset_tab_link_text"]).click()
        driver.find_element_by_link_text(locator["dataset_create_link_text"]).click()
        driver.find_element_by_id(locator["dataset_name_id"]).click()
        driver.find_element_by_id(locator["dataset_name_id"]).clear()
        driver.find_element_by_id(locator["dataset_name_id"]).send_keys(test_data["dataset_name1"])
        driver.find_element_by_id(locator["dataset_default_label_id"]).click()
        driver.find_element_by_id(locator["dataset_default_label_id"]).clear()
        driver.find_element_by_id(locator["dataset_default_label_id"]).send_keys(test_data["dataset_default_label"])
        driver.find_element_by_xpath(locator["dataset_save_xpath"]).click()
        time.sleep(2)

        # upload image1
        driver.find_element_by_xpath(locator["dataset_dropfile"]).send_keys(test_data["dataset_image_1"])
        time.sleep(10)
        # upload image2
        driver.find_element_by_xpath(locator["dataset_upload_button"]).click()
        driver.find_element_by_xpath(locator["dataset_dropfile"]).send_keys(test_data["dataset_image_2"])
        time.sleep(10)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
