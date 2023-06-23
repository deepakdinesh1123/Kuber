from tinydb import Query, TinyDB

db = TinyDB("data.json")


def upsert_containers(data: dict, user: str):
    q = Query()
    env = db.search(q.user == "admin")
    if env:
        containers = env[0]["containers"]
        db.update({"containers": containers.append(data)}, q.user == user)
    else:
        db.insert({"user": user, "containers": [data]})
