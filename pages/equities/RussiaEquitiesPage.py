from selenium.webdriver.common.by import By

from helpers.SeleniumHelper import close_banner
from pages.BasePage import BasePage
from pages.equities.TableStocks import TableStocks


class RussiaEquitiesPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.title = "#leftColumn > h1.shortH1"
        self.stock_table = TableStocks(self.browser)

    @close_banner()
    def get_title(self):
        title = self.browser.find_element(By.CSS_SELECTOR, "#leftColumn > h1.shortH1")
        return title.text