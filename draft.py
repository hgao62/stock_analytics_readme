
from typing import Optional
import pandas as pd
import yfinance as yf
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
    stock = yf.Ticker(ticker)
    df = stock.history('1d')
    pe = stock.info['trailingPE']


if __name__ == "__main__":
    fetch_stock_data("AAPL", period="1d")