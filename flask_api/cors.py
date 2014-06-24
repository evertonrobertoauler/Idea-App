from flask import request, current_app


def before_request():
    if request.method == 'OPTIONS':
        resp = current_app.make_default_options_response()
        h = resp.headers
        if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
            h['Access-Control-Allow-Headers'] = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']

        h['Access-Control-Allow-Origin'] = "http://127.0.0.1:9000"
        h['Access-Control-Allow-Credentials'] = 'true'
        h['Access-Control-Allow-Methods'] = request.headers['Access-Control-Request-Method']

        return resp


def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = "http://127.0.0.1:9000"
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp