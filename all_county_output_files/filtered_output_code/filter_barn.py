import pandas as pd

def remove_rows_with_terms(csv_file, terms, output_file):
    df = pd.read_csv(csv_file)

    df = df[~df['Resource Name'].str.contains('|'.join(terms), case=False)]

    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_csv = 'output_files/barn_output.csv'
    terms_to_remove = ['farm', 'house']
    output_csv = 'filtered_barn_output.csv'

    remove_rows_with_terms(input_csv, terms_to_remove, output_csv)

    print(f"Filtered data saved to {output_csv}")