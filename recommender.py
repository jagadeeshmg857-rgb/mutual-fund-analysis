import pandas as pd

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

risk = input("Enter Risk Level (Low/Moderate/High): ")

result = perf[
    perf["risk_grade"].str.lower() == risk.lower()
].sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print("\nTop 3 Recommended Funds:\n")
print(result[[
    "scheme_name",
    "fund_house",
    "sharpe_ratio",
    "risk_grade"
]])