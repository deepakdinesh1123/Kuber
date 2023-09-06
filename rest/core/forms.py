import json

from django import forms


class JsonSchemaForm(forms.ModelForm):
    def generate_json_schema(self):
        fields = self.fields

        json_schema = {"type": "object", "required": [], "properties": {}}

        for field_name, field in fields.items():
            json_property = {
                "title": field.label,
            }

            if field.required:
                json_schema["required"].append(field_name)

            if isinstance(field.widget, forms.widgets.Textarea):
                json_property["type"] = "string"
            else:
                if isinstance(field, forms.BooleanField):
                    json_property["type"] = "boolean"
                    json_property["oneOf"] = [
                        {"title": "Enable", "const": True},
                        {"title": "Disable", "const": False},
                    ]
                else:
                    json_property["type"] = "string"

            if field.widget.attrs.get("default"):
                json_property["default"] = field.widget.attrs["default"]

            json_schema["properties"][field_name] = json_property

        return json_schema
