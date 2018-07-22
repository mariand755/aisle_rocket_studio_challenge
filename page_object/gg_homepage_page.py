from selenium.webdriver.common.by import By


class Homepage(object):
    def __init__(self, driver):
        self.driver = driver

        # page locators
        mission_statement = "//p[contains(text(),'When your gear is within reach, your passions are,')]"
        xpath_current_deals = "//div[@id='promotion-header']"
        xpath_all_deals = "//div[@class='swiper-wrapper']"

        self.mission = driver.find_element(By.XPATH, mission_statement)
        self.current_deals = driver.find_element(By.XPATH, xpath_current_deals)
        self.deals_displayed = driver.find_element(By.XPATH, xpath_all_deals)

    def get_mission(self):
        return self.mission

    def all_current_deals(self):
        return self.current_deals

    def deals(self):
        return self.deals_displayed

    def close_deals(self):
        return self.current_deals.click()
