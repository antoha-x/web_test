import os
from datetime import datetime

from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from helpers.SeleniumHelper import MyListener, take_screenshot
from helpers.Storage import Storage
from helpers.utils import log_step


@fixture
def browser_chrome(context, timeout=10, is_headless=False):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    if is_headless:
        chrome_options.add_argument('headless')
    context.browser = EventFiringWebDriver(webdriver.Chrome(options=chrome_options), MyListener())
    context.browser.implicitly_wait(timeout)
    yield context.browser
    context.browser.delete_all_cookies()
    context.browser.quit()


@fixture
def browser_firefox(context, timeout=10):
    context.browser = webdriver.Firefox()
    context.browser.implicitly_wait(timeout)
    yield context.browser
    context.browser.quit()


def before_tag(context, tag):
    if tag == "fixture.browser.firefox":
        use_fixture(browser_firefox, context, timeout=10)
    if tag == "fixture.browser.chrome.headless":
        use_fixture(browser_chrome, context, timeout=10, is_headless=True)
    if tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context, timeout=10)


def before_all(context):
    context.storage = Storage()
    context.test_report = Storage(False)
    context.screenshot = ""


def before_step(context, step):
    context.step = step

@take_screenshot()
def after_step(context, step):
    log_step(context)
    context.test_report.save_to_file("./test_reports.json")