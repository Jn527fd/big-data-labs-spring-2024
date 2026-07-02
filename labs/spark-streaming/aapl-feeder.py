#!/usr/bin/env python3
import time
from pathlib import Path

import pandas as pd

repo_root = Path(__file__).resolve().parents[2]
aapl_path = repo_root / 'data' / 'samples' / 'aapl.csv'

aapl_df = pd.read_csv(aapl_path)
aapl_df.dropna(inplace=True)
aapl_df = aapl_df.loc[:,['Date', 'Close/Last']]
aapl_df = aapl_df.iloc[::-1]

for _, row in aapl_df.iterrows():
    print(row['Date'], row['Close/Last'], flush = True)
    time.sleep(1.0)
