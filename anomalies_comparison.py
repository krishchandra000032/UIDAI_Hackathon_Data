import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

INPUT_FILE = "detected_anomalies.csv"


def plot_anomalies():
    if not os.path.exists(INPUT_FILE):
        print("Run the detection script first!")
        return

    df = pd.read_csv(INPUT_FILE)


    anomalies = df[df['anomaly_label'] == 'Anomalous']
    normal = df[df['anomaly_label'] == 'Normal']

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 1, 1)

    plt.scatter(normal.index, normal['total_transactions'],
                c='blue', alpha=0.3, s=10, label='Normal Traffic')

    plt.scatter(anomalies.index, anomalies['total_transactions'],
                c='red', alpha=0.8, s=30, marker='x', label='Anomalous Activity')

    plt.title('Anomaly Detection: Transaction Volume Outliers', fontsize=14)
    plt.xlabel('Record Index')
    plt.ylabel('Daily Transaction Volume')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.subplot(2, 2, 3)
    sns.boxplot(x='anomaly_label', y='total_transactions', data=df, palette={'Normal': 'skyblue', 'Anomalous': 'red'})
    plt.title('Distribution Comparison', fontsize=12)
    plt.yscale('log')
    plt.ylabel('Volume (Log Scale)')

    plt.subplot(2, 2, 4)
    state_counts = anomalies['state'].value_counts().head(5)
    sns.barplot(x=state_counts.values, y=state_counts.index, palette='Reds_r')
    plt.title('Top 5 States with Suspicious Spikes', fontsize=12)
    plt.xlabel('Number of Anomalies')

    plt.tight_layout()
    plt.savefig("anomaly_report.png")
    print("Graph saved as 'anomaly_report.png'")


if __name__ == "__main__":
    plot_anomalies()