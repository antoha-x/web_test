from selenium.webdriver.common.by import By

from helpers.SeleniumHelper import close_banner
from pages.BasePage import BasePage


class TableStocks(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.table = self.browser.find_element(By.CSS_SELECTOR, "#cross_rate_markets_stocks_1")

    def __company_name_webelements(self):
        return self.table.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(2)")

    def __company_price_webelements(self):
        return self.table.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(3)")

    @close_banner()
    def column_company_names(self):
        names = []
        company_names = self.__company_name_webelements()
        for company in company_names:
            names.append(company.text)
        return names.copy()

    @close_banner()
    def column_cost(self):
        cost = []
        prices = self.__company_price_webelements()
        for item in prices:
            cost.append(float(item.text.replace('.', '').replace(',', '.')))
        return cost.copy()

    def get_stocks_dict(self):
        return dict(zip(self.column_company_names(), self.column_cost()))
