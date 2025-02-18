import pandas as pd
from pathlib import Path
from typing import Optional

def sort_names_excel(input_path: str, output_path: Optional[str] = None) -> None:
    """
    Read names from Excel file, sort by alphabetical order and length, then save to a new file
    
    Args:
        input_path: Path to input Excel file
        output_path: Path to output Excel file (optional)
    """
    try:
        # Check if input file exists
        input_file = Path(input_path)
        if not input_file.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        # Read Excel file
        df = pd.read_excel(input_path)
        
        # Check if "Name" column exists
        if "Name" not in df.columns:
            raise ValueError('Excel file must contain a "Name" column')
            
        # Create columns for sorting
        df['first_letter'] = df['Name'].str[0].str.upper()
        df['name_length'] = df['Name'].str.len()
        
        # Sort by first letter and name length
        df_sorted = df.sort_values(
            by=['first_letter', 'name_length'],
            ascending=[True, True]
        )
        
        # Remove helper columns
        df_sorted = df_sorted.drop(['first_letter', 'name_length'], axis=1)
        
        # Create default output path if not specified
        if output_path is None:
            output_path = input_file.parent / f"sorted_{input_file.name}"
            
        # Save sorted results to new Excel file
        df_sorted.to_excel(output_path, index=False)
        print(f"Sorting completed, file saved to: {output_path}")
        
    except Exception as e:
        print(f"An error occurred during processing: {str(e)}")

if __name__ == "__main__":
    input_file = '/Users/myrickwang/Desktop/random_names.xlsx'
    sort_names_excel(input_file)
