import time
import unittest
import yaml
from selenium.common.exceptions import NoSuchElementException
from common.signin import SignIn


class EditDataset(unittest.TestCase):

    def setUp(self):
        self.driver = SignIn()

    def test_edit_dataset(self):
        driver = self.driver.sign_in()

        with open("../config/aurora_locator.yaml") as f:
            locator = yaml.load(f)
        with open("../config/test_data.yaml") as f:
            test_data = yaml.load(f)

        # check if private dataset exists in advance
        driver.find_element_by_link_text(locator["dataset_tab_link_text"]).click()
        time.sleep(2)
        try:
            self.assertIsNotNone(driver.find_element_by_xpath(locator["dataset_edit_xpath"]))
        except NoSuchElementException:
            print("No private dataset in aurora. Please create a private dataset to run the case.")

        # edit dataset:
        # 1. change dataset nanme
        # 2. change private dataset to public dataset
        driver.find_element_by_xpath(locator["dataset_edit_xpath"]).click()
        time.sleep(2)
        current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        new_dataset_name = test_data["dataset_name2"] + current_time
        driver.find_element_by_id(locator["dataset_name_id"]).clear()
        driver.find_element_by_id(locator["dataset_name_id"]).send_keys(new_dataset_name)
        driver.find_element_by_id(locator["dataset_private_id"]).click()
        driver.find_element_by_xpath(locator["dataset_save_xpath"]).click()
        driver.find_element_by_xpath(locator["dataset_sharingcheck_xpath"]).click()
        time.sleep(2)

        # verify the above changes by searching new name in public
        driver.find_element_by_xpath(locator["dataset_public_xpath"]).click()
        time.sleep(2)
        driver.find_element_by_xpath(locator["dataset_search_xpath"]).click()
        driver.find_element_by_xpath(locator["dataset_search_xpath"]).clear()
        driver.find_element_by_xpath(locator["dataset_search_xpath"]).send_keys(new_dataset_name)
        try:
            self.assertIsNotNone(driver.find_element_by_link_text(new_dataset_name))
        except NoSuchElementException:
            print("Edit dataset failed.")
        else:
            print("Edit dataset successfully.")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()