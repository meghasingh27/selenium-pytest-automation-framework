import pytest

from utils.driver_factory import DriverFactory
from config.config import Config


@pytest.fixture(scope="function")
def driver():

    driver = DriverFactory.get_driver()

    driver.get(Config.BASE_URL)

    yield driver

    driver.quit()