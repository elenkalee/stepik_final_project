from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Bank_wire_payment_page(Base):
    """Финальная странциа подтверждения платежа, переход на страницу с сообщением, что запрос завершен"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""
    confirm_my_order_btn = '//*[@id="cart_navigation"]/button'
    main_word = '//*[@id="center_column"]/div/p/strong'

    """GETTERS"""

    def get_confirm_my_order_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_my_order_btn)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    """ACTIONS"""

    def click_confirm_my_order_btn(self):
        self.get_confirm_my_order_btn().click()
        print("Clicked confirm_my_order_btn on Bank-wire Payment page")

    """METHODS"""

    def final_confirm_and_submit_order(self):
        self.click_confirm_my_order_btn()
        self.assert_word(self.get_main_word(), 'Your order on My Store is complete.')
