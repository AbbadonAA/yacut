import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='qwerty12345')
    # Не проходит pytest, хотя конфиг SORT_KEYS позволяет сделать
    # вывод в порядке, указанном в спецификации. Без него url и
    # short_link выводятся наоборот: short_link, url
    # JSON_SORT_KEYS = False
