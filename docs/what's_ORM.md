# Understanding ORM Models and SQL Table Mapping in SQLAlchemy

## What is an ORM Model?

**ORM (Object-Relational Mapping)** is a technique that allows developers to interact with a relational database using **Python objects** instead of writing raw SQL queries.

An **ORM model** is a Python class that represents a table in the database. Each class attribute corresponds to a column in the table, and each instance of the class represents a row in that table.

SQLAlchemy is a popular ORM library in Python that allows us to define and manipulate database tables using Python classes.

---

## How Does an ORM Model Map to an SQL Table?

When using SQLAlchemy ORM, each class definition maps to an actual table in the database. Here's how the mapping works:

### 1️⃣ Define an ORM Model (Python Class)

```python
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TickerPrice(Base):
    __tablename__ = "TickerPrice"  # This defines the table name

    Ticker = Column(String, primary_key=True)  # Stock symbol (e.g., "AAPL")
    Date = Column(Date, primary_key=True)  # Date of the stock price
    Close = Column(Float)  # Closing price of the stock
    Volume = Column(Integer)  # Number of shares traded
    StockSplits = Column(Integer)  # Stock splits if any
    Type = Column(String)  # Type of stock or classification
```

👉 **This Python class defines the structure of the `TickerPrice` table.**

---

### 2️⃣ How SQLAlchemy Maps This Model to an SQL Table

When you run SQLAlchemy with a database engine, it automatically translates the ORM model into an actual **SQL table** with the following structure:

```sql
CREATE TABLE TickerPrice (
    Ticker VARCHAR PRIMARY KEY,
    Date DATE PRIMARY KEY,
    Close FLOAT,
    Volume INTEGER,
    StockSplits INTEGER,
    Type VARCHAR
);
```

- `__tablename__ = "TickerPrice"` → Creates an SQL table named **TickerPrice**.
- Each `Column` in the class maps to a column in the SQL table.
- `primary_key=True` makes **Ticker + Date** a **composite primary key**.

---

### 3️⃣ Inserting Data Using ORM (Instead of Raw SQL)

Instead of writing raw SQL like:

```sql
INSERT INTO TickerPrice (Ticker, Date, Close, Volume, StockSplits, Type)
VALUES ('AAPL', '2024-02-14', 187.5, 5000000, 1, 'Equity');
```

You can use Python ORM:

```python
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import date

engine = create_engine("sqlite:///stocks.db")  # Create database engine
Session = sessionmaker(bind=engine)
session = Session()

# Create an ORM object (a row in the table)
new_stock = TickerPrice(
    Ticker="AAPL",
    Date=date(2024, 2, 14),
    Close=187.5,
    Volume=5000000,
    StockSplits=1,
    Type="Equity"
)

# Add to session and commit to database
session.add(new_stock)
session.commit()
```

✅ **No raw SQL needed! ORM handles it all.**

---

### 4️⃣ Querying Data Using ORM (Instead of Raw SQL)

Instead of writing:

```sql
SELECT * FROM TickerPrice WHERE Ticker = 'AAPL' AND Date = '2024-02-14';
```

You can use SQLAlchemy ORM:

```python
result = session.query(TickerPrice).filter_by(Ticker="AAPL", Date=date(2024, 2, 14)).first()
print(result.Close)  # Output: 187.5
```

✅ **Simplifies complex queries using Pythonic syntax!**

---

## Summary

| Feature        | ORM Model (Python)                 | SQL Table                              |
| -------------- | ---------------------------------- | -------------------------------------- |
| **Defined as** | Python class                       | SQL table                              |
| **Columns**    | Class attributes (`Column`)        | Table columns                          |
| **Rows**       | Class instances (objects)          | Table rows                             |
| **Queries**    | Python methods (`session.query()`) | SQL queries (`SELECT`, `INSERT`, etc.) |

This approach makes working with databases easier and more maintainable by using Python instead of raw SQL queries.
