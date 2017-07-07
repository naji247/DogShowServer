import re
import requests


LINE_PATTERN =  re.compile('{"losses": 0, "src": "(.+?)", "reportCount": 0, "rating": 1200, "wins": 0},')

input_names = '../data/puppy_seed_1.json'
output_names = '../data/puppy_seed_2.json'

def remove_invalids(input_names, output_names):
  with open(input_names, 'r') as old, open(output_names, 'w') as new:
    line = old.readline()
    successes = 0
    total = 0
    while line != '':

      tumblr_match = LINE_PATTERN.search(line)

      if tumblr_match:
        url = tumblr_match.group(1)
        try:
          code = requests.get(url).status_code
          new.write(line)
          successes += 1      
        except:
          pass
      else:
        new.write(line)

      total += 1
      print "{0} / {1}".format(successes, total)

      line = old.readline() 

remove_invalids(input_names, output_names)
