class BasePage(object):

    def __init__(self, browser):
        self.browser = browser
        """
        # Локатор для выпадающего меню. Подробнее в MainPage.py
        self.main_menu = {"xpath" :
            {"menu" : "//*[@id='navMenu']//a[text()='{}']",
            "sub_menu" : "//*[@id='navMenu']//ul[@class='subMenuNav']//a[text()='{}']",
            "sub_sub_menu" : "//*[@id='navMenu']//ul[@class='main']//a[text()='{}']"}
        }"""


    def get_browser(self):
        return self.browser

    """
    # Для работы с выпадающим меню через ActionChains. Подробнее в MainPage.py
    def get_main_menu(self):
        return self.main_menu.copy()"""
