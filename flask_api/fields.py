

class Field:

    def __init__(self, field, obj):

        self.form_field = field

        self.field = {
            'name': field.name,
            'label': field.verbose_name or field.name.capitalize(),
            'value': getattr(obj, field.name, field.default),
            'placeholder': field.help_text,
            'validators': [],
        }

        if field.required:
            self.field['validators'].append({
                'type': 'required',
                'description': 'Campo é obrigatório',
            })

    def get_field(self):
        raise Exception(
            '%s must implement the method get_field and return field!' %
            self.__class__.__name__
        )


class StringField(Field):

    def get_field(self):

        self.field['type'] = "text"

        if self.form_field.max_length:
            self.field['validators'].append({
                "type": "maxlength",
                "condition": self.form_field.max_length,
                "description": "Campo deve ter no máximo %d caractéres" % self.form_field.max_length,
            })

        if self.form_field.min_length:
            self.field['validators'].append({
                "type": "minlength",
                "condition": self.form_field.min_length,
                "description": "Campo deve ter no mínimo %d caractéres" % self.form_field.min_length,
            })

        return self.field


class EmailField(StringField):

    def get_field(self):

        super().get_field()

        self.field['type'] = "email"

        if self.form_field.max_length:
            self.field['validators'].append({
                "type": "email",
                "description": "E-mail inválido",
            })

        return self.field


class DateTimeField(Field):

    def get_field(self):

        self.field['type'] = "datetime"

        self.field['validators'].append({
            "type": "pattern",
            "condition": '/^\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}$/',
            "description": "Campo deve estar no formato DD/MM/AAAA HH:MI",
        })

        if self.field['value']:
            self.field['value'] = self.field['value'].strftime("%d/%m/%Y %H:%M")

        return self.field


class HiddenField(Field):

    def get_field(self):
        self.field['value'] = str(self.field['value'])
        return self.field
