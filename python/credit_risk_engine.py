import pandas as pd
import os

print("Script started")
print("Current working directory loaded")

# Load dataset
df = pd.read_excel("data/recycling_credit_data.xlsx")

# Credit Risk Decision Engine
def loan_decision(row):

    score = row["Credit_Score"]
    debt = row["Debt_to_Equity"]
    compliance = row["Regulatory_Compliance_Score"]
    cashflow = row["Cash_Flow_USD"]

    # Strong companies
    if score >= 70 and debt <= 1 and compliance >= 60:
        return "Approved"
    elif score < 50 or debt > 2:
        return "Rejected"
    else:
        return "Manual Review"


# Apply model
df["Loan_Decision"] = df.apply(
    loan_decision,
    axis=1
)

# KPIs
total_companies = len(df)

approved = (
    df["Loan_Decision"] == "Approved"
).sum()

rejected = (
    df["Loan_Decision"] == "Rejected"
).sum()

manual_review = (
    df["Loan_Decision"] == "Manual Review"
).sum()

approval_rate = round(
    approved / total_companies * 100,
    2
)

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Save final analysis
df.to_excel(
    "outputs/recycling_credit_analysis.xlsx",
    index=False
)

# Print results
print("\n========== SUSTAINABILITY-LINKED CREDIT RISK FRAMEWORK ==========\n")

print(f"Total Companies Evaluated : {total_companies}")
print(f"Approved                  : {approved}")
print(f"Rejected                  : {rejected}")
print(f"Manual Review             : {manual_review}")
print(f"Approval Rate             : {approval_rate}%")

print("\nLoan Decision Breakdown:")
print(df["Loan_Decision"].value_counts())

print("\nAnalysis file saved:")
print("outputs/recycling_credit_analysis.xlsx")