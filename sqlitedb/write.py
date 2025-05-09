
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from sqlitedb.connections import Session
from sqlitedb.models import TickerPrice

def write_data_to_sqlite(model:declarative_base, data: pd.DataFrame) -> None:
    """Write data to SQLite table using ORM model

    Args:
        model (declarative_base): SQLALchemy ORM model
        data (pd.DataFrame): data you want to insert into database
    """
    session = Session()
    try:
        records = data.to_dict(orient='records')
        session.bulk_insert_mappings(model, records)
        session.commit()
    except Exception as e:
        print(f"Error writing dat a to sqlite table  {model.__tablename__}: {e}")
        
    finally:
        session.close()
        
        
data = pd.DataFrame({
        'Ticker': ['AAPL', 'MSFT'],
        'Date': [pd.Timestamp(2024,1,1).date(), pd.Timestamp(2024,1,1).date()],
        'Close': [150.0, 250.0],
        'Volume': [10000, 200000],
        'StockSplits':[0,0],
        'Type':['Stock','Stock']
    })
    
write_data_to_sqlite(TickerPrice, data)