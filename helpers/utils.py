def find_percent_change(percent, actual_stock, db_stock):
    changed_stock = {}
    for company in db_stock:
        if __change_percent(db_stock[company], actual_stock[company]) >= float(percent):
            changed_stock[company] = actual_stock[company]
    return changed_stock


def __change_percent(old_cost, new_cost):
    return ((new_cost - old_cost) / old_cost) * 100


def normalize_file_name(file_name):
    replace_symbols = {
        '"': "'",
        ">": "",
        "<": "",
        "\\": "",
        "|": "",
        "/": "_",
        ":": "",
        "*": "",
        "?": ""
    }
    for key, value in replace_symbols.items():
        file_name = file_name.replace(key, value)
    return file_name

def log_step(context):
    report_data = {
        context.step.name : {
            "keyword": context.step.keyword,
            "status": context.step.status.name,
            "hook_failed": context.step.hook_failed,
            "duration": context.step.duration,
            "error_message": context.step.error_message,
            "screenshot": context.screenshot
        }
    }
    context.test_report.add_scenario_data(context.scenario.name, report_data)


def parse_status(status):
    pass