import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

INPUT_FILE = "final_master_dataset.csv"  # Ensure this file exists from the previous merge step


def perform_trivariate_analysis():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found. Run the merge script first.")
        return

    df = pd.read_csv(INPUT_FILE)

    df['Child_Traffic'] = 0
    df['Adult_Traffic'] = 0

    if 'age_0_5' in df.columns:
        df['Child_Traffic'] += df['age_0_5'] + df.get('age_5_17', 0)
        df['Adult_Traffic'] += df.get('age_18_greater', 0)

    if 'bio_age_5_17' in df.columns:
        df['Child_Traffic'] += df['bio_age_5_17']
        df['Adult_Traffic'] += df.get('bio_age_17_', 0)

    if 'demo_age_5_17' in df.columns:
        df['Child_Traffic'] += df['demo_age_5_17']
        df['Adult_Traffic'] += df.get('demo_age_17_', 0)

    df['Total_Traffic'] = df['Child_Traffic'] + df['Adult_Traffic']

    top_states = df.groupby('state')['Total_Traffic'].sum().nlargest(10).index
    df_top = df[df['state'].isin(top_states)]

    plt.figure(figsize=(14, 7))
    sns.barplot(data=df_top, x='state', y='Total_Traffic', hue='data_category', errorbar=None)
    plt.title('Trivariate Analysis: State vs Operation Type vs Volume')
    plt.xticks(rotation=45)
    plt.ylabel('Total Transactions')
    plt.tight_layout()
    plt.savefig('analysis_state_category_vol.png')
    print("Generated: analysis_state_category_vol.png")

    age_analysis = df.groupby('data_category')[['Child_Traffic', 'Adult_Traffic']].sum().reset_index()
    age_melt = age_analysis.melt(id_vars='data_category', var_name='Demographic', value_name='Count')

    plt.figure(figsize=(10, 6))
    sns.barplot(data=age_melt, x='data_category', y='Count', hue='Demographic', palette='viridis')
    plt.title('Trivariate Analysis: Operation Type vs Age Demographics')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('analysis_category_age_vol.png')
    print("Generated: analysis_category_age_vol.png")

    pivot_table = df_top.groupby(['state', 'data_category'])['Total_Traffic'].sum().unstack()

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='Blues', linewidths=.5)
    plt.title('Activity Heatmap: Intensity of Operations across States')
    plt.tight_layout()
    plt.savefig('analysis_heatmap.png')
    print("Generated: analysis_heatmap.png")


if __name__ == "__main__":
    perform_trivariate_analysis()