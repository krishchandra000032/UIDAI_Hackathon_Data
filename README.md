# 🇮🇳 Aadhar Data Intelligence Suite (UIDAI Hackathon 2026)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Anomaly%20Detection-orange?style=for-the-badge&logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Hackathon%20Ready-success?style=for-the-badge)

## 📌 Project Overview
This repository hosts a comprehensive **Data Engineering & AI Pipeline** designed for the **UIDAI Hackathon 2026**. It tackles the challenge of processing massive, noisy Aadhar administrative datasets. The suite automates the journey from raw, inconsistent CSV files to high-level predictive insights.

**Key Capabilities:**
* **Fuzzy Cleaning:** Uses Levenshtein distance (`fuzzywuzzy`) to fix typo-riddled State/District names (e.g., merging "Maha rashtra" & "Maharashtra").
* **Unified Merging:** Intelligently combines Enrolment, Biometric, and Demographic datasets into a master file.
* **Fraud Detection:** An unsupervised Machine Learning model (**Isolation Forest**) to flag suspicious enrolment spikes ("Ghost Centres").
* **AI Forecasting:** A **Gradient Boosting Regressor** that predicts future footfall for 2026 based on seasonal patterns.

---

## 📂 Project Structure
```text
UIDAI_Hackathon_Project/
├── raw_data/                 # Place your original 10+ CSV files here
├── clean/                    # (Auto-generated) standardized CSVs
├── clean_data.py             # Script 1: Cleaning & Normalization
├── visualize_data.py         # Script 2: Before/After Cleaning Graphs
├── merge_data.py             # Script 3: Master Dataset Creation
├── trivariate_analysis.py    # Script 4: Demographic Insights
├── detect_fraud.py           # Script 5: Anomaly/Fraud Detection System
├── forecast_footfall.py      # Script 6: AI Prediction Model
├── final_master_dataset.csv  # (Output) The unified analysis file
├── detected_anomalies.csv    # (Output) List of suspicious transactions
├── README.md                 # Project Documentation
└── requirements.txt          # Python dependencies
