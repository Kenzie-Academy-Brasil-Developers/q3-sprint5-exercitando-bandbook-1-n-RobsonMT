# Desenvolva sua classe Band abaixo

from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class Band(db.Model):
    __tablename__ = "bands"

    band_id = Column(Integer, primary_key=True)
    name = Column(String)
    albuns = relationship("Album", back_populates="band")
