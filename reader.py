import dataset
from pprint import pprint
from dynaconf import settings


db = dataset.connect(settings.DATABASE_URL)
# table = db['releases']
table = db["answers"]

result = table.all()

pprint(list(result))
