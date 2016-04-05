import csv
import json

destination = open( 'puppy_seed_1.json', 'w')
f = open( 'raw_dog_1.csv', 'r' )
reader = csv.DictReader( f, fieldnames = ( "src", "wins" ) )
count = 0
unique_links = set()

out = "["
for row in reader:
	if row['src'] not in unique_links:
		unique_links.add(row['src'])
		row['rating'] = 1200
		row['wins'] = 0
		row['losses'] = 0
		row['reportCount'] = 0
		out += "\n\t" + json.dumps(row)
		count += 1
out += "\n]"
print(count)
destination.write(out)
f.close()
destination.close()
