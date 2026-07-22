from twelvedata import TDClient
from pprint import pprint

import dotenv
import os

dotenv.load_dotenv()

API_KEY = os.getenv("TWELVE_DATA_API_KEY")

# td = TDClient(apikey=API_KEY)

# ts = td.time_series(
#     symbol="EUR/USD",
#     interval="1day",      # 1min, 5min, 15min, 1h, 1day, etc.
#     outputsize=100
# )

# df = ts.as_pandas()

# print(df.head())

from pathlib import Path

# Get the script's directory
script_dir = Path(__file__).parent.resolve()

# Go up one level (..) and into 'storage'
storage_dir = script_dir.parent / "storage"

print(storage_dir)
# df.to_csv("eurusd_1min.csv", index=True)