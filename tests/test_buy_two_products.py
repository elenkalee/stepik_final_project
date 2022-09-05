import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.addresses_page import Addresses_page
from pages.bank_wire_payment_page import Bank_wire_payment_page
from pages.dresses_page import Dresses_page
from pages.index_page import Index_page
from pages.payment_page import Payment_page
from pages.shipping_page import Shipping_page
from pages.sign_in_page import Sign_in_page
from pages.summary_page import Summary_page


def test_buy_two_products():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\EL\\PycharmProjects\\final_project_stepik\\utilities\\chromedriver.exe',
        options=options)

    ip = Index_page(driver)
    ip.go_to_dresses()

    dp = Dresses_page(driver)
    dp.add_to_cart_two_items()

    sp = Summary_page(driver)
    sp.confirm_shopping_cart_summary()

    sign_in = Sign_in_page(driver)
    sign_in.sign_in()

    ap = Addresses_page(driver)
    ap.confirm_address()

    shp = Shipping_page(driver)
    shp.confirm_shipping_info()

    pp = Payment_page(driver)
    pp.choose_bank_wire_payment()

    bwp = Bank_wire_payment_page(driver)
    bwp.final_confirm_and_submit_order()

    print("Test Completed")
    time.sleep(3)
    driver.quit()
