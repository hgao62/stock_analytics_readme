from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TickerPrice(Base):
    __tablename__ = "TickerPrice"
    Ticker = Column(String, primary_key=True)
    Date = Column(Date, primary_key=True)
    Close = Column(Float)
    Volume = Column(Integer)
    StockSplits = Column(Integer)
    Type = Column(String)

