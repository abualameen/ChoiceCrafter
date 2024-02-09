#!/usr/bin/python3
"""This module handles all default
RESTFul API actions for Alternative objects."""
from flask import jsonify, abort, request
from models import storage
from models.alternative import Alternative
from api.v1.views import app_views
from models.base_model import BaseModel


@app_views.route('/alternatives', methods=['GET'], strict_slashes=False)
def get_all_alternatives():
    """Retrieves the list of all Result objects."""
    alternatives = [alternative.to_dict() for alternative in
                    storage.all(Alternative).values()]
    return jsonify(alternatives)


@app_views.route('/alternatives/<alternative_id>',
                 methods=['GET'], strict_slashes=True)
def get_alternative_by_id(alternative_id):
    """Retrieves a Alterntive object."""
    alternative = storage.get(Alternative, alternative_id)
    if alternative is None:
        abort(404)
    return jsonify(alternative.to_dict())
