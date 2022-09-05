from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Index_page(Base):
    """Главная страница интернет-магазина"""
    url = 'http://automationpractice.com/index.php'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""
    dresses_link = '//*[@id="block_top_menu"]/ul/li[2]/a'
    main_word = '//*[@id="center_column"]/h1/span[1]'  # Dresses

    """GETTERS"""

    def get_dresses_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dresses_link)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    """ACTIONS"""

    def click_dresses_link(self):
        self.get_dresses_link().click()
        print("Click dresses link")

    """METHODS"""

    def go_to_dresses(self):
        """Переход с главной страницы на вкладку Dresses для выбора товара по фильтрам"""
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_dresses_link()
