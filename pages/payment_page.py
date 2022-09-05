from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Payment_page(Base):
    """Страница Payment, выбор способа платежа, переход на страницу с типом платежа"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""
    pay_by_bank_wire_btn = '//a[@title="Pay by bank wire"]'

    """GETTERS"""

    def get_pay_by_bank_wire_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pay_by_bank_wire_btn)))

    """ACTIONS"""

    def click_pay_by_bank_wire_btn(self):
        self.get_pay_by_bank_wire_btn().click()
        print("Clicked pay_by_bank_wire_btn")

    """METHODS"""

    def choose_bank_wire_payment(self):
        self.get_current_url()
        self.click_pay_by_bank_wire_btn()
