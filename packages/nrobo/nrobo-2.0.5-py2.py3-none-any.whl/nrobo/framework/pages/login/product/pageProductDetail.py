import time

from helpers.Page import Page
from selenium.webdriver.common.by import By


class PageProductDetail(Page):

    def __init__(self, driver, data={}, extra={}):
        super().__init__(driver)
        self.data = data
        self.extra = extra

        self.inventory_details_name = (By.XPATH, "//div[contains(@class,'inventory_details_name')]")
        self.inventory_details_desc = "//div[contains(@class,'inventory_details_desc')]"
        self.inventory_details_price = (By.XPATH, "//div[contains(@class,'inventory_details_price')]")
        self.btn_inventory = (By.XPATH, "//button[contains(@class,'btn_inventory') and text()='Add to cart']")

    def get_inventory_details_name(self):
        return self.find_by_element(*self.inventory_details_name).text

    def match_found_inventory_details_description(self, data={}):
        return self.is_element_displayed(By.XPATH, "//div[contains(@class,'inventory_details_desc') and text()='" + data['product_description'] + "']")

    def get_inventory_details_price(self):
        return self.find_by_element(*self.inventory_details_price).text

    def is_button_add_to_cart_present(self):
        return self.is_element_displayed(*self.btn_inventory)

    def click_button_add_to_cart(self):
        self.find_element_click(*self.btn_inventory)
