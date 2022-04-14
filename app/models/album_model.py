# Desenvolva sua classe Album abaixo

from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Album(db.Model):
    __tablename__ = "albums"

    album_id = Column(Integer, primary_key=True)
    name = Column(String)
    release_date = Column(DateTime)

    band_id = Column(Integer, ForeignKey("bands.band_id"))

    band = relationship("Band", back_populates="albums", uselist=False)
    musics = relationship("Music", backref="album")
