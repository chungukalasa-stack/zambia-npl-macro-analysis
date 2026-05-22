# Assessing the Macroeconomic Drivers of Asset Quality in Zambia (2010–2025)

An analyst-grade econometric project exploring the transmission channels between macroeconomic shocks (Exchange Rates, Inflation, GDP) and commercial banking asset quality—measured via Non-Performing Loans (NPLs)—using data from the Bank of Zambia (BoZ), IMF, and World Bank.

## 📊 Core Findings & Executive Summary
Contrary to standard macroeconomic theory which suggests that local currency depreciation creates a delayed spike in credit defaults, this empirical analysis demonstrates **zero delayed transmission** from the Kwacha exchange rate to bank NPLs in Zambia. 

Lagged correlation analysis across $t-0$, $t-1$, and $t-2$ horizons yields static correlations of `-0.5717`, `-0.5684`, and `-0.5592` respectively. This marginal weakening confirms that the signal is dominated by a structural historical time trend (simultaneous long-term BoZ supervisory improvements and Kwacha depreciation) rather than a direct causal channel. The data strongly suggests that Zambian commercial banks proactively restructure credit exposure immediately during currency shocks rather than letting losses accumulate over multi-year horizons.

### The Three-Phase Credit Cycle Architecture
Our exploratory trajectory analysis isolates three clear historical regimes in Zambia's credit landscape:
1. **2010–2014 (Sharp Compression):** NPLs drop drastically from `13.5%` to `6.1%`, reflecting a massive post-Global Financial Crisis (GFC) balance sheet cleanup.
2. **2015–2020 (Dual Stress Cycles):** Volatility driven by the 2015/2016 Kwacha power-crisis shocks and the 2020 COVID-19 economic disruptions.
3. **2021–2025 (The New Supervisory Baseline):** Structural stabilization of NPLs around a highly disciplined `4%` to `5%` floor, driven by modernized central bank macroprudential frameworks.

---

## 📁 Repository Structure
* `final_master_pipeline.py`: The core operational script handling descriptive summary statistics, the Week 3 Lagged Correlation Engine, and text-based trajectory matrix generation.
* `macro_eda.py`: Baseline reference script hosting the initial un-lagged/lagged OLS regression models and diagnostic metadata warnings.
* `Zambia_Macro_Data_Clean.xlsx`: Compiled operational database dataset (2010-2025).

---

## 🛠️ Diagnostic & Econometric Constraints
Any realistic exploration of this dataset must account for severe small-sample time-series constraints ($n=16$):
* **Degrees of Freedom Limit:** Loading a multi-variable OLS regression with 3 independent variables onto 15 usable rows drops residual degrees of freedom to $df=11$, inflating standard errors and rendering individual p-values unreliable.
* **Multicollinearity:** Baseline OLS runs flag an extreme Condition Number exceeding **5,500**, confirming severe co-movement between `Log_GDP` and `USD_ZMW_Avg`.
* **Serial Correlation:** A Durbin-Watson statistic of `0.959` indicates lingering cyclical patterns, verifying that a standard linear time-series framework cannot substitute for comprehensive panel-data methods.

---

## 🚀 How to Run the Workspace Engines
Ensure you have `pandas`, `numpy`, and `statsmodels` installed in your Python environment.

```bash
pip install pandas numpy statsmodels

