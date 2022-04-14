# Desenvolva sua classe Music abaixo

from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String, Time


@dataclass
class Music(db.Model):
    __tablename__ = "musics"

    music_id = Column(Integer, primary_key=True)
    title = Column(String)
    duration = Column(Time)

    album_id = Column(Integer, ForeignKey("albums.album_id"))
