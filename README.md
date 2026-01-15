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
├── clean_data/                    # (Auto-generated) standardized CSVs
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

---

## 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/UIDAI-Hackathon-Project.git](https://github.com/your-username/UIDAI-Hackathon-Project.git)
    cd UIDAI_Hackathon_Project
    ```

2.  **Install Dependencies**
    Ensure you have Python 3.8+ installed. Then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Data Setup**
    * Create a folder named `raw_data` in the root directory.
    * Place all your original Aadhar CSV files (Enrolment, Biometric, Demographic) inside `raw_data/`.

---

## 🛠️ Execution Pipeline

Run the scripts in this specific order to replicate the full analysis:

### **1. Data Cleaning**
Standardizes State/District names (e.g., merging "Maharashtra" & "Maha rashtra") and removes duplicates.
```bash
python clean_data.py
