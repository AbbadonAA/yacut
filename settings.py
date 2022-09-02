import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Не проходит pytest, хотя конфиг SORT_KEYS позволяет сделать
    # вывод в порядке, указанном в спецификации. Без него url и
    # short_link выводятся наоборот: short_link, url
    # JSON_SORT_KEYS = False
