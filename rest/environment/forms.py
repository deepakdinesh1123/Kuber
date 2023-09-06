from core.forms import JsonSchemaForm

from .models import Environment


class EnvForm(JsonSchemaForm):
    def generate_json_schema(self, args_list):
        json_schema = super().generate_json_schema()
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

                # print(modification)
                json_schema["properties"][key] = key_val

        return json_schema

    class Meta:
        model = Environment
        fields = ["env_name", "image", "config", "type", "private"]
