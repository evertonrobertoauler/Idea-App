from flask import Flask, jsonify

from flask_api import settings

app = Flask(__name__)
app.config.from_object(settings)

from flask_api.models import db
db.init_app(app)

from flask_api.cors import before_request, after_request
app.before_request(before_request)
app.after_request(after_request)


@app.route('/api/form')
def form():
    from flask_api.helpers import model_to_form
    from flask_api.models import Todo

    return jsonify(model_to_form(Todo, Todo.objects.first()))


if __name__ == '__main__':

    from flask_api.debug import app_options

    app.run(**app_options)