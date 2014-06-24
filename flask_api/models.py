from flask_security import UserMixin, RoleMixin
from flask_login import current_user
from flask_mongoengine import Document, MongoEngine
import mongoengine as me
from datetime import datetime

db = MongoEngine()


class Role(RoleMixin, me.EmbeddedDocument):
    name = me.StringField(max_length=80, unique=True)
    description = me.StringField(max_length=255)


class User(UserMixin, Document):
    name = me.StringField(required=True, max_length=100, verbose_name="Nome")
    email = me.EmailField(required=True, unique=True, verbose_name="E-mail")
    password = me.StringField(verbose_name="Senha", required=True)
    active = me.BooleanField(default=True, verbose_name="Ativo")
    teacher = me.BooleanField(default=False)
    confirmed_at = me.DateTimeField(verbose_name="Confirmado em")
    roles = me.ListField(me.EmbeddedDocumentField(Role), default=[])


class ClassRoom(Document):
    name = me.StringField(max_length=100, verbose_name="Nome")
    teacher = me.ReferenceField(User, default=lambda: current_user)
    students = me.ListField(me.ReferenceField(User), verbose_name="Alunos")


class Question(Document):

    teacher = me.ReferenceField(User, default=lambda: current_user)

    text = me.StringField(
        max_length=100, required=True, min_length=10,
        verbose_name="Questão", help_text="Texto"
    )

    answers = me.ListField(
        me.StringField(max_length=100, required=True),
        verbose_name="Alternativas"
    )

    created = me.DateTimeField(
        default=datetime.now(), required=True,
        verbose_name="Criado", help_text="Data criacao"
    )


class Vote(me.EmbeddedDocument):
    answer = me.StringField(max_length=100, required=True)
    students = me.ListField(me.ReferenceField(User), verbose_name="Alunos")


class KnowledgeTest(Document):

    question = me.ReferenceField(Question, verbose_name="Pergunta")

    votes = me.ListField(Vote)

    start = me.DateTimeField(
        default=datetime.now(), required=True,
        verbose_name="Início", help_text="Início do teste"
    )

    finish = me.DateTimeField(
        default=datetime.now(), required=True,
        verbose_name="Fim", help_text="Fim do teste"
    )