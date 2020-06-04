from dynaconf import settings
import dataset


async def find_match(user_id):
    db = dataset.connect(settings.DATABASE_URL)

    user_db = db["users"]
    # user = user_db.find_one(id=user_id)

    other_users = list(user_db.all())

    answer_db = db["user_movies"]
    answers = list(answer_db.find(user_id=user_id))
    match = None
    for other_user in other_users:
        if other_user["id"] == user_id:
            continue

        other_answers = list(answer_db.find(user_id=other_user["id"]))
        score = (
            sum(a1["action"] == a2["action"] for a1, a2 in zip(answers, other_answers))
            / 20
        )
        if not match or score > match["score"]:
            match = {"score": score, "user": other_user}
    return match["user"], match["score"]
