from selenium import webdriver

from config.config import Config


class DriverFactory:

    @staticmethod
    def get_driver():

        if Config.BROWSER.lower() == "chrome":

            driver = webdriver.Chrome()

            driver.maximize_window()
            driver.implicitly_wait(Config.IMPLICIT_WAIT)
            driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

            return driver

        raise Exception(
            f"Browser {Config.BROWSER} not supported"
        )