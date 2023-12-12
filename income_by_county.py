import requests
import pandas as pd

api_key = '9ef3c3c8381f4b303b8e8123d51665662aa44cd1'
year = '2019' 
endpoint = f'https://api.census.gov/data/{year}/acs/acs5'

income_variable = 'B19013_001E'
name_variable = 'NAME'
geography = 'for=county:*&in=state:36'

url = f'{endpoint}?get={income_variable},{name_variable}&{geography}&key={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data[1:], columns=data[0])
    df.columns = ['Median Household Income', 'County Name', 'State', 'County Code']

    df.to_csv('income_data_counties_ny.csv', index=False)
else:
    print(f"Error: {response.status_code}")
