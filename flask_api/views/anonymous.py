from flask_api import models as m
from flask_api import fields as f
from flask import request
from flask_security.utils import encrypt_password, login_user, verify_password
from mongoengine.errors import NotUniqueError
from flask_login import logout_user


def resources():
    return {
        "routes": [{
            "path": "/",
            "resource": {
                "service": "$ideaForm",
                "params": ["login/form/"],
            }
        }, {
            "path": "/criar/conta/",
            "resource": {
                "service": "$ideaForm",
                "params": ["registration/form/"],
            }
        }],
        "defaultPath": "/"
    }


def navbar():
    return {
        "type": "inverse",
        "right": [{
            "widget": "link",
            "href": "#",
            "description": "Login"
        }, {
            "widget": "link",
            "href": "#/criar/conta",
            "description": "Cadastrar"
        }]
    }


def login_form():
    return {
        "title": "Login",
        "type": "horizontal",
        "submit": {
            "path": "login/",
            "method": "POST",
        },
        "fields": [
            f.EmailField(m.User.email).get_field(),
            f.PasswordField(m.User.password).get_field(),
        ],
        "buttons": [{
            "type": "submit",
            "value": "Login"
        }]
    }


def login():
    data = request.get_json(force=True)

    user = m.User.objects(email=data['email']).first()

    if user and verify_password(data['password'], user.password):
        login_user(user)
        return {'data': {'path': '/', 'resources': True}}
    else:
        return {'data': {'errors': ['Login inválido']}, 'status': 400}


def logout():
    logout_user()
    return {'data': {'path': '/', 'resources': True}}


def registration_form():

    password = f.PasswordField(m.User.password).get_field()
    password['name'] = 'confirm_password'
    password['label'] = 'Confirmar Senha'
    password['validators'].append({
        "type": "match",
        "condition": "password",
        "description": "Senhas não correspondem",
    })

    return {
        "title": "Cadastro",
        "type": "horizontal",
        "submit": {
            "path": "registration/",
            "method": "POST"
        },
        "fields": [
            f.StringField(m.User.name).get_field(),
            f.EmailField(m.User.email).get_field(),
            f.PasswordField(m.User.password).get_field(),
            password,
        ],
        "buttons": [{
            "type": "submit",
            "value": "Cadastrar"
        }]
    }


def registration():

    data = request.get_json(force=True)
    user = m.User()
    user.name = data['name']
    user.email = data['email']
    user.password = encrypt_password(data['password'])

    try:
        user.save()
        login_user(user)
        return {'data': {'path': '/', 'resources': True}}
    except NotUniqueError:
        msg = 'Já existe um outro usúario com mesmo email'
    except Exception:
        msg = 'Erro desconhecido'

    return {'data': {'errors': [msg]}, 'status': 400}
