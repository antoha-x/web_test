from selenium.webdriver.common.by import By

from helpers.SeleniumHelper import close_banner
from pages.BasePage import BasePage
from pages.equities.RussiaEquitiesPage import RussiaEquitiesPage


class RussiaPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = super().get_browser()
        self.link_russia_stocks = "//h2/a[contains(text(),'{}')]"

    @close_banner()
    def go_to_russia_stocks(self, text_to):
        self.browser.find_element(By.XPATH, self.link_russia_stocks.format(text_to)).click()
        return RussiaEquitiesPage(self.browser)