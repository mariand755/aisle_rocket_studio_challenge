from selenium.webdriver.common.by import By


class LandingPage(object):
    def __init__(self, driver):
        self.driver = driver

        # page locators
        mission_statement = "//h5[contains(text(),'See it for yourself at The Home Depot.')]"
        xpath_durable_icon = "//span[@class='swiper-pagination-bullet slide-1']"
        xpath_durable_text = "//h4[contains(text(),'Quartz is one of nature’s hardest minerals and nat')]"
        xpath_close_view = "/html[1]/body[1]/section[3]/div[2]/a[1]"

        self.mission = driver.find_element(By.XPATH, mission_statement)
        self.durable_link = driver.find_element(By.XPATH, xpath_durable_icon)
        self.durable_confirm_text = driver.find_element(By.XPATH, xpath_durable_text)
        self.close_button = driver.find_element(By.XPATH, xpath_close_view)

    def get_mission(self):
        return self.mission

    def durable_button(self):
        self.durable_link.click()

    def confirm_durable_text(self):
        return self.durable_confirm_text

    def close_durable(self):
        self.close_button.click()
