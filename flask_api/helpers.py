from flask_api import fields


def model_to_form(model, obj=None):

    if not obj:
        obj = model()

    form = {
        'type': 'horizontal',
        'fields': [],
        "buttons": [{
            "type": "submit",
            "value": "Salvar"
        }, {
            "type": "reset",
            "value": "Limpar"
        }],
    }

    for (name, field) in getattr(obj, '_fields').items():

        class_name = field.__class__.__name__

        field_class = getattr(fields, class_name, fields.HiddenField)

        form['fields'].append(
            field_class(field, obj).get_field()
        )

    return form
