from core.forms import JsonSchemaForm

from .models import Interview


class InterForm(JsonSchemaForm):
    def generate_json_schema(self, args_list=None):
        json_schema = super().generate_json_schema()
        # print(args_list)
        key_val = None
        if args_list:
            print(args_list)
            for key, value in args_list.items():
                if key in json_schema.get("properties", {}):
                    key_val = {
                        "title": key.capitalize(),
                        "type": "string",
                        "enumNames": list(value.values()),
                        "enum": list(value.keys()),
                    }

                json_schema["properties"][key] = key_val

        return json_schema

    class Meta:
        model = Interview
        fields = [
            "environment",
            "name",
            "problem",
            "config",
            "time_limit",
        ]
