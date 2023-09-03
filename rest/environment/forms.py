import json
from django import forms
from .models import Environment
from user.models import KuberUser


def generate_json_schema(form_class):
    fields = form_class().fields

    json_schema = {
        "title": "Form Schema",
        "description": "Dynamically generated form schema.",
        "type": "object",
        "required": [],
        "properties": {}
    }

    for field_name, field in fields.items():
        json_property = {
            "title": field.label,
        }

        if field.required:
            json_schema["required"].append(field_name)

        if isinstance(field.widget, forms.widgets.Textarea):
            json_property["type"] = "string"
        else:
            json_property["type"] = "string"

        if field.widget.attrs.get("default"):
            json_property["default"] = field.widget.attrs["default"]

        json_schema["properties"][field_name] = json_property

    return json_schema


class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = '__all__'


json_schema = generate_json_schema(EnvironmentForm)


formatted_json = json.dumps(json_schema, indent=2)
print(formatted_json)
