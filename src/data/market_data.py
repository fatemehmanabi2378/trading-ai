import ccxt
import pandas as pd


def fetch_ohlcv(
    exchange_name="binance",
    symbol="BTC/USDT",
    timeframe="1h",
    limit=500,
):
    """
    Fetch OHLCV market data from a cryptocurrency exchange.

    Parameters
    ----------
    exchange_name : str
        Exchange name supported by CCXT.
    symbol : str
        Trading pair.
    timeframe : str
        Candle timeframe.
    limit : int
        Number of candles to fetch.

    Returns
    -------
    pandas.DataFrame
        OHLCV market data.
    """

    exchange_class = getattr(ccxt, exchange_name)
    exchange = exchange_class()

    ohlcv = exchange.fetch_ohlcv(
        symbol=symbol,
        timeframe=timeframe,
        limit=limit,
    )

    columns = [
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    df = pd.DataFrame(
        ohlcv,
        columns=columns,
    )

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        unit="ms",
        utc=True,
    )

    return df