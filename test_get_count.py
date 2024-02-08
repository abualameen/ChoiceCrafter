#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.criteria import Criteria

print("All objects: {}".format(storage.count()))
print("Criteria objects: {}".format(storage.count(Criteria)))

first_criteria_id = list(storage.all(Criteria).values())[0].id
print("First state: {}".format(storage.get(Criteria, first_criteria_id)))
