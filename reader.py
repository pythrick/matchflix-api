import dataset
from pprint import pprint

db = dataset.connect('sqlite:///db.sqlite3')
# table = db['releases']
table = db["answers"]

result = table.all()

pprint(list(result))
