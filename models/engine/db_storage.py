#!/usr/bin/env python3
from sqlalchemy import create_engine
import os


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(HBNB_MYSQL_USER,                                                                      HBNB_MYSQL_PWD,
                                                      HBNB_MYSQL_HOST,
                                                      HBNB_MYSQL_DB), pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            self.__engine.drop_all(tables)

    def all(self, cls=None):
        return self.__session

    def new(self, obj):
        pass

    def save(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        pass
