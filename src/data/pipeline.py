from pathlib import Path

from market_data import fetch_ohlcv


DATA_DIR = Path("data/raw")


def save_market_data(
    symbol="BTC/USDT",
    timeframe="1h",
    limit=500,
):
    df = fetch_ohlcv(
        exchange_name="binance",
        symbol=symbol,
        timeframe=timeframe,
        limit=limit,
    )

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    filename = (
        symbol.replace("/", "_")
        + "_"
        + timeframe
        + ".csv"
    )

    output_path = DATA_DIR / filename

    df.to_csv(
        output_path,
        index=False,
    )

    print(f"Saved {len(df)} rows")
    print(f"File: {output_path}")


if __name__ == "__main__":
    save_market_data()