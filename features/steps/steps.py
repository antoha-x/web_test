from behave import when, then


from helpers import utils
from pages.main_page.MainPage import MainPage


@when('зайти на сайт {url}')
def open_url(context, url):
    context.main_page = MainPage(context.browser)
    context.main_page.open(url)



@when('в главном меню выбрать "{menu}" -> "{sub_menu}" -> "{title}"')
def go_to_menu(context, menu, sub_menu=None, title=None):
    context.russia_equities = context.main_page.go_to_sub_menu(menu, sub_menu).go_to_russia_stocks(title)


@then('заголовок на странице будет "{expected_title}"')
def check_title(context, expected_title):
    current_title = context.russia_equities.get_title()
    assert expected_title in current_title, f"Загловок страницы не соответствует заданному!\n" \
                                            f"Ожидаемый заголовок: {expected_title}\n" \
                                            f"Фактический загловок: {current_title}"


@then('Собрать информацию об акциях, цена которых изменилась на {change_percent} процентов в большую сторону')
def collect_stock(context, change_percent):
    actual_stock = context.russia_equities.stock_table.get_stocks_dict()
    collect_stock = utils.find_percent_change(change_percent,
                                              actual_stock,
                                              context.storage.get_scenario_data("db"))
    context.storage.add_scenario_data(context.scenario.name, collect_stock)


@then('выгрузить собранные данные в файл "{file_name}"')
def save_to_file(context, file_name):
    context.storage.save_to_file(file_name, context.scenario.name)
