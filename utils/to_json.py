import json

from utils.case_change import snake_to_camel_case


def model_snake_to_camel_case(model):
    new_item = {}
    for key, value in model.__dict__.items():
        if not key.startswith("_"):
            if key.find("_") > 0:
                new_key = snake_to_camel_case(key)
                new_item = {**new_item, new_key: str(value)}
            else:
                new_item = {**new_item, key: str(value)}

    return new_item


def queryset_to_json(queryset):
    data = []
    for item in queryset:
        data.append(model_snake_to_camel_case(item))

    return json.dumps(data)
