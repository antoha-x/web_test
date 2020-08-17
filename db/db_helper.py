from db import config
from db.Database import Database


def __sql_from_file(sql_file_name):
    with open("/".join([config.BASE_SQL_FILE_DIR, sql_file_name])) as file:
        sql = ""
        for line in file.readlines():
            sql = "".join([sql, line.rstrip()])
    return sql


def run_sql_file(sql_file_name, *args):
    query = __sql_from_file(sql_file_name)
    cursor = Database().connect()
    cursor.execute(query, args)
    if ' '.join(query.split()).lower().startswith("select"):
        return cursor.fetchall()


def get_stocks_db():
    def normalize_price(result):
        column_number_company_name = 0
        column_number_price = 1
        normalize_result = {}
        for row in result:
            normalize_result[row[column_number_company_name]] = \
                float(row[column_number_price].replace('.', '').replace(',', '.'))
        return normalize_result
    return normalize_price(run_sql_file(config.GET_STOCKS))
