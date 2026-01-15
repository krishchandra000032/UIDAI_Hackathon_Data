import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
import numpy as np

RAW_FOLDER = "raw_data"
CLEAN_FOLDER = "clean_data"


def get_metrics(folder, filename, is_clean_folder=False):
    """Reads a file and returns row count and unique state count."""
    path = os.path.join(folder, filename)

    try:
        df = pd.read_csv(path)

        df.columns = df.columns.str.strip().str.lower()

        rows = len(df)

        if 'state' in df.columns:
            states = df['state'].dropna().astype(str).str.lower().str.strip()
            unique_states = states.nunique()
        else:
            unique_states = 0

        return rows, unique_states
    except Exception as e:
        print(f"  Warning: Could not read {path}. Reason: {e}")
        return 0, 0


def generate_comparison_chart():
    raw_files = glob.glob(os.path.join(RAW_FOLDER, "*.csv"))

    if not raw_files:
        print(f"Error: No CSV files found in '{RAW_FOLDER}'!")
        return

    results = []
    print(f"Found {len(raw_files)} raw files. Comparing with cleaned versions...\n")

    for raw_path in raw_files:
        filename = os.path.basename(raw_path)
        clean_filename = f"clean_{filename}"
        if not os.path.exists(os.path.join(CLEAN_FOLDER, clean_filename)):
            print(f"  Skipping {filename}: Corresponding clean file not found in '{CLEAN_FOLDER}'.")
            continue

        print(f"  Comparing: {filename} vs {clean_filename}")

        raw_rows, raw_states = get_metrics(RAW_FOLDER, filename)
        clean_rows, clean_states = get_metrics(CLEAN_FOLDER, clean_filename, is_clean_folder=True)

        if raw_rows > 0:  
            results.append({
                "File": filename[:15] + "...",  
                "Raw Rows": raw_rows,
                "Clean Rows": clean_rows,
                "Raw Unique States": raw_states,
                "Clean Unique States": clean_states
            })

    if not results:
        print("\nNo data available to plot. Check if files exist in both 'raw_data' and 'clean' folders.")
        return

    df_metrics = pd.DataFrame(results)

    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    x = np.arange(len(df_metrics))
    width = 0.35

    plt.bar(x - width / 2, df_metrics["Raw Rows"], width, label='Raw', color='#ff9999')
    plt.bar(x + width / 2, df_metrics["Clean Rows"], width, label='Clean', color='#66b3ff')

    plt.ylabel('Row Count')
    plt.title('Data Cleaning: Row Reduction (Duplicates/Nulls)')
    plt.xticks(x, df_metrics["File"], rotation=45, ha='right')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.bar(x - width / 2, df_metrics["Raw Unique States"], width, label='Raw', color='#ffcc99')
    plt.bar(x + width / 2, df_metrics["Clean Unique States"], width, label='Clean', color='#99ff99')

    plt.ylabel('Unique State Names')
    plt.title('Standardization: Quality Improvement')
    plt.xticks(x, df_metrics["File"], rotation=45, ha='right')
    plt.legend()

    plt.tight_layout()
    output_img = "comparison_chart.png"
    plt.savefig(output_img)
    print(f"\nSuccess! Chart saved as '{output_img}'.")


if __name__ == "__main__":
    generate_comparison_chart()
