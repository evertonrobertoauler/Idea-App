from flask_login import current_user, request
from flask_api import models as m


def resources():
    return {
        "routes": [{
            "path": "/",
            "resource": {
                "service": "$ideaForm",
                "params": ["knowledge/test/form/"],
            }
        }, {
            "path": "/sair/",
            "resource": {
                "service": "$ideaLogout",
            }
        }],
        "defaultPath": "/"
    }


def navbar():
    return {
        "type": "inverse",
        "right": [{
            "widget": "link",
            "href": "#/",
            "description": current_user.name
        }, {
            "widget": "link",
            "href": "#/sair/",
            "description": "Sair"
        }]
    }


def knowledge_test_form():
    return {
        "title": "Teste de conhecimento",
        "type": "horizontal",
        "submit": {
            "path": "knowledge/test/",
            "method": "POST"
        },
        "fields": [{
            "type": "radio",
            "description": "Pergunta?",
            "name": "pergunta",
            "value": "b",
            "options": {
                "a": "teste1",
                "b": "teste2"
            }
        }],
        "buttons": [{
            "type": "submit",
            "value": "Responder"
        }]
    }


def knowledge_test():
    data = request.get_json(force=True)
    data['path'] = '/'
    return {'data': data}
