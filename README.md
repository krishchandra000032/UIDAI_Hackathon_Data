# 🇮🇳 Aadhar Data Intelligence Suite (UIDAI Hackathon 2026)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Anomaly%20Detection-orange?style=for-the-badge&logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Hackathon%20Ready-success?style=for-the-badge)

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
│   ├── raw/
│   └── processed/
├── images/                   # PNGs and visualization assets
│   └── uidai-overview.png
├── notebooks/                # Jupyter notebooks for exploration
│   └── EDA.ipynb
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

#Aadhar Dataset (Raw Data Set VS Clean Data Set)
<img width="1400" height="600" alt="comparison_chart" src="https://github.com/user-attachments/assets/2b7c20c1-6afa-43fe-bd89-1ed20857b813" />


Best practices & notes
- Do NOT commit large raw data files to the repository. Use .gitignore for data/.
- Add CI (GitHub Actions) to run tests and basic checks on PRs.
- Keep the requirements.txt minimal and pinned for reproducibility.

Contributing
1. Fork the repo
2. Create a feature branch: git checkout -b feat/my-feature
3. Make changes and add tests
4. Open a PR with a clear description of changes

License
If you have a preferred license, add a LICENSE file in the repo root. The badge above will reflect the chosen license. If none is specified, add one (e.g., MIT) to clarify reuse terms.

Contact

Maintainer: krishchandra000032 (krishuchandra1783@gmail.com)

Collaborater: Insaan01 (sakshamagarwal.octave@gmail.com)

Repository: https://github.com/krishchandra000032/UIDAI_Hackathon_Data

Acknowledgements
- UIDAI hackathon materials and collaborators
- Open-source libraries used (pandas, scikit-learn, numpy, matplotlib, etc.)

