from time import sleep
from environment import EnvironmentSetup
from page_object.cs_landingpage_page import LandingPage


class LandingPageTest(EnvironmentSetup):

    def test_verify_if_object_exists(self):
        # Opens the webpage in Chrome
        self.visit_page()
        # initialize landing page
        landingpage = LandingPage(self.driver)
        # verifies the mission statement is displayed on page
        self.assertTrue(landingpage.get_mission().is_displayed(), True)
        # print to the console
        self.write_to_console("Mission Statement for Landing Page is Displayed")

    def test_open_close_durable_button(self):
        # Opens the webpage in Chrome
        self.visit_page()
        # initialize landing page
        landingpage = LandingPage(self.driver)
        # click on the durable icon to open dialogue box
        landingpage.durable_button()
        # print to console
        self.write_to_console("Clicked on Durable Icon")
        # verifies content text displayed on durable dialogue box
        self.assertTrue(landingpage.confirm_durable_text().is_displayed(), True)
        # print to console
        self.write_to_console("Display text on Durable Popup confirmed")
        # close durable dialogue box
        landingpage.close_durable()
        # print to console
        self.write_to_console("Clicked on Durable Close Button")

    def visit_page(self):
        # Opens the webpage in Chrome
        self.driver.get("https://www.seecaesarstonequartz.com/")
        # wait time for page to load
        self.driver.set_page_load_timeout(20)

    def write_to_console(self, message):
        # print text to console
        print(message)
        sleep(2)

# Use following code if you are going to run test case individually.
# if __name__ == '__main__':
#     unittest.main()
