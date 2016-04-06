# takes in a text containing the urls of the pictures of puppies (1 url in each line)
# outputs a json file containing all of the picture records with initialized values

import json


raw_names = ['raw_dog_1.txt', 'raw_dog_0.txt']
json_name = 'puppy_seed_1.json'

def raw_to_json(raw_names, json_name):
	destination = open( json_name, 'w')
	count = 0
	unique_links = set()
	json_list = []
	for raw_name in raw_names:
		f = open( raw_name, 'r' )
		src_list = list(f.read().splitlines())
		def jsonify(src):
			nonlocal count
			if src not in unique_links:
				row = {'src' : src, 'rating':1200, 'wins':0, 'losses':0, 'reportCount':0}
				unique_links.add(src)
				count += 1
				return json.dumps(row)
			else:
				return None
		json_list += list(filter(lambda x: x is not None, map(jsonify, src_list)))
		f.close()
	out = "[\n\t" + ",\n\t".join(json_list) + "\n]"
	print(count)
	destination.write(out)
	destination.close()

raw_to_json(raw_names, json_name)