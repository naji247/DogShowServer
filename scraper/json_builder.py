# takes in a text containing the urls of the pictures of puppies (1 url in each line)
# outputs a json file containing all of the picture records with initialized values

import json

json_name = 'puppy_seed_1.json'
csv_name = 'raw_dog_1.txt'

def csv_to_json(csv_name, json_name):
	destination = open( json_name, 'w')
	f = open( csv_name, 'r' )
	count = 0
	unique_links = set()
	src_list = list(f.read().splitlines())

	def jsonify(src):
		nonlocal count
		row = {'src' : src}
		if src not in unique_links:
			unique_links.add(src)
			row['rating'] = 1200
			row['wins'] = 0
			row['losses'] = 0
			row['reportCount'] = 0
			count += 1
		return json.dumps(row)

	json_list = map(jsonify, src_list)
	out = "[\n\t" + ",\n\t".join(json_list) + "\n]"
	print(count)
	destination.write(out)
	f.close()
	destination.close()

csv_to_json(csv_name, json_name)