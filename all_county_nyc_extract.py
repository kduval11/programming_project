import csv

input_csv_file = 'all_county_sites_by_type.csv'
output_csv_file = 'all_county_sites_nyc_only.csv'

nyc_keywords = ['New York', 'Bronx', 'Queens', 'Kings', 'Richmond']

with open(input_csv_file, 'r', newline='') as infile:
    reader = csv.DictReader(infile)
    header = reader.fieldnames

    nyc_rows = []

    for row in reader:
        if any(keyword in row['County'] for keyword in nyc_keywords):
            nyc_rows.append(row)

with open(output_csv_file, 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(nyc_rows)

print(f"Filtered data written to {output_csv_file}")
