#language: ru
@fixture.browser.chrome
Функционал: сайт investing.com
    Сценарий: Собираем информацию (название, цена) о российских акциях, цена которых изменилась
    на определенный % в большую сторону.
        Если зайти на сайт https://ru.investing.com/
        И в главном меню выбрать "Котировки" -> "Россия" -> "Россия - акции"
        Тогда заголовок на странице будет "Россия - акции"
        И Собрать информацию об акциях, цена которых изменилась на 5 процентов в большую сторону
        И выгрузить собранные данные в файл "stock.json"