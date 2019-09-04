import json

from django.db import models

models_type = {'string': models.CharField(max_length=128), 'boolean': models.BooleanField(),
               'int': models.IntegerField(), 'float': models.FloatField(),
               'date': models.DateTimeField(auto_now_add=False), 'time': models.TimeField(auto_now_add=False)
               }


def create_fields(data):
    model_fields = {}
    var = json.loads(data)
    for k in var['field_names']:
        if var['fields'][k] in models_type:
            model_fields.update({
                k: var['fields'][k]
            })
    return model_fields
