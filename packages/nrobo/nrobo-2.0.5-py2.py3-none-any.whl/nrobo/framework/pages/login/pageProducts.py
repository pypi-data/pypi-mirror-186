import time

from selenium.common import StaleElementReferenceException

from helpers.Page import Page
from selenium.webdriver.common.by import By
from config import nRoboConfig


class PageProducts(Page):
    lnk_shopping_cart = (By.XPATH, "//a[contains(@class,'shopping_cart_link')]")

    # ---------------------------
    # CSS class structure
    # ---------------------------
    # inventory_list
    #   inventory_item
    #       inventory_item_name
    #       inventory_item_desc
    #       inventory_item_price
    #       btn_inventory

    inventory_list = "inventory_list"
    inventory_item = "inventory_item"
    inventory_item_img = "inventory_item_img"
    inventory_item_name = "inventory_item_name"
    inventory_item_desc = "inventory_item_desc"
    inventory_item_price = "inventory_item_price"
    btn_inventory = "btn_inventory"

    lst_inventory = (By.CSS_SELECTOR, "." + inventory_list + " > ." + inventory_item)

    def __init__(self, driver, data={}, extra={}):
        super().__init__(driver)
        self.data = data
        self.extra = extra

    def get_inventory_list(self):
        return self.find_by_elements(*self.lst_inventory)

    def select_product(self, data={}):
        self.log.info("Select product[" + data['product_name'] + "]")
        for inventory in self.get_inventory_list():

            #  Validate product name
            try:
                _element = inventory.find_element(By.XPATH,
                                      './/div[contains(@class,"' + self.inventory_item_name + '") and text()="' + str(
                                          data['product_name']) + '"]')
            except StaleElementReferenceException as e:
                pass

            #  self.log.info(_element)

            if _element:
                time.sleep(nRoboConfig.Waits.SLEEP_TIME.value)
                try:
                    inventory.find_element(By.XPATH, ".//img[@alt='" + data['product_name'] + "']/../..//a").click()
                except StaleElementReferenceException as e:
                    pass

    def match_found_product_description(self, data={}):
        self.log.info("Get product[" + data['product_name'] + "] description")

        for inventory in self.get_inventory_list():

            #  Validate product name
            try:
                _element = inventory.find_element(By.XPATH,
                                                  './/div[contains(@class,"' + self.inventory_item_name + '") and text()="' + str(
                                                      data['product_name']) + '"]')
            except StaleElementReferenceException as e:
                pass

            #  self.log.info(_element)

            #  Validate product description
            try:
                inventory.find_element(By.XPATH,
                                                  '../..//div[contains(@class,"' + self.inventory_item_desc + '") and text()="' + data['product_description'] + '"]')
                return True
            except StaleElementReferenceException as e:
                pass

            return False



