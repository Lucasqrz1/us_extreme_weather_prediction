import pandas as pd
import glob
import os

def consolidate_details(input_folder, output_file):
    """Consolidates all CSV from 'details' """
    print("Consolidating Details...")
    
    csv_files = glob.glob(f'{input_folder}/*.csv.gz')
    df_list = []
    
    for file in csv_files:
        print(f"Processing: {file}")
        df = pd.read_csv(file, compression='gzip', low_memory=False)
        df_list.append(df)
    
    df_consolidated = pd.concat(df_list, ignore_index=True)
    df_consolidated.to_csv(output_file, index=False)
    print(f"✅ Details consolidated: {len(df_consolidated)} lines")
    
    return df_consolidated

def consolidate_fatalities(input_folder, output_file):
    """Consolidates all CSVs from 'Fatalities' """
    print("\nConsolidating Fatalities...")
    
    csv_files = glob.glob(f'{input_folder}/*.csv.gz')
    df_list = []
    
    for file in csv_files:
        print(f"Processing: {file}")
        df = pd.read_csv(file, compression='gzip', low_memory=False)
        df_list.append(df)
    
    df_consolidated = pd.concat(df_list, ignore_index=True)
    df_consolidated.to_csv(output_file, index=False)
    print(f"✅ Fatalities consolidating: {len(df_consolidated)} lines")
    
    return df_consolidated

def merge_details_fatalities(details_file, fatalities_file, output_file):
    """Merge Details with Fatalities"""
    print("\nMerging Details + Fatalities...")
    
    # Load consolidated
    details = pd.read_csv(details_file, low_memory=False)
    fatalities = pd.read_csv(fatalities_file, low_memory=False)
    
    # Group fatalities per event (count deaths)
    fatalities_count = fatalities.groupby('EVENT_ID').size().reset_index(name='TOTAL_DEATHS')
    
    # Merge
    final_df = details.merge(fatalities_count, on='EVENT_ID', how='left')
    
    # Fill events with no deaths
    final_df['TOTAL_DEATHS'] = final_df['TOTAL_DEATHS'].fillna(0).astype(int)
    
    # Saves
    final_df.to_csv(output_file, index=False)
    print(f"✅ Final dataset: {len(final_df)} lines")
    print(f"Total events with deaths: {(final_df['TOTAL_DEATHS'] > 0).sum()}")
    
    return final_df

if __name__ == "__main__":
    # Creates folders if they don't exist
    os.makedirs('data/processed', exist_ok=True)
    
    # 1. Consolidates Details
    details_df = consolidate_details(
        input_folder='data/raw/details',
        output_file='data/processed/details_consolidated.csv'
    )
    
    # 2. Consolidates Fatalities
    fatalities_df = consolidate_fatalities(
        input_folder='data/raw/fatalities',
        output_file='data/processed/fatalities_consolidated.csv'
    )
    
    # 3. Merge
    final_df = merge_details_fatalities(
        details_file='data/processed/details_consolidated.csv',
        fatalities_file='data/processed/fatalities_consolidated.csv',
        output_file='data/processed/final_dataset.csv'
    )
    
    print("\n🎉 Consolidation complete!")

