import sqlite3

DB_FILE_NAME = "stocks"


class MetaDatabase(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaDatabase, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaDatabase):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(DB_FILE_NAME)
            self.cursor = self.connection.cursor()
        return self.cursor
