from pprint import pprint

import dataset

db = dataset.connect("sqlite:///db.sqlite3")
# table = db['releases']
table = db["answer"]

result = table.all()

pprint(list(result))
