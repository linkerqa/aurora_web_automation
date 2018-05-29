import time
import unittest
import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from common.signin import SignIn


class EditWorkspace(unittest.TestCase):
    def setUp(self):
        self.driver = SignIn()

    def test_edit_workspace(self):
        driver = self.driver.sign_in()

        with open("../config/aurora_locator.yaml") as f:
            locator = yaml.load(f)
        with open("../config/test_data.yaml") as f:
            test_data = yaml.load(f)

        # go back to workspace page & view the first workspace
        driver.find_element_by_link_text(locator["workspace_tab_link_text"]).click()
        time.sleep(2)
        driver.find_element_by_link_text(locator["workspace_view_detail_link_text"]).click()
        time.sleep(5)

        # import dataset
        driver.find_element_by_xpath(locator["workspace_import_dataset_xpath"]).click()
        first_dataset_locator = (By.XPATH, locator["workspace_first_dataset_xpath"])
        WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(first_dataset_locator))
        dataset_name = driver.find_element_by_xpath(locator["workspace_first_dataset_xpath"]).text
        driver.find_element_by_xpath(locator["workspace_first_dataset_xpath"]).click()
        driver.find_element_by_xpath(locator["workspace_add_button_xpath"]).click()

        add_dataset_check_locator = (By.LINK_TEXT, dataset_name)
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(add_dataset_check_locator))
        except TimeoutException:
            print("import dataset failed")
        else:
            print("import dataset successfully")

        # mount volume
        driver.find_element_by_xpath(locator["workspace_mount_volume_xpath"]).click()
        driver.find_element_by_xpath(locator["workspace_search_volume_xpath"]).send_keys(test_data["volume_name"])
        time.sleep(2)
        driver.find_element_by_xpath(locator["workspace_first_volume_xpath"]).click()

        #

    def tearDown(self):
            pass


if __name__ == "__main__":
    unittest.main()