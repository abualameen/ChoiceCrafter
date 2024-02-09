#!/usr/bin/python3
"""This module handles all default RESTFul API actions for criteria objects."""
from flask import jsonify, abort, request
from models import storage
from models.criteria import Criteria
from api.v1.views import app_views
from models.base_model import BaseModel


@app_views.route('/criterias', methods=['GET'], strict_slashes=False)
def get_all_criteria():
    """Retrieves the list of all Criteria objects."""
    criterias = [criteria.to_dict() for criteria in
                 storage.all(Criteria).values()]
    return jsonify(criterias)


@app_views.route('/criterias/<criteria_id>',
                 methods=['GET'], strict_slashes=True)
def get_criteria_by_id(criteria_id):
    """Retrieves a Criteria object."""
    criteria = storage.get(Criteria, criteria_id)
    print(criteria_id)
    print(criteria)
    if criteria is None:
        abort(404)
    return jsonify(criteria.to_dict())
