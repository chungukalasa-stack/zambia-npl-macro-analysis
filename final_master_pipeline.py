import pandas as pd
import numpy as np

print("\n" + "="*60)
print("     ZAMBIA NPL EXPLORATORY DATA ENGINE & LAGGED ANALYSIS    ")
print("============================================================")

data = {
    'Year':               [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
    'USD_ZMW_Avg':        [4.80,4.86,5.15,5.39,6.15,8.63,10.31,9.53,10.50,12.89,18.34,19.70,16.96,19.82,26.01,26.63],
    'WB_NPL_Percentage':  [13.5,11.2,8.1,7.0,6.1,7.3,9.7,11.8,11.5,8.9,11.2,5.9,4.4,4.3,5.1,4.8],
    'Inflation_Rate_YoY': [8.5,6.4,6.6,7.0,7.8,10.1,17.9,6.6,7.5,9.2,15.7,22.0,11.0,10.9,13.9,13.1],
    'Log_GDP':            [23.728948,23.880266,23.961944,24.055470,24.022800,23.777267,23.763015,23.977509,23.992835,23.871719,23.619178,23.818843,24.097435,24.062588,24.007929,24.000411]
}

df = pd.DataFrame(data)
required_cols = ['USD_ZMW_Avg', 'WB_NPL_Percentage', 'Inflation_Rate_YoY', 'Log_GDP']

# PART 1: SYSTEMIC DESCRIPTIVE SUMMARY
print("\n[PART 1] DESCRIPTIVE BASELINES")
print("-" * 55)
print(df[required_cols].describe().T[['mean', 'std', 'min', 'max']])

# PART 2: WEEK 3 STRATEGIC LAGGED CORRELATION ANALYSIS (REPLACES PREMATURE OLS)
print("\n[PART 2] LAGGED FX CORRELATION ANALYSIS (TARGET: CURRENT NPL)")
print("-" * 55)
for lag in [0, 1, 2]:
    df[f'FX_Lag{lag}'] = df['USD_ZMW_Avg'].shift(lag)
    corr_val = df['WB_NPL_Percentage'].corr(df[f'FX_Lag{lag}'])
    n_size = len(df) - lag
    print(f"  FX (t-{lag}) vs NPL (t) Response: r = {corr_val:+.4f}  (n={n_size})")

# PART 3: TEXT VISUAL TRAJECTORY AREA
print("\n[PART 3] TEXT GRAPH TRAJECTORY AREA")
print("-" * 55)
for year, npl in zip(df['Year'], df['WB_NPL_Percentage']):
    print(f"  {year} ({npl:>4}%) | " + ("*" * int(npl * 2)))
print("-" * 55)
print("  SCALE BASEL  | 0%----5%----10%----15%")

print("\n============================================================")
print("[+] Execution Successful. Ready for Repository Staging.")
print("============================================================")
