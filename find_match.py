from dynaconf import settings
import dataset


def find_match(db, user, users):
    answer_db = db["answer"]
    answers = list(answer_db.find(owner_id=user["id"]))
    match = None
    for another_user in users:
        if another_user["id"] == user["id"]:
            continue

        another_answers = list(answer_db.find(owner_id=another_user["id"]))
        score = sum(a1["action"] == a2["action"] for a1, a2 in zip(answers, another_answers)) / 20
        if not match or score > match["score"]:
            match = {
                "score": score,
                "user": another_user
            }
    return match["user"], match["score"]


if __name__ == '__main__':
    db = dataset.connect(settings.DATABASE_DSN)
    user_db = db["user"]
    users = list(user_db.all())
    user = users[0]  # Usuário do questionário
    match, score = find_match(db, user, users)
    print(dict(user))
    print(dict(match))
    print(score)
