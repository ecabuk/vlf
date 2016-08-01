from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

from settings import SETTINGS, DB_SESSION


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    interval = Column(Integer, nullable=True)
    transmitters = Column(Text, default='')
    stations = relationship('Station', backref='profile', cascade='all, delete, delete-orphan')

    @staticmethod
    def create_new():
        new_profile = Profile(
            interval=SETTINGS.value('profile_session/interval', 5),
            transmitters=SETTINGS.value('profile_session/interval', '26.7'),
        )
        DB_SESSION.add(new_profile)
        DB_SESSION.commit()
        return new_profile

    def new_station(self):
        if self.has_stations():
            new_point = int(
                DB_SESSION.query(Station).with_parent(self).order_by(Station.point.desc()).first().point) + 1
        else:
            new_point = 1
        new_station = Station(
            profile=self,
            point=new_point,
            frames=100,
            resolution=10,
        )
        DB_SESSION.add(new_station)
        DB_SESSION.commit()
        return new_station

    def has_stations(self):
        return len(self.stations) != 0

    def get_last_station(self):
        return DB_SESSION.query(Station).with_parent(self).order_by(Station.point.desc()).first()


class Station(Base):
    __tablename__ = 'stations'

    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    measurements = relationship('Measurement', backref='station', cascade='all, delete, delete-orphan')
    point = Column(Integer)

    frames = Column(Integer, nullable=True)
    resolution = Column(Integer, nullable=True)

    time = Column(DateTime, nullable=True)

    def has_measurements(self):
        return len(self.measurements) != 0


class Measurement(Base):
    __tablename__ = 'measurements'

    id = Column(Integer, primary_key=True)
    station_id = Column(Integer, ForeignKey('stations.id'))
    freq = Column(Float)

    in_phase = Column(Float)
    quadrature = Column(Float)
