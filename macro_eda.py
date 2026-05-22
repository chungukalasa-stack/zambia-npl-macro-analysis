import pandas as pd
import numpy as np
import statsmodels.api as sm

print("\n" + "="*60)
print("   ZAMBIA MACROECONOMIC REGRESSION WORKSTATION (BASELINE REFERENCES)   ")
print("============================================================")

data = {
    'Year':               [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025],
    'USD_ZMW_Avg':        [4.80,4.86,5.15,5.39,6.15,8.63,10.31,9.53,10.50,12.89,18.34,19.70,16.96,19.82,26.01,26.63],
    'WB_NPL_Percentage':  [13.5,11.2,8.1,7.0,6.1,7.3,9.7,11.8,11.5,8.9,11.2,5.9,4.4,4.3,5.1,4.8],
    'Inflation_Rate_YoY': [8.5,6.4,6.6,7.0,7.8,10.1,17.9,6.6,7.5,9.2,15.7,22.0,11.0,10.9,13.9,13.1],
    'Nominal_GDP_USD':    [2.02e10,2.35e10,2.55e10,2.80e10,2.71e10,2.12e10,2.09e10,2.59e10,2.63e10,2.33e10,1.81e10,2.21e10,2.92e10,2.82e10,2.67e10,2.65e10],
    'Log_GDP':            [23.728948,23.880266,23.961944,24.055470,24.022800,23.777267,23.763015,23.977509,23.992835,23.871719,23.619178,23.818843,24.097435,24.062588,24.007929,24.000411]
}

df = pd.DataFrame(data)

# Generate 1-Year Lagged Matrix
df['Lagged_USD_ZMW'] = df['USD_ZMW_Avg'].shift(1)
df['Lagged_Inflation'] = df['Inflation_Rate_YoY'].shift(1)
df_clean = df.dropna().copy()

# OLS Variable Definition
Y = df_clean['WB_NPL_Percentage']
X = df_clean[['Lagged_USD_ZMW', 'Lagged_Inflation', 'Log_GDP']]
X = sm.add_constant(X)

lagged_model = sm.OLS(Y, X).fit()

print("\n--- CRITICAL DIAGNOSTIC MODEL SUMMARY ---")
print(lagged_model.summary())
print("\n[!] WARNING: Low Degrees of Freedom (df=11). Model overfitted.")
print("[!] WARNING: Condition Number indicates severe multicollinearity.")
