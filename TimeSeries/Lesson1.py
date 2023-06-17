import pandas as pd

df = pd.read_csv("ALBRK.csv", index_col='Date', parse_dates=['Date'])
print(df.head())