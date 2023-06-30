import json
from concurrent import futures

import definitions.retrieve_pb2 as retrieve_pb2
import definitions.retrieve_pb2_grpc as retrieve_pb2_grpc
import grpc
from tinydb import Query, TinyDB

# Create a TinyDB instance
db = TinyDB("../data.json")


class DataServiceServicer(retrieve_pb2_grpc.DataServiceServicer):
    def RetrieveInformation(self, request, context):
        user = request.user
        env_name = request.env_name
        print(user)
        print(env_name)
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
                    json_data = json.dumps(
                        {"error": f"No information found for environment {env_name}"},
                        indent=4,
                    )
            else:
                json_data = json.dumps(user_info, indent=4)
        else:
            json_data = json.dumps(
                {"error": f"No information found for user {user}"}, indent=4
            )

        response = retrieve_pb2.RetrieveInformationResponse(json_data=json_data)
        # return response

        # response = retrieve_pb2.RetrieveInformationResponse()
        response.json_data = json.dumps(json_data)
        return response
