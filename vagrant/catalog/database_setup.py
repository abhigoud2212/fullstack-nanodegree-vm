__author__ = 'abhig'

import sys
from sqlalchemy import Column,ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key= True)
    name = Column(String(250), nullable= False)
    email = Column(String(250), nullable= False)
    picture = Column(String(250))

class Restaurant(Base):

    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key = True)
    name = Column(String(200), nullable= False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship(User, backref="restaurant", passive_deletes=True)

    @property
    def serialize(self):

        return {
            'id': self.id,
            'name': self.name
        }

class MenuItem(Base):

    __tablename__ = 'menu_item'

    name = Column(String(100), nullable= False)
    id = Column(Integer, primary_key= True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    image = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id', ondelete='CASCADE'))
    restaurant = relationship(Restaurant, backref="menu_item", passive_deletes=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship(User, backref="menu_item", passive_deletes=True)

# serializable format
    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
            'image': self.image
        }
### Insert at the end of the file #####
engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.create_all(engine)