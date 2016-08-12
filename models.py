from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///msgdetect.db")
Session = sessionmaker(bind = engine)

def get_session():
  return Session()

class User(Base): #inherits Base
    __tablename__="users"

    id = Column(Integer, primary_key=True)
    device = Column(String(120))
    accel_readings = relationship('Accelerometer', backref='user', lazy='dynamic')
    keyboard_readings = relationship('Keyboard', backref='user', lazy='dynamic')
    def __repr__(self):
        return '<User "%d">' % (self.id)

class Accelerometer(Base):
    __tablename__="accelerometer"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    timestamp = Column(DateTime, index = True)
    accel_x = Column(Float)
    accel_y = Column(Float)
    accel_z = Column(Float)

    def __repr__(self):
        return '<Accelerometer "%d">' % (self.id)

class Keyboard(Base):
    __tablename__="keyboard"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    timestamp = Column(DateTime, index = True)
    key_press = Column(Integer, index = True)

    def __repr__(self):
        return '<Keyboard "%d">' % (self.id)

# if __name__ == "__main__":
#     engine = create_engine("sqlite:///msgdetect.db")
#     Base.metadata.create_all(bind=engine)
#     #Session = sessionmaker(bind = engine)
