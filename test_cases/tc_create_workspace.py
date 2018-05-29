import unittest
import yaml
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from common.signin import SignIn


class CreateWorkspace(unittest.TestCase):
    def setUp(self):
        self.driver = SignIn()

    def test_create_workspace(self):
        driver = self.driver.sign_in()

        with open("../config/aurora_locator.yaml") as f:
            locator = yaml.load(f)
        with open("../config/test_data.yaml") as f:
            test_data = yaml.load(f)

        # create a new workspace
        driver.find_element_by_link_text(locator["workspace_tab_link_text"]).click()
        driver.find_element_by_xpath(locator["workspace_create_xpath"]).click()
        driver.find_element_by_class_name(locator["workspace_name_class_name"]).click()
        driver.find_element_by_class_name(locator["workspace_name_class_name"]).clear()
        driver.find_element_by_class_name(locator["workspace_name_class_name"]).send_keys(test_data["workspace_name"])
        environment_select = Select(driver.find_element_by_class_name(locator["workspace_environment_select_class_name"]))
        environment_select.select_by_visible_text(test_data["workspace_environment"])
        driver.find_element_by_xpath(locator["workspace_save_xpath"]).click()
        workspace_create_check_locator = (By.XPATH, locator["workspace_create_check_xpath"])
        try:
            WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(workspace_create_check_locator))
        except TimeoutException:
            print("create workspace failed")
        else:
            print("create workspace successfully")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()


