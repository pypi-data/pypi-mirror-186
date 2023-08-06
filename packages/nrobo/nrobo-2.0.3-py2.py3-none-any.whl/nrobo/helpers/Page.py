from helpers.SeleniumWebdriverWrapper import SeleniumWebdriverWrapper


class Page(SeleniumWebdriverWrapper):
    """
    Base class for all Page objects
    """

    def __int__(self, driver):
        """
        Constructor

        :param driver:
        :return:
        """

        super.__init__(driver)

