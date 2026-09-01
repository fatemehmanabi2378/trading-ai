from market_data import fetch_ohlcv


df = fetch_ohlcv(
    exchange_name="binance",
    symbol="BTC/USDT",
    timeframe="1h",
    limit=10,
)

print(df)