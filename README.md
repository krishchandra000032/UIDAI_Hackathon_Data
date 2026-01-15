# 🇮🇳 Aadhar Data Intelligence Suite (UIDAI Hackathon 2026)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Anomaly%20Detection-orange?style=for-the-badge&logo=scikit-learn)


## 📌 Project Overview
This repository hosts a comprehensive **Data Engineering & AI Pipeline** designed for the **UIDAI Hackathon 2026**. It tackles the challenge of processing massive, noisy Aadhar administrative datasets. The suite automates the journey from raw, inconsistent CSV files to high-level predictive insights.

**Key Capabilities:**
* **Fuzzy Cleaning:** Uses Levenshtein distance (`fuzzywuzzy`) to fix typo-riddled State/District names.
* **Unified Merging:** Intelligently combines Enrolment, Biometric, and Demographic datasets.
* **Fraud Detection:** Unsupervised ML (**Isolation Forest**) to flag suspicious "Ghost Centres" (anomalous volume spikes).
* **AI Forecasting:** **Gradient Boosting** to predict future footfall for 2026 based on seasonal patterns.

---



Short description
This repository contains code, notebooks, and data assets used for the UIDAI hackathon — data processing, modeling experiments, and evaluation scripts for Aadhaar-related dataset tasks (preprocessing, feature engineering, modeling and evaluation). The project is Python-based.


### Table of contents
- Features
- Project structure
- Installation
- Quick start
- Examples (collapsible)
- Contributing
- License
- Contact

Features
- Data cleaning and preprocessing pipelines
- Exploratory notebooks and visualizations
- Model training and evaluation scripts
- Reproducible environment via requirements.txt / virtualenv

Project structure
The following is a suggested structure. Adjust to match the repository contents.

```text
UIDAI_Hackathon_Data/
├── README.md
├── LICENSE
├── requirements.txt
├── data/                     # Raw and processed datasets (not tracked if large)
│   ├── raw_data/
│   └── clean_data/
├── images/                   # PNGs and visualization assets
│   └── uidai-overview.png
├── src/                      # Source code (modules & scripts)
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── model.py
│   └── evaluate.py
├── scripts/                  # Convenience CLI scripts
│   └── train.sh
└── tests/                    # Unit / integration tests
    └── test_preprocessing.py
```

Installation
1. Clone the repository
```bash
git clone https://github.com/krishchandra000032/UIDAI_Hackathon_Data.git
cd UIDAI_Hackathon_Data
```

2. (Recommended) Create and activate a virtual environment
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If you do not have a requirements.txt, create one by inspecting the environment or by running:
```bash
pip freeze > requirements.txt
```

Quick start
- Run a notebook:
  - Open `notebooks/EDA.ipynb` with Jupyter or VS Code.
- Run preprocessing:
```bash
python -m src.preprocessing --input data/raw/myfile.csv --output data/processed/clean.csv
```
- Train a model:
```bash
python -m src.model --train data/processed/clean.csv --output models/model.pkl
```

Examples (collapsible)
<details>
<summary>Show example: minimal preprocessing script</summary>

```python
# src/preprocessing.py (example snippet)
import pandas as pd
from sklearn.impute import SimpleImputer

def load_data(path):
    return pd.read_csv(path)

def basic_cleaning(df):
    # drop duplicates
    df = df.drop_duplicates()
    # simple fill for numeric cols
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = SimpleImputer(strategy='median').fit_transform(df[num_cols])
    return df

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    df = load_data(args.input)
    df = basic_cleaning(df)
    df.to_csv(args.output, index=False)
    print(f"Saved cleaned data to {args.output}")
```
</details>

<details>
<summary>Show example: training CLI</summary>

```bash
# scripts/train.sh
#!/usr/bin/env bash
python -m src.model \
  --train data/processed/clean.csv \
  --epochs 50 \
  --batch-size 128 \
  --output models/uidai_model.pkl
```
</details>

---
### ℹ️ Visualization & InfoGraphics

### Aadhar Dataset (Raw Data Set VS Clean Data Set) 
('FuzzyWuzzy')
<img width="1400" height="600" alt="comparison_chart" src="https://github.com/user-attachments/assets/2b7c20c1-6afa-43fe-bd89-1ed20857b813" />

### 🧐 Analysis (Trivariate Analysis of Clean Data Set)

<img width="1000" height="600" alt="analysis_category_age_vol" src="https://github.com/user-attachments/assets/cb509b54-2272-40b0-b939-bffda446ba39" />

<img width="1200" height="800" alt="analysis_heatmap" src="https://github.com/user-attachments/assets/ec469a7c-36c8-4694-b84e-c2e16bde107b" />

<img width="1400" height="700" alt="analysis_state_category_vol" src="https://github.com/user-attachments/assets/62f7f477-6d75-40bc-9c5f-4a86ee496494" />

### 🧩 Anomalies (Fraud Detection and False Data) 
('Isolation forest')

<img width="1500" height="1000" alt="anomaly_report" src="https://github.com/user-attachments/assets/fba7817d-d005-4bc3-a17e-3f4ed79b8632" />

<img width="437" height="187" alt="top5anamolies1" src="https://github.com/user-attachments/assets/726def89-8ee7-49f4-a2e3-b9240f767a21" />

<img width="649" height="224" alt="top5anamolies 2" src="https://github.com/user-attachments/assets/c0015c64-c414-4402-9887-7cd1915e84cf" />

### ⌛️ Forecast (360 days prediction models) ('Footfall Forcaster')

<img width="1500" height="700" alt="forecast_2026" src="https://github.com/user-attachments/assets/1f7bb030-d30d-4444-bc49-58b06bdb4fc1" />

---

### Best practices & notes
- Do NOT commit large raw data files to the repository. Use .gitignore for data/.
- Add CI (GitHub Actions) to run tests and basic checks on PRs.
- Keep the requirements.txt minimal and pinned for reproducibility.

---

### ✉️ Contact

Maintainer: krishchandra000032 (krishuchandra1783@gmail.com)

Collaborater: Insaan01 (sakshamagarwal.octave@gmail.com)

Repository: https://github.com/krishchandra000032/UIDAI_Hackathon_Data

---

### 🏅 Acknowledgements
- UIDAI hackathon materials and collaborators
- Open-source libraries used (pandas, scikit-learn, numpy, matplotlib, etc.)

