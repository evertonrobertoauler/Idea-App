from flask import Flask, Response
from flask_security import Security, MongoEngineUserDatastore
import json
from flask_api import settings
from flask_login import current_user

app = Flask(__name__)
app.config.from_object(settings)

from flask_api.models import db, User, Role
db.init_app(app)

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from flask_api.cors import before_request, after_request
app.before_request(before_request)
app.after_request(after_request)


def jsonify(data, status=200):

    js = json.dumps(data)
    resp = Response(js, status=status, mimetype='application/json')

    return resp


@app.route('/api/resources/')
def resources():
    if current_user.is_anonymous():
        from flask_api.views.anonymous import resources
    elif current_user.teacher:
        from flask_api.views.teacher import resources
    else:
        from flask_api.views.student import resources

    return jsonify(resources())


@app.route('/api/navbar/')
def navbar():
    if current_user.is_anonymous():
        from flask_api.views.anonymous import navbar
    elif current_user.teacher:
        from flask_api.views.teacher import navbar
    else:
        from flask_api.views.student import navbar

    return jsonify(navbar())


@app.route('/api/login/form/')
def login_form():
    from flask_api.views.anonymous import login_form
    return jsonify(login_form())


@app.route('/api/login/', methods=['POST'])
def login():
    from flask_api.views.anonymous import login
    return jsonify(**login())


@app.route('/api/logout/', methods=['POST'])
def logout():
    from flask_api.views.anonymous import logout
    return jsonify(**logout())


@app.route('/api/registration/form/')
def registration_form():
    from flask_api.views.anonymous import registration_form
    return jsonify(registration_form())


@app.route('/api/registration/', methods=['POST'])
def registration():
    from flask_api.views.anonymous import registration
    return jsonify(**registration())


@app.route('/api/knowledge/test/form/')
def knowledge_test_form():
    from flask_api.views.student import knowledge_test_form
    return jsonify(knowledge_test_form())


@app.route('/api/knowledge/test/', methods=['POST'])
def knowledge_test():
    from flask_api.views.student import knowledge_test
    return jsonify(**knowledge_test())


if __name__ == '__main__':

    from flask_api.debug import app_options

    app.run(**app_options)