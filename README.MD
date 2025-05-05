

1. python 3.11(版本一定要对，超级重要！)
下载链接：https://www.python.org/downloads/release/python-3110/
2. Visual studio code(代码开发IDE)
下载链接：https://code.visualstudio.com/download
3. Github account
注册链接：https://github.com/
4. Gmail邮箱(自动化发邮件用)
5. teams（上课用）
下载链接：https://www.microsoft.com/en-ca/microsoft-teams/download-app
6. obs(用来录频，便于自己复习回顾上课的内容）
下载链接：https://obsproject.com/download

把邮箱发我建repo, 添加collaborator

### Lesson1: Self Learning
1. what is a virtual environment
https://www.youtube.com/watch?v=Y21OR1OPC9A

2. Github 101
https://www.youtube.com/watch?v=SD7YNLv5Evc



### Lesson 2
1. create virtual environment by running command(finish watching video above what is a virtual environment)
```
python -m venv venv
```
2. activate your virtual environment

on Windows, run command below in your project root directory terminal(see my screenshot below)

```
venv\Scripts\activate
```

![alt text](image-1.png)

macOS,  run command below in your project root directory terminal


```
source venv/bin/activate
```

3. copy the requirements.txt in this repo to your project root directory

4. run command below(this install all the project dependencies listed in requirements.txt)
```
pip install -r requirements.txt
```

5. copy yahoo_finance_api_usage_example.py to your project root directory and run it and you should see the data output

#### Task 1. create a file called utilities.py and create function called fetch stock data in utilities.py
```python
def fetch_stock_data(
    ticker: str,
    period: Optional[str] = None,
    start_date: Optional[pd.Timestamp] = None,
    end_date: Optional[pd.Timestamp] = None,
) -> pd.DataFrame:
    """
    Fetch historical stock data for a specific ticker from Yahoo Finance.

    Parameters:
        ticker (str): Stock ticker symbol.
        period (Optional[str]): Period string for Yahoo Finance API (e.g., '1mo', '3mo', '1y').
        start_date (Optional[str]): Start date for fetching data.
        end_date (Optional[str]): End date for fetching data.

    Returns:
        pd.DataFrame: DataFrame with historical stock data.
    """

```
It should Output dataframe like below, for example fetch_stock_data("AAPL", period="1d")
should produce result in this screenshot
![alt text](image-2.png)

fetch_stock_data("AAPL", start_date=pd.Timestamp("2021-01-01"), end_date=pd.Timestamp("2021-01-31")) should looks like this below
![alt text](image-3.png)

### Lesson 3
1. install sqlite

What's ORM ?

ORM (Object-Relational Mapping) is a technique that allows developers to interact with a relational database using Python objects instead of writing raw SQL queries.

An ORM model is a Python class that represents a table in the database. Each class attribute corresponds to a column in the table, and each instance of the class represents a row in that table.

SQLAlchemy is a popular ORM library in Python that allows us to define and manipulate database tables using Python classes.

2. create database model
```
from sqlalchemy import Column, Integer, String, Float, Date, MetaData, Table, ForeignKey
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


class TickerInfo(Base):
    __tablename__ = 'TickerInfo'
    Ticker = Column(String, primary_key=True)
    CompanyName = Column(String)
    Sector = Column(String)
    Industry = Column(String)
    Country = Column(String)
    MarketCap = Column(Float)
    PERatio = Column(Float)
    ForwardPERatio = Column(Float)
    Dividend = Column(Float)
    ROE = Column(Float)
    ROA = Column(Float)
    Description = Column(String)
    Website = Column(String)
    LastUpdated = Column(Date)


class SP500Holdings(Base):
    __tablename__ = TableList.SP500_HOLDINGS
    Ticker = Column(String, primary_key=True)
    Sector = Column(String)
    Industry = Column(String)
    CompanyName = Column(String)
    
```

alembic init alembic

alembic revision --autogenerate -m "Initial migration"

alembic upgrade head


3. create a folder called sqlitedb, inside this folder create a file called write.py and create a function called 
```python
def write_data_to_sqlite(model: DeclarativeBase, data: pd.DataFrame) -> None:
    """
    Write data to a SQLite table using ORM model.
    
    Parameters:
        model: SQLAlchemy ORM model.
        data (pd.DataFrame): DataFrame containing the data to write.
    """
    session = Session()
    try:

        records = data.to_dict(orient='records')
        session.bulk_insert_mappings(model, records)
        session.commit()
        print(f"Data written to table {model.__tablename__} successfully.")
    except Exception as e:
        logger.error(f"Error writing data to SQLite table {model.__tablename__}: {e}")

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

```
4. create a file called read.py and create a function called read_data_from_sqlite
```python
def read_data_from_sqlite(model, filters: Dict[str,any]= None,date_range: Tuple[str, str] = None) -> pd.DataFrame:
   
    """
    Read data from a SQLite table using ORM model with optional filters and date range.
    
    Parameters:
        model: SQLAlchemy ORM model.
        filters (Dict[str, any]): Dictionary of column-value pairs for filtering.
        date_range (Tuple[str, str]): Tuple containing the start and end dates for filtering.
        columns_to_select (Optional[List[str]]): List of columns to select.
        is_distinct (Optional[bool]): Whether to select distinct rows.
    
    Returns:
        pd.DataFrame: DataFrame containing the query results.
    """
   
    return df
```
### Lesson 4
5. create a function called ticker_data_processing in main.py
```python
def ticker_data_processing(
    mode: str,
    ticker: str,
    model,
    start_date: Optional[pd.Timestamp] = None,
    end_date: Optional[pd.Timestamp] = None,
    longest_period: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetch ticker data based on the mode and return all data for that ticker 

    Parameters:
        mode (str): 'initial', 'daily', or 'rerun'
        start_date (Optional[pd.Timestamp]): Start date for rerun mode.
        end_date (Optional[pd.Timestamp]): End date for rerun mode.

    Returns:
        pd.DataFrame: DataFrame with ticker data.
    """
    # if mode is "initial":
        # fetch data using longest_period( 1y, 3y, etc)
        # write to sqlite db(calling the function you just created in step 1)
    
    # if mode is daily:
       # fetch data for just 1 day
       # write to db

    # if mode is rerun:
      # fetch stock data for start date and end date
      # upsert data to sqlite using the upsert_data_in_sqlite function below already created for you
      # put the upsert_data_in_sqlite function in write.py




def upsert_data_in_sqlite(model, set_values: dict, filters: dict=None, date_range: tuple = None) -> None:
    """
    Upsert data in a SQLite table using ORM model.
    
    Parameters:
        model: SQLAlchemy ORM model.
        set_values (dict): Dictionary of column-value pairs to set.
        filters (dict): Dictionary of column-value pairs for the WHERE clause.
        date_range (tuple): Tuple containing the start and end dates for filtering.
    """
    if not filters and not date_range:
        raise ValueError("A WHERE clause or date range must be provided to upsert data.")

    session = Session()
    try:
        query = session.query(model)
        if date_range:
            start_date, end_date = date_range
            query = query.filter(model.Date.between(start_date, end_date))
        
        if filters:
            for column, value in filters.items():
                query = query.filter(getattr(model, column) == value)
        
        existing_record = query.first()
        if existing_record:
            query.update(set_values)
            print(f"Data updated in table {model.__tablename__} successfully.")
        else:
            new_record = model(**set_values)
            session.add(new_record)
            print(f"Data inserted into table {model.__tablename__} successfully.")
        
        session.commit()
    except Exception as e:
        print(f"Error upserting data in SQLite table {model.__tablename__}: {e}")
    finally:
        session.close()
```


### Lesson 5
Create the calculate_returns function to calculate stock return
```python
def calculate_returns(
    df: pd.DataFrame, periods: list, period_days, ticker: str, report_date: pd.Timestamp
) -> dict:
    """
    Calculate returns for specified periods.

    Parameters:
        df (pd.DataFrame): DataFrame with an 'Adj Close' column.
        periods (list): List of periods for which to calculate returns.
        period_days (dict): Dictionary mapping periods to days.
        ticker (str): Stock ticker symbol.

    Returns:
        dict: Dictionary of returns for each period.
    """
    returns = {"Ticker": ticker}

    for period in periods:
        try:
            if period in ['1d', '3d', '5d']:
                # Use trading days for 1d, 3d, 5d periods
                start_date = report_date 
                trading_days = 0 # <=
                period_days = {'1d':1, '3d':3, '5d':5, '1y':365}
                while trading_days < period_days[period]: 
                    start_date -= timedelta(days=1) 
                    if start_date.weekday() < 5:  # Monday to Friday are trading days
                        trading_days += 1
                start_date = start_date.date()
            else:
                start_date = (report_date - timedelta(days=period_days[period])).date()
        except Exception as e:
            logger.error(
                f"Error calculating start_date for {ticker} during {period}: {e}"
            )
            print(f"Error calculating start_date for {ticker} during {period}: {e}")
            returns[f"{period}_return"] = 0
            continue  # Skip to the next period

        # Convert start_date to pandas Timestamp and normalize
        # start_date_normalized = pd.Timestamp(start_date).normalize().tz_localize('UTC')
        # Normalize dates to ignore timezone and other attributes
        report_date_data = df[df["Date"] == report_date.date()]["Close"]
        if report_date_data.empty:
            logger.error(f"No data found for {ticker} on {report_date.date()}")
            print(f"No data found for {ticker} on {report_date.date()}")
            raise Exception(f"No data found for {ticker} on {report_date.date()}")
        else:
            
            report_date_price = report_date_data.values[0]
        if start_date in df["Date"].values:
            try:

                lookback_date_price = df[df["Date"] == start_date]["Close"].values[0]
                returns[f"{period}_return"] = round(
                    (report_date_price / lookback_date_price - 1), 4
                )
            except Exception as e:
                logger.error(
                    f"Error calculating return for {ticker} during {period}: {e}"
                )
                print(f"Error calculating return for {ticker} during {period}: {e}")
                returns[f"{period}_return"] = 0
        else:
            # If start date is not in the data, calculate the return using the closest available date
            neighbour_days = get_neighbour_days(start_date)
            for adj_lookback_date in neighbour_days:
                if adj_lookback_date in df["Date"].values:
                    try:
                        lookback_date_price = df[df["Date"] == adj_lookback_date][
                            "Close"
                        ].values[0]
                        returns[f"{period}_return"] = round(
                            (report_date_price / lookback_date_price - 1), 4
                        )
                        break
                    except Exception as e:
                        logger.error(
                            f"Error calculating return for {ticker} on {adj_lookback_date} during {period}: {e}"
                        )
                        returns[f"{period}_return"] = pd.NA
                        continue
            else:
                returns[f"{period}_return"] = 0
    return returns
```


### Lesson 6

Finish top_gainers functions below
```Python
def get_top_gainers(
    tickers: list,
    lookback_periods: list,
    mode: str,
    all_tickers: List[str],
    start_date: Optional[pd.Timestamp] = None,
    end_date: Optional[pd.Timestamp] = None,
    benchmark_against_sp500: bool = True,
) -> pd.DataFrame:
    logger.info(f"Running get_top_gainers in '{mode}' mode.")
    """
    Screen top gainers for a list of tickers over specified lookback periods,
    including S&P 500 returns for each period.

    Parameters:
        tickers (list): List of stock tickers.
        lookback_periods (list): List of periods for which to calculate returns.
        mode (str): 'initial', 'daily', or 'rerun'
        start_date (Optional[str]): Start date for rerun mode.
        end_date (Optional[str]): End date for rerun mode.

    Returns:
        pd.DataFrame: DataFrame with returns for each ticker and time period,
                      including S&P 500 returns.
    """


def enrich_with_sector_industry(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enrich the DataFrame with sector and industry information.

    Parameters:
        df (pd.DataFrame): DataFrame with stock data.
        info_path (str): Path to the CSV file containing sector and industry information.

    Returns:
        pd.DataFrame: Enriched DataFrame with sector and industry columns.
    """


```
