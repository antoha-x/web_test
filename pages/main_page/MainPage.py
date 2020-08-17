from selenium.webdriver.common.by import By

from helpers.SeleniumHelper import close_banner
from pages.BasePage import BasePage
from pages.markets.RussiaPage import RussiaPage

INDEX_MENU_CATEGORY_FOR_REMOVE = 0


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = super().get_browser()
        self.sub_menu_quotation = "//*[@id='markets_subnav_link' and contains(text(),'{}')]"

    def open(self, url):
        self.browser.get(url)
        return self

    # Добавил реализацию перехода через выпадающее меню с использованием ActionChains,
    # но при подключении листенера не работеат, нужен фикс selenium'а
    """@close_banner()
    def go_to_menu(self, *args):
        menu = self.get_main_menu()["xpath"].copy()
        list_menu_category = list(menu)
        actions = ActionChains(self.browser)
        for item in args:
            if item is not None:
                element_menu = self.browser.find_element(By.XPATH,
                    menu.pop(list_menu_category.pop(INDEX_MENU_CATEGORY_FOR_REMOVE)).format(item))
                actions.move_to_element(element_menu._parent)
        actions.click().perform()"""

    @close_banner()
    def go_to_sub_menu(self, menu, sub_menu):
        self.browser.find_element(By.XPATH, self.sub_menu_quotation.format(menu)).click()
        self.browser.find_element(By.XPATH, self.sub_menu_quotation.format(sub_menu)).click()
        return RussiaPage(self.browser)