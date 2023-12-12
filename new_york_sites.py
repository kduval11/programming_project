import csv

new_york_data = []

with open('National_Register_of_Historic_Places.csv') as new_york_csv:
    csv_file = csv.DictReader(new_york_csv)
    for line in csv_file:
        new_york_data.append(dict(line))

for site in new_york_data:
    print(site)

csv_filename = 'new_york_sites_all_counties.csv'
with open(csv_filename, 'w', newline='') as csv_file:
    fieldnames = new_york_data[0].keys()
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    csv_writer.writeheader()

    csv_writer.writerows(new_york_data)

print(f'Data written to {csv_filename}')


