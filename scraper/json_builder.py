# takes in a text containing the urls of the pictures of puppies (1 url in each line)
# outputs a json file containing all of the picture records with initialized values

import json
import re


TUMBLR_PATTERN = re.compile("http://[0-9]{2}.media.tumblr.com/([a-z0-9]+?)/.+?")

raw_names = ['raw_dog_1.txt', 'raw_dog_0.txt']
blacklist_name = 'blacklist.txt'
json_name = 'puppy_seed_1.json'

def raw_to_json(raw_names, blacklist_name, json_name):
	destination = open( json_name, 'w')
	count = 0
	unique_links = set()
	tumblr_set = set()
	json_list = []

	f = open(blacklist_name, 'r')
	blacklist = list(f.read().splitlines())
	for bad_img in blacklist:
		tumblr_set.add(bad_img)
		
	for raw_name in raw_names:
		f = open(raw_name, 'r' )
		src_list = list(f.read().splitlines())
		def jsonify(src):
			nonlocal count
			if src not in unique_links:
				tumblr_match = TUMBLR_PATTERN.match(src)
				if tumblr_match:
					identifier =  tumblr_match.group(1)
					if identifier == '3a4d4eb72ed3fbe7936a64e8d0729ae1':
						print("text")
					print(identifier)
					if identifier in tumblr_set:
						return None
					else:
						tumblr_set.add(identifier)
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

raw_to_json(raw_names, blacklist_name, json_name)