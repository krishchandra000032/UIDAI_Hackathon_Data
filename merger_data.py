import pandas as pd
import glob
import os
INPUT_FOLDER = "clean_data"
OUTPUT_FILE = "final_master_dataset.csv"


def merge_clean_files():
    search_path = os.path.join(INPUT_FOLDER, "clean_*.csv")
    files = glob.glob(search_path)

    if not files:
        print("No 'clean' files found! Please run the cleaning script first.")
        return

    print(f"Found {len(files)} files. Merging...")

    data_frames = []

    for file_path in files:
        try:
            filename = os.path.basename(file_path)
            df = pd.read_csv(file_path)
            if "biometric" in filename.lower():
                df['data_category'] = 'Biometric Update'
            elif "demographic" in filename.lower():
                df['data_category'] = 'Demographic Update'
            elif "enrolment" in filename.lower():
                df['data_category'] = 'New Enrolment'
            else:
                df['data_category'] = 'Other'
            df['source_file'] = filename

            data_frames.append(df)
            print(f"  -> Added {len(df)} rows from {filename}")

        except Exception as e:
            print(f"  Error reading {filename}: {e}")

    master_df = pd.concat(data_frames, ignore_index=True, sort=False)
    
    numeric_cols = master_df.select_dtypes(include=['number']).columns
    
    master_df[numeric_cols] = master_df[numeric_cols].fillna(0)

    master_df.to_csv(OUTPUT_FILE, index=False)

    print("-" * 30)
    print("MERGE COMPLETE SUCCESS")
    print("-" * 30)
    print(f"Total Rows: {len(master_df)}")
    print(f"Total Columns: {len(master_df.columns)}")
    print(f"Saved to: {os.path.abspath(OUTPUT_FILE)}")


if __name__ == "__main__":
    merge_clean_files()
