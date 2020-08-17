from selenium.common.exceptions import JavascriptException

from pages import banner_locators


def remove_all_banners(browser) -> None:
    for type_locator, locator in banner_locators.close_banners.items():
        remove_all_element(browser, type_locator, locator)


def remove_by_class(browser, list_element_class) -> None:
    js_function = """
        function removeElementsByClass(className){
            var elements = document.getElementsByClassName(className);
            while(elements.length > 0){
                elements[0].parentNode.removeChild(elements[0]);
            }
        };"""
    js_parts = [js_function]

    for element in list_element_class:
        js_parts.append("removeElementsByClass('{}');".format(element))

    js_script = "\n ".join(js_parts)
    browser.execute_script(js_script)


def remove_by_id(browser, list_element_id) -> None:
    for element in list_element_id:
        js_script = """var elements = document.getElementById('{}');
        if (elements != null) {{elements.remove();}}""".format(element)
        browser.execute_script(js_script)

def remove_all_element(browser, type_locator, list_element):
    js_function = """
            function removeElements(selectorType, selector){
                var elements = ("id".localeCompare(selectorType) === 0) ? 
                    document.getElementById(selector) : document.getElementsByClassName(selector);
                if (elements != null) {
                    while(elements.length > 0){
                        elements[0].parentNode.removeChild(elements[0]);
                    }
                }
            };"""
    js_parts = [js_function]
    for element in list_element:
        js_parts.append("removeElements('{}', '{}');".format(type_locator, element))

    js_script = "\n ".join(js_parts)
    browser.execute_script(js_script)