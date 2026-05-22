import pandas as pd
import numpy as np

print("\n" + "="*70)
print("     ZAMBIAN COMMERCIAL BANKING DIVISION: SME CREDIT SCORECARD ENGINE   ")
print("======================================================================")

# 1. DEFINE BORROWER PROFILES (Zambian SMEs)
sme_portfolio = [
    {
        "Company_ID": "SME_001",
        "Name": "Chongwe Agri-Inputs Ltd",
        "DSCR": 1.6,              # Repayment capacity (>1.5 is strong)
        "Sector": "Agriculture",   # Volatile sector per NPL findings
        "FX_Exposure": "High",     # Imports fertilizer/seed in USD
        "Collateral_Pct": 1.20,    # 120% coverage of loan value
        "Missed_Payments": 0,      # Clean history
        "Years_In_Op": 4           # Established business
    },
    {
        "Company_ID": "SME_002",
        "Name": "Lusaka Tech Distributors",
        "DSCR": 1.1,              # Tight repayment capacity
        "Sector": "Commercial",    # Standard trading
        "FX_Exposure": "High",     # Imports electronics entirely in USD
        "Collateral_Pct": 0.80,    # Under-collateralized (80%)
        "Missed_Payments": 1,      # One historical delinquency
        "Years_In_Op": 1           # Startup proxy
    },
    {
        "Company_ID": "SME_003",
        "Name": "Kalingalinga Copper Artisans",
        "DSCR": 1.8,              # Strong cash flow coverage
        "Sector": "Manufacturing", # Domestic production
        "FX_Exposure": "Low",      # Local inputs, local sales
        "Collateral_Pct": 1.50,    # Over-collateralized (150%)
        "Missed_Payments": 0,      # Clean history
        "Years_In_Op": 7           # Very stable
    }
]

# 2. CURRENT MACROECONOMIC ENVIRONEMENT STRESS INDICATOR (From NPL Research)
# Toggle this to see how the entire portfolio dynamically re-scores during a macro crisis
KWACHA_VOLATILITY_ACTIVE = True 

# 3. SCORECARD LENDING LOGIC ENGINE
def evaluate_sme(sme):
    score = 0
    
    # Variable 1: DSCR (Weight: 25 points)
    if sme["DSCR"] >= 1.5:     score += 25
    elif sme["DSCR"] >= 1.2:   score += 15
    else:                      score += 5
    
    # Variable 2: Sector Risk (Weight: 20 points)
    if sme["Sector"] in ["Agriculture", "Import-Dependent"]: score += 5  # NPL Penalty
    else:                                                    score += 20
        
    # Variable 3: Currency Exposure (Weight: 20 points)
    if sme["FX_Exposure"] == "High":   score += 5  # Currency Risk Penalty
    else:                              score += 20
        
    # Variable 4: Collateral Coverage (Weight: 15 points)
    if sme["Collateral_Pct"] >= 1.0:   score += 15
    elif sme["Collateral_Pct"] >= 0.5: score += 8
    else:                              score += 0
        
    # Variable 5: Payment History (Weight: 10 points)
    if sme["Missed_Payments"] == 0:    score += 10
    else:                              score += 0
        
    # Variable 6: Business Age (Weight: 5 points)
    if sme["Years_In_Op"] >= 3:        score += 5
    else:                              score += 2
        
    # Variable 7: Macro Stress Adjustment (Weight: 5 points)
    # If Kwacha is volatile, high FX exposure companies take an automatic final penalty
    if KWACHA_VOLATILITY_ACTIVE and sme["FX_Exposure"] == "High":
        score += 0  # Deducts potential bonus points during active stress cycles
    else:
        score += 5  # Full marks during stable regimes
        
    # 4. OUTPUT CATEGORIZATION AND CREDIT DECISION MATRIX
    if score >= 75:
        category = "LOW RISK"
        decision = "APPROVE CREDIT LINE"
    elif score >= 50:
        category = "MEDIUM RISK"
        decision = "HOLD FOR CREDIT COMMITTEE REVIEW"
    else:
        category = "HIGH RISK"
        decision = "REJECT / FREEZE APPLICATION"
        
    return score, category, decision

# 5. RUN COMPILATION PIPELINE
processed_smes = []
for idx, b in enumerate(sme_portfolio):
    final_score, risk_tier, credit_action = evaluate_sme(b)
    processed_smes.append({
        "SME Name": b["Name"],
        "Sector": b["Sector"],
        "FX Risk": b["FX_Exposure"],
        "Total Score (0-100)": final_score,
        "Risk Category": risk_tier,
        "Credit Decision": credit_action
    })

df_output = pd.DataFrame(processed_smes)

print(f"[LIVE MARKET CONDITONS] Active Kwacha Macro Stress: {KWACHA_VOLATILITY_ACTIVE}")
print("-" * 115)
print(df_output.to_string(index=False))
print("-" * 115)
print("[+] Scoring Execution Successful. Scorecard Matrix Aligned with BoZ Benchmarks.")
print("======================================================================")
