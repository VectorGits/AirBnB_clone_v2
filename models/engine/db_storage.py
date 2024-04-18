from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models.state import State
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        new_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Amenity, Place, Review]
            objs = []
            for cls in classes:
                objs.extend(self.__session.query(cls))
        for obj in objs:
            key = type(obj).__name__ + "." + str(obj.id)
            new_dict[key] = obj
        return new_dict
