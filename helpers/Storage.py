import json
from collections import Mapping, Container
from sys import getsizeof


from db import db_helper


class Storage(object):
    def __init__(self, init_from_db=True) -> None:
        if init_from_db:
            self.keys = ['db', ]
            self.scenario_data = {self.keys[0] : db_helper.get_stocks_db()}
        else:
            self.keys = []
            self.scenario_data ={}

    def add_key(self, key):
        if self.find_index_key(key) == -1:
            self.keys.append(key)
            self.scenario_data[key] = {}
        return self

    def get_keys(self):
        return self.keys.copy()

    def find_index_key(self, key):
        if self.keys.count(key) != 0:
            return self.keys.index(key)
        return -1

    def size(self):
        return self.__deep_getsizeof(self.scenario_data, set())

    def get_scenario_data(self, key):
        return self.scenario_data[key].copy()

    def add_scenario_data(self, key, data):
        if self.find_index_key(key) == -1:
            self.add_key(key)
        self.scenario_data[key].update(data)
        return self


    def __deep_getsizeof(self, o, ids):
        d = self.__deep_getsizeof
        if id(o) in ids:
            return 0

        r = getsizeof(o)
        ids.add(id(o))

        if isinstance(o, str):
            return r

        if isinstance(o, Mapping):
            return r + sum(d(k, ids) + d(v, ids) for k, v in o.items())

        if isinstance(o, Container):
            return r + sum(d(x, ids) for x in o)

        return r

    def save_to_file(self, filename, key=None):
        save_data = self.scenario_data if key is None else self.scenario_data[key]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(save_data, file, ensure_ascii=False)
