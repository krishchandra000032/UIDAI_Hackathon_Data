import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import os

INPUT_FILE = "final_master_dataset.csv"
OUTPUT_ANOMALY_FILE = "detected_anomalies.csv"
CONTAMINATION_LEVEL = 0.01  # We assume top 1% of data might be anomalies


def detect_anomalies():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found. Run the merge script first.")
        return

    print("Loading Master Dataset...")
    df = pd.read_csv(INPUT_FILE)

    age_cols = [c for c in df.columns if 'age' in c]
    df['total_transactions'] = df[age_cols].sum(axis=1)

    df = df.dropna(subset=['total_transactions'])

    X = df[['total_transactions']].values

    print(f"Training Isolation Forest on {len(df)} records...")

    iso_forest = IsolationForest(n_estimators=100, contamination=CONTAMINATION_LEVEL, random_state=42)

    preds = iso_forest.fit_predict(X)

    df['anomaly_status'] = preds
    df['anomaly_label'] = df['anomaly_status'].map({1: 'Normal', -1: 'Anomalous'})

    anomalies = df[df['anomaly_status'] == -1]
    normal = df[df['anomaly_status'] == 1]

    df.to_csv(OUTPUT_ANOMALY_FILE, index=False)

    print("-" * 30)
    print("DETECTION COMPLETE")
    print("-" * 30)
    print(f"Total Analyzed: {len(df)}")
    print(f"Normal Records: {len(normal)}")
    print(f"Suspicious Anomalies Detected: {len(anomalies)}")
    print(f"Saved results to: {OUTPUT_ANOMALY_FILE}")

    if not anomalies.empty:
        print("\nTop 5 Detected Anomalies (Highest Volume):")
        print(anomalies.sort_values(by='total_transactions', ascending=False)[
                  ['state', 'district', 'pincode', 'total_transactions', 'data_category']].head(5))


if __name__ == "__main__":
    detect_anomalies()