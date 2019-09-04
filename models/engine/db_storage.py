#!/usr/bin/python3
"""MySQL database storage"""
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import State, City, User, Place, Review, Amenity
from models.base_model import BaseModel, Base
import os


class DBStorage:
    """Manages database
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialization
        """
        HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(HBNB_MYSQL_USER,
                                                      HBNB_MYSQL_PWD,
                                                      HBNB_MYSQL_HOST,
                                                      HBNB_MYSQL_DB),
            pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """shows all objects
        """
        new_dict = dict()
        if cls:
            temp = self.__session.query(eval(cls)).all()
        else:
            temp = self.__session.query(State, City, User, Place).all()
        for item in temp:
            thing = str(item).split(' ')
            key = thing[0][1:-1] + '.' + thing[1][1:-1]
            d = {key: item}
            new_dict.update(d)
        return new_dict

    def new(self, obj):
        """adds new object otsession
        """
        self.__session.add(obj)

    def save(self):
        """saves session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """ Close dtabase
        """
        self.__session.remove()
