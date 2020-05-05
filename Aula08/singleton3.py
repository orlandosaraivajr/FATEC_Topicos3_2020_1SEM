# Singleton com Metaclasses

import sqlite3
class MetaSingleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
    
class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()

print(logger1, logger2)


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

db1.close()
