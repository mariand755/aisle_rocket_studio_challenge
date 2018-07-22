from time import sleep
from environment import EnvironmentSetup
from page_object.gg_homepage_page import Homepage


class HomepageTest(EnvironmentSetup):

    def test_verify_if_object_exists(self):
        self.visit_page()

        homepage = Homepage(self.driver)
        self.assertTrue(homepage.get_mission().is_displayed(), True)
        self.write_to_console("Mission Statement is Displayed on Homepage")

    def test_current_deals(self):
        self.visit_page()

        homepage = Homepage(self.driver)
        homepage.all_current_deals()
        self.assertTrue(homepage.all_current_deals().is_displayed(), True)
        self.write_to_console("Promotions Tab Displayed on Homepage")
        self.assertTrue(homepage.deals().is_displayed(), True)
        self.write_to_console("Current Deals Displayed Confirmed")
        homepage.close_deals()
        self.write_to_console("Clicked to Close Current Deals View")


    def visit_page(self):
        self.driver.get("https://www.gladiatorgarageworks.com/")
        self.driver.set_page_load_timeout(20)

    def write_to_console(self, message):
        print(message)
        sleep(2)

# Use following code if you are going to run test case individually.
# if __name__ == '__main__':
#     unittest.main()
