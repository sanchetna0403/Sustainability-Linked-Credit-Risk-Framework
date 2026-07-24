# Waste-to-Wealth Credit Optimizer

## Overview

The Waste-to-Wealth Credit Optimizer is a credit risk assessment system designed for recycling-sector businesses. The project evaluates financial performance, operational efficiency, and sustainability indicators to generate financing recommendations.

## Objective

To develop a data-driven framework that helps assess the creditworthiness of recycling companies and supports lending decisions using financial and environmental metrics.

## Tools Used

* Python
* MySQL
* Microsoft Excel (financial modeling: ratio analysis, rule-based credit scorecard, sensitivity analysis, dashboard)

## Dataset

A synthetic dataset of 500 recycling companies was generated using Python. The dataset includes:

* Company Information
* Annual Revenue
* Profit Margin
* Debt-to-Equity Ratio
* Cash Flow
* Credit Score
* Regulatory Compliance Score
* CO₂ Saved
* Waste Recycled
* Loan Amount Requested
* Risk Category

## Project Workflow

### 1. Data Generation

Generated a structured dataset containing financial, operational, and sustainability metrics.

### 2. Database Management

Imported data into MySQL and performed SQL-based analysis.

### 3. Credit Risk Assessment

Built a rule-based credit evaluation engine using:

* Credit Score
* Debt-to-Equity Ratio
* Regulatory Compliance Score
* Cash Flow

### 4. Loan Recommendation Engine

Classified companies into:

* Approved
* Manual Review
* Rejected

### 5. Analytics

Performed:

* Risk Analysis
* Credit Score Analysis
* Revenue Analysis
* Sustainability Performance Analysis

## Project Structure

```text
Waste_to_Wealth_Credit_Optimizer
│
├── data
├── outputs
├── python
├── sql
├── documentation
└── README.md
```

## Key Outcomes

* Automated credit assessment for 500 recycling companies.
* Generated loan approval recommendations.
* Integrated financial and sustainability indicators into decision-making.
* Performed SQL-based business analytics and reporting.
* Built a financial modeling layer in Excel with ratio analysis, a rule-based credit scorecard, and sensitivity analysis on lending thresholds.
* Identified that sustainability performance and credit risk are not directly correlated, reinforcing the need for multi-factor lending decisions.

## Skills Demonstrated

* Python Programming
* SQL
* Data Analytics
* Credit Risk Assessment
* Financial Analysis
* Business Intelligence
* Sustainability Analytics
* Financial Modeling
* Sensitivity Analysis
* Excel-based Rule Engine Design

### 6. Excel Financial Modeling Layer

To complement the Python/MySQL pipeline with hands-on financial modeling, a multi-sheet Excel workbook was built on top of the dataset:

* **Ratio Analysis** — Debt-to-Equity, Cash-Flow-to-Loan, and Profit Margin computed per company
* **Credit Scorecard** — a fully explainable, rule-based scoring engine built using nested IF/AND/OR formulas, replicating the credit decision logic directly in Excel (Approved / Manual Review / Rejected). This mirrors how credit risk systems are typically built in regulated lending environments, favoring transparency over black-box models.
* **Sensitivity Analysis** — a data table testing how the overall approval rate shifts as the Debt-to-Equity threshold is tightened or loosened, visualized as a line chart
* **Summary Dashboard** — KPI cards (total companies, approval rate, avg credit score, avg CO₂ saved by approved companies) plus charts for risk category distribution and average CO₂ saved by risk category

**Key insight:** Rejected companies had the *highest* average CO₂ saved (4451.72) compared to Approved companies (4275.59) — showing that strong environmental performance alone does not guarantee creditworthiness; financial health and regulatory compliance remain the primary drivers of the lending decision.
