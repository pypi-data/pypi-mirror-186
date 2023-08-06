import time

import pytest

from pages.login.pageProducts import PageProducts
from pages.login.product.pageProductDetail import PageProductDetail
from helpers.nRobo import NRobo
from pages.pagePublic import PagePublic


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('password')
@pytest.mark.usefixtures('username')
@pytest.mark.usefixtures('url')
class TestProductDetailsPage(NRobo):

    @pytest.mark.regression
    def test_product_details_page_view(self, url, username, password):

        data = {'product_name': "Sauce Labs Backpack",
                'product_description': "carry.allTheThings() with the sleek, streamlined Sly Pack that melds "
                                       "uncompromising style with unequaled laptop and tablet protection.",
                'product_price': "$29.99"
                }  # Store test data in form of dictionary

        pagePublic = PagePublic(self.driver)
        pagePublic.get(url)

        pagePublic.type_username("standard_user")
        pagePublic.type_password("secret_sauce")
        pagePublic.click_button_login()

        pageProducts = PageProducts(pagePublic.driver)
        pageProducts.select_product(data)

        pageProductDetails = PageProductDetail(pagePublic.driver)

        assert pageProductDetails.get_inventory_details_name() == data['product_name']
        assert pageProductDetails.match_found_inventory_details_description(data) == True
        assert pageProductDetails.is_button_add_to_cart_present() == True
        assert pageProductDetails.get_inventory_details_price() == data['product_price']

