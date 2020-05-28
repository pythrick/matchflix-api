from pprint import pprint

import dataset

db = dataset.connect("sqlite:///db.sqlite3")
user_db = db["user"]


release_db = db["release"]
answer_db = db["answer"]


def get_set_answers(user_id):
    answers = answer_db.find(owner_id=user_id)
    return set([a["release_id"] for a in answers if a["action"] == "RIGHT"])


# Recuperar os sets
users = list(user_db.all())


user = users[0]  # Usuário do questionário

user_answers = get_set_answers(user["id"])
# Comparar com os sets de filmes dos outros usuários
closest_match = None
for another_user in users:
    if another_user["id"] == user["id"]:
        continue
    another_user_answers = get_set_answers(another_user["id"])
    intersection = user_answers & another_user_answers

    score = len(intersection) / 20
    if not closest_match or score > closest_match["score"]:
        closest_match = {
            "score": score,
            "match_user": another_user,
            "intersection": intersection,
            "user": user,
        }


pprint(closest_match)
