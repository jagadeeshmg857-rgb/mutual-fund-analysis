import pandas as pd

# Load dataset
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort by AMFI code and date
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Keep valid NAV values
nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("Cleaning completed")
print("Rows:", len(nav))

import pandas as pd

# ---------- NAV History ----------
nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

# ---------- Scheme Performance ----------
perf = pd.read_csv("data/raw/07_scheme_performance.csv")

perf = perf.drop_duplicates()

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense ratio validation
perf = perf[
    (perf["expense_ratio_pct"] >= 0.1) &
    (perf["expense_ratio_pct"] <= 2.5)
]

perf.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance cleaned")

# ---------- Investor Transactions ----------

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn = txn.drop_duplicates()

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn = txn[txn["amount_inr"] > 0]

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.title()
)

txn.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions cleaned")