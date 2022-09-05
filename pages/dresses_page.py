from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Dresses_page(Base):
    """Страница Dresses. Здесь выбираются фильтры и добавляется товар в корзину"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""

    summer_dresses_checkbox = '//input[@id="layered_category_11"]'
    size_s_checkbox = '//input[@id="layered_id_attribute_group_1"]'
    color_yellow_checkbox = '//input[@id="layered_id_attribute_group_16"]'
    color_orange_checkbox = '//input[@id="layered_id_attribute_group_13"]'
    price_range_slider = '//*[@id="layered_price_slider"]/a[2]'
    sort_by_drop_down = '//div[@id="uniform-selectProductSort"]'
    sort_by_lowest_price_first = '[value="price:asc"]'
    hover_main_menu_item_1 = '//*[@id="center_column"]/ul/li[1]/div/div[2]'
    add_to_cart_btn_item_1 = '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]'
    continue_shopping_btn = '//span[@title="Continue shopping"]'
    hover_main_menu_item_2 = '//*[@id="center_column"]/ul/li[2]/div/div[2]'
    add_to_cart_btn_item_2 = '//*[@id="center_column"]/ul/li[2]/div/div[2]/div[2]/a[1]'
    proceed_to_checkout_btn = '//a[@title="Proceed to checkout"]'

    """GETTERS"""

    def get_summer_dresses_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.summer_dresses_checkbox)))

    def get_size_s_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_s_checkbox)))

    def get_color_yellow_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_yellow_checkbox)))

    def get_color_orange_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_orange_checkbox)))

    def get_price_range_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_range_slider)))

    def get_sort_by_drop_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_drop_down)))

    def get_sort_by_lowest_price_first(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.sort_by_lowest_price_first)))

    def get_add_to_cart_btn_item_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_btn_item_1)))

    def get_continue_shopping_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_shopping_btn)))

    def get_add_to_cart_btn_item_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_btn_item_2)))

    def get_proceed_to_checkout_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.proceed_to_checkout_btn)))

    """ACTIONS"""

    # TODO: Здесь возникли сложности с классом Actios и геттерами. Не могу понять, как использовать геттеры.

    def check_summer_dresses_checkbox(self):
        # TODO: как вызвать get_summer_dresses_checkbox() ?
        action = ActionChains(self.driver)
        local_summer_dresses_checkbox = self.driver.find_element(By.XPATH, self.summer_dresses_checkbox)
        action.move_to_element(local_summer_dresses_checkbox)
        action.click()
        print("! Clicked summer_dresses_checkbox")

    def check_size_s_checkbox(self):
        # TODO: как вызвать get_size_s_checkbox()?
        action = ActionChains(self.driver)
        local_size_s_checkbox = self.driver.find_element(By.XPATH, self.size_s_checkbox)
        action.move_to_element(local_size_s_checkbox)
        action.click()
        print("! Clicked size_S_checkbox")

    def check_color_yellow_checkbox(self):
        self.get_color_yellow_checkbox().click()
        print("! Clicked color_yellow_checkbox")

    def check_color_orange_checkbox(self):
        self.get_color_orange_checkbox().click()
        print("! Clicked color_orange_checkbox")

    def move_price_range_slider(self):
        # TODO: как вызвать get_price_range_slider()?
        action = ActionChains(self.driver)
        price_range = self.driver.find_element(By.XPATH, self.price_range_slider)
        action.click_and_hold(price_range).move_by_offset(-20, 0).release().perform()
        print("! Moved price_range_slider")

    def click_sort_by_price_lowest_first(self):
        self.get_sort_by_drop_down().click()
        self.get_sort_by_lowest_price_first().click()
        print("! Sort_by Price: Lowest First chosen")

    def click_add_to_cart_btn_item_1(self):
        # TODO: как вызвать get_add_to_cart_btn_item_1()?
        action = ActionChains(self.driver)
        local_main_menu_1 = self.driver.find_element(By.XPATH, self.hover_main_menu_item_1)
        action.move_to_element(local_main_menu_1)  # Навести мышь на главное появляющееся меню
        local_add_to_cart_1 = self.driver.find_element(By.XPATH, self.add_to_cart_btn_item_1)
        action.move_to_element(local_add_to_cart_1)  # Навести мышь на подменю, где кнопка add to cart
        action.click().perform()
        print("! Clicked add_to_cart_btn_item_1")

    def click_continue_shopping_btn(self):
        self.get_continue_shopping_btn().click()
        print("! Clicked continue_shopping_btn")

    def click_add_to_cart_btn_item_2(self):
        # TODO: как вызвать get_add_to_cart_btn_item_1()?
        action = ActionChains(self.driver)
        local_main_menu_2 = self.driver.find_element(By.XPATH, self.hover_main_menu_item_2)
        action.move_to_element(local_main_menu_2)  # Навести мышь на главное появляющееся меню
        local_add_to_cart_2 = self.driver.find_element(By.XPATH, self.add_to_cart_btn_item_2)
        action.move_to_element(local_add_to_cart_2)
        action.click().perform()  # Навести мышь на подменю, где кнопка add to cart

    def click_proceed_to_checkout_btn(self):
        self.get_proceed_to_checkout_btn().click()
        print("! Clicked proceed_to_checkout on Dresses page")

    """METHODS"""

    def add_to_cart_two_items(self):
        """Основной тест-сценарий: установка фильтров, выбор двух товаров, переход в корзину"""
        self.get_current_url()
        self.check_summer_dresses_checkbox()
        self.check_size_s_checkbox()
        self.check_color_orange_checkbox()
        self.check_color_yellow_checkbox()
        self.move_price_range_slider()
        self.click_sort_by_price_lowest_first()
        self.click_add_to_cart_btn_item_1()
        self.click_continue_shopping_btn()
        self.click_add_to_cart_btn_item_2()
        self.click_proceed_to_checkout_btn()
