Use this command from DogShow/ to import the data from puppy_seed.json

mongoimport --db dogshow --collection dogs --drop --file data/puppy_seed.json --type json --jsonArray
