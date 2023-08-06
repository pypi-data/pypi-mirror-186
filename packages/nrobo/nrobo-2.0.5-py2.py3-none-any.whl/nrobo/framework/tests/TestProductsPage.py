import time

import pytest

from pages.login.pageProducts import PageProducts
from helpers.nRobo import NRobo
from pages.pagePublic import PagePublic


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('password')
@pytest.mark.usefixtures('username')
@pytest.mark.usefixtures('url')
class TestProductPage(NRobo):

    @pytest.mark.sanity
    def test_product_details_page_opens_when_a_user_clicks_on_an_inventory_item(self, url, username, password):

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

        assert pageProducts.match_found_product_description(data) == True

        pageProducts.select_product(data)



