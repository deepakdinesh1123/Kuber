import json

from tinydb import Query, TinyDB

db = TinyDB("data.json")


def upsert_containers(data: dict, user: str):
    q = Query()
    env = db.search(q.user == user)
    if env:
        environments = env[0]["environments"]
        env_name = data.get("env_name")
        existing_env = next(
            (env_item for env_item in environments if env_name in env_item), None
        )
        if existing_env:
            containers = existing_env[env_name]["containers"]
            existing_containers = set(containers)
            new_containers = data["containers"]
            duplicate_containers = list(
                set(new_containers).intersection(existing_containers)
            )
            if duplicate_containers:
                print(
                    f"Container(s) {', '.join(duplicate_containers)} already exist in environment {env_name}."
                )
            else:
                containers.extend(new_containers)
                db.update({"environments": environments}, q.user == user)
        else:
            new_env = {env_name: {"containers": data["containers"]}}
            environments.append(new_env)
            db.update({"environments": environments}, q.user == user)
    else:
        db.insert(
            {
                "user": user,
                "environments": [
                    {data.get("env_name"): {"containers": data["containers"]}}
                ],
            }
        )


def delete_environment(env_name: str, user: str):
    q = Query()
    env = db.search(q.user == user)
    if env:
        environments = env[0]["environments"]
        existing_env = next(
            (env_item for env_item in environments if env_name in env_item), None
        )
        if existing_env:
            environments.remove(existing_env)
            db.update({"environments": environments}, q.user == user)
            print(f"Environment {env_name} deleted.")
        else:
            print(f"Environment {env_name} not found.")
    else:
        print(f"No environments found for user {user}.")


def delete_container(container_name: str, env_name: str, user: str):
    q = Query()
    env = db.search(q.user == user)
    if env:
        environments = env[0]["environments"]
        existing_env = next(
            (env_item for env_item in environments if env_name in env_item), None
        )
        if existing_env:
            containers = existing_env[env_name]["containers"]
            if container_name in containers:
                containers.remove(container_name)
                db.update({"environments": environments}, q.user == user)
                print(
                    f"Container {container_name} deleted from environment {env_name}."
                )
            else:
                print(
                    f"Container {container_name} not found in environment {env_name}."
                )
        else:
            print(f"Environment {env_name} not found.")
    else:
        print(f"No environments found for user {user}.")


def delete_user(user: str):
    q = Query()
    db.remove(q.user == user)
    print(f"User {user} deleted.")


def retrieve_information(user: str, env_name: str = None):
    q = Query()
    env = db.search(q.user == user)
    if env:
        user_info = env[0]
        if env_name:
            env_data = next(
                (
                    env_item
                    for env_item in user_info["environments"]
                    if env_name in env_item
                ),
                None,
            )
            if env_data:
                return json.dumps(env_data[env_name], indent=4)
            else:
                return json.dumps(
                    {"error": f"No environment named {env_name} found for user {user}"},
                    indent=4,
                )
        else:
            return json.dumps(user_info, indent=4)
    else:
        return json.dumps({"error": f"No information found for user {user}"}, indent=4)



