import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
import datetime
import os


INPUT_FILE = "final_master_dataset.csv"
OUTPUT_IMG = "forecast_2026.png"




def create_features(df):
    """
    Creates time-series features for the Machine Learning model.
    """
    df = df.copy()
    df['day_of_year'] = df['date'].dt.dayofyear
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.dayofweek
    df['sin_day'] = np.sin(2 * np.pi * df['day_of_year'] / 365.0)
    df['cos_day'] = np.cos(2 * np.pi * df['day_of_year'] / 365.0)
    return df




def run_forecast():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    print("Loading data and training AI model...")

    df = pd.read_csv(INPUT_FILE)

    count_cols = [c for c in df.columns if 'age' in c or 'count' in c]

    if not count_cols:
        count_cols = df.select_dtypes(include=np.number).columns.tolist()

    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')
    df.dropna(subset=['date'], inplace=True)

    daily_df = df.groupby('date')[count_cols].sum().sum(axis=1).reset_index(name='daily_traffic')
    daily_df = daily_df.sort_values('date')

    train_df = create_features(daily_df)
    features = ['day_of_week', 'month', 'sin_day', 'cos_day']

    X = train_df[features]
    y = train_df['daily_traffic']

    model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)
    model.fit(X, y)

    last_date = daily_df['date'].max()
    future_dates = [last_date + datetime.timedelta(days=x) for x in range(1, 366)]
    future_df = pd.DataFrame({'date': future_dates})
    future_df = create_features(future_df)

    future_df['predicted_traffic'] = model.predict(future_df[features])

    plt.figure(figsize=(15, 7))

    plt.plot(daily_df['date'], daily_df['daily_traffic'],
             label='Historical (Actual)', color='gray', alpha=0.4)

    plt.plot(future_df['date'], future_df['predicted_traffic'],
             label='AI Forecast (Next Year)', color='#007acc', linewidth=2)


    plt.plot(future_df['date'], future_df['predicted_traffic'].rolling(30).mean(),
             label='Trend (30-Day Avg)', color='navy', linestyle='--', linewidth=2)

    plt.title('Aadhar Centre Footfall Forecast: 2026 Projections', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('Daily Transactions')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_IMG)

    print("-" * 30)
    print("FORECAST COMPLETE")
    print("-" * 30)
    print(f"Projected Total Footfall (Next Year): {int(future_df['predicted_traffic'].sum()):,}")
    print(f"Graph saved to: {OUTPUT_IMG}")


if __name__ == "__main__":
    run_forecast()