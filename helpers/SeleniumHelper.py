import functools
import os
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

from helpers.utils import normalize_file_name
from pages import banner_locators


class MyListener(AbstractEventListener):
    def after_find(self, by, value, driver):
        print(f'Тип поиска: {by}, локатор: {value}. Элемент найден')

    def on_exception(self, exception, driver):
        print(exception)


def close_banner():
    def step_decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            selector_list = banner_locators.get_banner_selector_list()
            for selector in selector_list:
                close_element(args[0].get_browser(), selector)
            return func(*args, **kwargs)

        return wrapped

    return step_decorator


def close_element(browser, selector):
    try:
        elements = browser.find_elements(By.XPATH, selector)
        for element in elements:
            if element.is_displayed():
                element.click()
    except NoSuchElementException:
        return False


def get_screenshot(browser, full_name):
    browser.save_screenshot(full_name)
    return full_name


def create_file_name(step_name):
    dir_name = "screenshots"
    file_name = f'{step_name}{datetime.today().timestamp()}.png'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return f'./{dir_name}/{normalize_file_name(file_name)}'


def take_screenshot():
    def step_decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            browser = args[0].browser
            file_name = create_file_name(args[0].step.name)
            args[0].screenshot = file_name
            result = func(*args, **kwargs)
            get_screenshot(browser, file_name)
            return result
        return wrapped

    return step_decorator
