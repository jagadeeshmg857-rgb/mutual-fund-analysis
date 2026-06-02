-- Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense Ratio Less Than 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;