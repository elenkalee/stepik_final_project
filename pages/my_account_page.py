from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class NAME_page(Base):
    url = 'http://automationpractice.com/index.php'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""
    item_1 = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]'

    """GETTERS"""

    def get_item_1_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_1)))

    """ACTIONS"""

    def click_item_1_link(self):
        self.get_item_1_link().click()
        print("Click item_1 link")

    """METHODS"""

    def open_item_1_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_item_1_link()
