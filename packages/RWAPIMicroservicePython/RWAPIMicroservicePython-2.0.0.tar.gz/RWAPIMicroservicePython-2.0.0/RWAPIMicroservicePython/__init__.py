import json

import requests
from flask import request, Response
from requests import Session, Request
from werkzeug.datastructures import ImmutableMultiDict

from RWAPIMicroservicePython.errors import NotFound

GATEWAY_URL = None
MICROSERVICE_TOKEN = None


def register(app, gateway_url, token):
    @app.after_request
    def set_cors_headers(response):
        response.headers["access-control-allow-origin"] = "*"
        response.headers["access-control-allow-headers"] = "upgrade-insecure-requests"
        response.headers["access-control-allow-credentials"] = "true"
        response.headers["access-control-allow-methods"] = "OPTIONS,GET,PUT,POST,PATCH,DELETE"
        return response

    global MICROSERVICE_TOKEN, GATEWAY_URL
    MICROSERVICE_TOKEN = token
    GATEWAY_URL = gateway_url

    @app.before_request
    def get_logger_user():
        authorization_token_header = request.headers.get('authorization')
        if authorization_token_header is None:
            return

        logged_user_response = requests.get(
            GATEWAY_URL + '/auth/user/me',
            headers={
                'content-type': 'application/json',
                'Authorization': authorization_token_header
            }
        )

        if logged_user_response.status_code >= 400:
            return Response(logged_user_response.text, status=logged_user_response.status_code,
                            mimetype='application/json')

        http_args = request.args.to_dict()
        http_args['loggedUser'] = logged_user_response.text
        request.args = ImmutableMultiDict(http_args)

    @app.after_request
    def add_cache_headers(response):
        response.headers.set('cache-control', 'private')
        return response


def request_to_microservice(config):
    """Request to microservice method"""
    try:
        session = Session()
        request_config = Request(
            method=config.get('method'),
            url=GATEWAY_URL + config.get('uri'),
            headers={
                'content-type': 'application/json',
                'Authorization': 'Bearer ' + MICROSERVICE_TOKEN,
                'APP_KEY': config.get('application', 'rw')
            },
        )
        if 'body' in config:
            request_config.data = json.dumps(config.get('body'))
        prepped = session.prepare_request(request_config)

        response = session.send(prepped)
    except Exception as error:
        raise error

    try:
        return response.json()
    except Exception:
        raise NotFound(response.text)
