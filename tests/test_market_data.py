from src.data.market_data import fetch_ohlcv


def test_fetch_ohlcv():
    df = fetch_ohlcv(
        exchange_name="binance",
        symbol="BTC/USDT",
        timeframe="1h",
        limit=10,
    )

    assert len(df) == 10

    expected_columns = [
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    assert list(df.columns) == expected_columns