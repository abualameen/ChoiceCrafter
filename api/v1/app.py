#!/usr/bin/python3
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    """ this closes the db storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ when there is a 404 error"""
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ the main function """
    host = environ.get('CC_API_HOST')
    port = environ.get('CC_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5005'
    app.run(host=host, port=port, debug=True)
