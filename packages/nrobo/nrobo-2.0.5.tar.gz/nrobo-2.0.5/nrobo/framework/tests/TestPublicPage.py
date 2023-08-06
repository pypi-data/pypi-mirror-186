import pytest

from helpers.Page import Page
from helpers.nRobo import NRobo

from pages.pagePublic import PagePublic
from pages.login.pageProducts import PageProducts


@pytest.mark.usefixtures('setup')
@pytest.mark.usefixtures('password')
@pytest.mark.usefixtures('username')
@pytest.mark.usefixtures('url')
class TestSauceDemoDotCom(NRobo):

    @pytest.mark.sanity
    def test_a_user_can_login_with_valid_credential(self, url, username, password):
        pagePublic = PagePublic(self.driver)
        pagePublic.get(url)

        pagePublic.type_username("standard_user")
        pagePublic.type_password("secret_sauce")
        pagePublic.click_button_login()

        pageProducts = PageProducts(pagePublic.driver)

        assert pageProducts.is_element_displayed(*pageProducts.lnk_shopping_cart) == True

    @pytest.mark.sanity
    @pytest.mark.ui
    def test_a_user_can_not_login_with_invalid_credential(self, url, username, password):
        pagePublic = PagePublic(self.driver)
        pagePublic.get(url)

        pagePublic.type_username("locked_out_user")
        pagePublic.type_password("secret_sauce")
        pagePublic.click_button_login()

        assert pagePublic.is_element_displayed(*pagePublic.txt_username) == True
        assert pagePublic.is_element_displayed(*pagePublic.txt_password) == True
        assert pagePublic.is_element_displayed(*pagePublic.btn_login) == True
        assert pagePublic.is_element_displayed(*pagePublic.msg_locked_out_user)

    @pytest.mark.sanity
    def test_sample_failing_test(self, url, username, password):
        pagePublic = PagePublic(self.driver)
        pagePublic.get(url)

        pagePublic.type_username("locked_out_user")
        pagePublic.type_password("secret_sauce")
        pagePublic.click_button_login()

        assert False == True  # Assured failure

    @pytest.mark.sanity
    @pytest.mark.skip  # Test will be skipped
    def test_sample_skipping_test(self, url, username, password):
        pagePublic = PagePublic(self.driver)
        pagePublic.get(url)

        pagePublic.type_username("locked_out_user")
        pagePublic.type_password("secret_sauce")
        pagePublic.click_button_login()

        assert False == True
