import json
import re

from django.template.defaulttags import register


@register.filter(name="times")
def times(number):
    return range(number)


@register.filter()
def class_name(value):
    return value.__class__.__name__


@register.filter
def pretty_json(value):
    return json.dumps(value, indent=4)


@register.filter
def get_item(dictionary, key):
    return str(dictionary.get(key))


@register.filter
def make_variable(value):
    rep = {"&": "and", " ": "_", ",": "", "/": "_or_", "-": "_"}
    rep = {re.escape(k): v for k, v in rep.items()}
    pattern = re.compile("|".join(rep.keys()))
    result = pattern.sub(lambda m: rep[re.escape(m.group(0))], value)
    return result.lower()
