#!/usr/bin/python3
"""This module handles all default RESTFul API actions for Result objects."""
from flask import jsonify, abort, request
from models import storage
from models.result import Result
from api.v1.views import app_views
from models.base_model import BaseModel


@app_views.route('/results', methods=['GET'], strict_slashes=False)
def get_all_results():
    """Retrieves the list of all Result objects."""
    results = [result.to_dict() for result in storage.all(Result).values()]
    return jsonify(results)


@app_views.route('/results/<result_id>', methods=['GET'], strict_slashes=True)
def get_result_by_id(result_id):
    """Retrieves a Result object."""
    result = storage.get(Result, result_id)
    if result is None:
        abort(404)
    return jsonify(result.to_dict())
