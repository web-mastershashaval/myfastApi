from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="blog")

class User(Base):
    __tablename__ ='Users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column (String)
    email = Column (String)
    password = Column (String)

    blogs = relationship('blog', back_populates='creator')