import pandas as pd


FILE_PATH = "data/raw/BTC_USDT_1h.csv"


def validate_data(file_path):
    df = pd.read_csv(file_path)

    print("Dataset shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nData types:")
    print(df.dtypes)

    print("\nFirst rows:")
    print(df.head())


if __name__ == "__main__":
    validate_data(FILE_PATH)