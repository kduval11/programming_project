import pandas as pd
import os

input_csv_path = 'new_york_sites_all_counties.csv' 

df = pd.read_csv(input_csv_path)

keywords = ['church', 'chapel', 'cathedral', 'seminary', 'tempel', 'synagogue', 'parish', 'house', 'cottage', 'mansion', 'school', 'academy', 'district', 'tavern', 'hotel', 'inn', 'farm', 'barn',
            'restaurant', 'library', 'station', 'post', 'factory', 'cemetery', 'burial', 'hall', 'bank', 'park', 'theater', 'theatre', 'manor', 'mosque',
         'birthplace', 'estate', 'homestead', 'studio', 'armory', 'fort', 'hospital','club', 'bridge', 'windmill']

output_directory = 'output_files'
os.makedirs(output_directory, exist_ok=True)

for keyword in keywords:
    keyword_df = df[df['Resource Name'].str.contains(keyword, case=False)]
    
    if not keyword_df.empty:
        output_file_path = f'{output_directory}/{keyword}_output.csv'
        keyword_df.to_csv(output_file_path, index=False)
        print(f'{output_file_path} created successfully.')

other_df = df[~df['Resource Name'].str.contains('|'.join(keywords), case=False)]
if not other_df.empty:
    output_file_path = f'{output_directory}/Other_output.csv'
    other_df.to_csv(output_file_path, index=False)
    print(f'{output_file_path} created successfully.')