from flask_mongoengine import Document, MongoEngine
import mongoengine as me
from datetime import datetime

db = MongoEngine()


class Todo(Document):

    text = me.StringField(
        max_length=100, required=True, min_length=10, verbose_name="Texto", help_text="Descrição"
    )
    email = me.EmailField(
        max_length=100, required=True, min_length=10, verbose_name="E-mail", help_text="Insira um E-mail válido"
    )
    created = me.DateTimeField(
        default=datetime.now(), required=True, verbose_name="Criado", help_text="data criacao"
    )