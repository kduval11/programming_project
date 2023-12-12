import pandas as pd

def remove_rows_with_terms(csv_file, terms, output_file):
    df = pd.read_csv(csv_file)

    df = df[~df['Resource Name'].str.contains('|'.join(terms), case=False)]

    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_csv = 'output_files/house_output.csv'
    terms_to_remove = ['farmhouse', 'district', 'cemetery', 'post', 'cottage', 'library', 'manor', 'mansion', 'parish', 'tavern']
    output_csv = 'filtered_house_output.csv'

    remove_rows_with_terms(input_csv, terms_to_remove, output_csv)

    print(f"Filtered data saved to {output_csv}")