import random
from uuid import uuid4

import dataset
from faker import Faker
from dynaconf import settings

db = dataset.connect(settings.DATABASE_DSN)
user_db = db["user"]

fake = Faker()


release_db = db["release"]
answer_db = db["answer"]
releases = list(release_db.all())

for i in range(500):
    user_id = user_db.insert({"id": str(uuid4()), "email": f"{i}{fake.email()}"})

    for release in releases:
        answer = answer_db.insert(
            {
                "id": str(uuid4()),
                "action": random.choice(["LEFT", "RIGHT", "DID_NOT_WATCH"]),
                "owner_id": user_id,
                "release_id": release["id"],
            }
        )
