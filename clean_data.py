import pandas as pd
import glob
import os
from fuzzywuzzy import process, fuzz

INPUT_FOLDER = "raw_data"
OUTPUT_FOLDER = "clean_data"
THRESHOLD = 90


def get_optimized_mapping(series, threshold=90):
    """
    Creates a mapping dictionary to standardize text using fuzzy logic.
    """
    counts = series.value_counts()
    unique_values = counts.index.tolist()

    mapping = {}

    while unique_values:
        primary = unique_values.pop(0)
        mapping[primary] = primary

        matches = process.extract(
            primary,
            unique_values,
            scorer=fuzz.token_sort_ratio,
            limit=None
        )

        similar_values = [x[0] for x in matches if x[1] >= threshold]

        for match in similar_values:
            mapping[match] = primary
            if match in unique_values:
                unique_values.remove(match)

    return mapping


def clean_file(file_path):
    filename = os.path.basename(file_path)
    print(f"Processing: {filename}...")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    original_count = len(df)

    df.columns = df.columns.str.strip().str.lower()

    if 'state' in df.columns:
        df = df[df['state'] != 'state']

    for col in ['state', 'district']:
        if col in df.columns:
            valid_values = df[col].dropna().astype(str)
            if not valid_values.empty:
                print(f"  - Fuzzy cleaning column: {col}...")
                mapping_dict = get_optimized_mapping(valid_values, THRESHOLD)
                df[col] = df[col].map(mapping_dict).fillna(df[col])

    subset_cols = [c for c in ['state', 'district', 'pincode'] if c in df.columns]
    df.dropna(subset=subset_cols, inplace=True)
    df.drop_duplicates(inplace=True)

    clean_filename = f"clean_{filename}"
    output_path = os.path.join(OUTPUT_FOLDER, clean_filename)

    df.to_csv(output_path, index=False)

    cleaned_count = len(df)
    print(f"  -> Saved to: {output_path}")
    print(f"  -> Removed {original_count - cleaned_count} rows.\n")


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created folder: {OUTPUT_FOLDER}")

    search_path = os.path.join(INPUT_FOLDER, "*.csv")
    files = glob.glob(search_path)

    if not files:
        print(f"No CSV files found in '{INPUT_FOLDER}' folder!")
    else:
        print(f"Found {len(files)} files in '{INPUT_FOLDER}'. Starting process...\n")
        for file in files:
            clean_file(file)
        print("All files processed.")
