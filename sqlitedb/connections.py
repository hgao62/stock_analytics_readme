from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_PATH = r"C:\development\repo\stock_analytics\sqlitedb\stock_analytics.db"

# Create a SQLAlchemy engine for Alembic
ENGINE = create_engine(f'sqlite:///{DATABASE_PATH}')
Session = sessionmaker(bind=ENGINE)