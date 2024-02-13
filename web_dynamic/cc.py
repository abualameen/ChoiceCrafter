#!/usr/bin/python3
"""
this the choice crafter flask app
"""
from models import storage
from models.criteria import Criteria
from models.alternative import Alternative
from models.result import Result
import copy
from flask import Flask, render_template, request, jsonify
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from flask import session
import secrets
import json
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """ this is a index function for the index route """
    if request.method == "POST":
        data = request.get_json()
        table_data = data.get('tableData')
        table_data = [[float(i) for i in sublist] for sublist in table_data]
        table_data1 = data.get('tableData1')
        sol = mcdm(table_data, table_data1)
        best_alternative = sol[0]
        best_perf_score = sol[1]
        best_alternative = [str(i) for i in best_alternative]
        table_data = [[str(i) for i in sublist] for sublist in table_data]
        criteriaName = []
        criterionType = []
        for i in range(len(table_data1)):
            if i % 2 == 0:
                criteriaName.append(table_data1[i])
            else:
                criterionType.append(table_data1[i])

        new_criteria = Criteria(
                                    criteriaName=json.dumps(criteriaName),
                                    criteriaType=json.dumps(criterionType))
        storage.new(new_criteria)
        # Save alternative and values
        criteriaName_json = json.dumps(criteriaName)
        best_alternative_json = json.dumps(best_alternative)

        # Create a new Result instance
        new_result = Result(
                                criteria_name=criteriaName_json,
                                best_alternative=best_alternative_json,
                                performance_score=best_perf_score)
        storage.new(new_result)

        new_alternative = Alternative(
            criteria_values=json.dumps(table_data),
            criteria_name=json.dumps(criteriaName),
        )
        storage.new(new_alternative)
        storage.save()
        return jsonify({
            'best_alternative': best_alternative,
            'best_perf_score': best_perf_score,
            'message': 'Data received successfully'
        })
    return render_template('index.html')

@app.route('/about_us', strict_slashes=False)
def about_us():
    """ the about us route """
    return render_template('about_us.html')

@app.route('/contact_us', strict_slashes=False)
def contact_us():
    """ the contact us route """
    return render_template('contact_us.html')


def mcdm(table_data, table_data1):
    """ MCDM ALGORITHM """
    criteriaName = []
    criterionType = []
    criteriaDic = {}
    # seperating the criteiaName and the criteriaType for ease of processing
    for i in range(len(table_data1)):
        if i % 2 == 0:
            criteriaName.append(table_data1[i])
        else:
            criterionType.append(table_data1[i])
    criterionType_copy = copy.copy(criterionType)
    #  creating a dictionary from the criterianame and criteria type
    for key in criteriaName:
        for value in criterionType_copy:
            criteriaDic[key] = value
            criterionType_copy.remove(value)
            break
    # print("criteriaDic", criteriaDic)
    sortcriterias = []

    mm_per_sco_cri = []
    norm_deci_mat = copy.deepcopy(table_data)
    
    # sorting based on column i.e criteria value column wise
    for i in range(0, len(table_data[0])):
        s = []
        for j in range(0, len(table_data)):
            collumn_vals = table_data[j][i]
            s.append(collumn_vals)
        if criterionType[i] == 'Beneficial':
            mm_per_sco_cri.append(max(s))
        else:
            mm_per_sco_cri.append(min(s))
    for m in range(0, len(table_data[0])):
        key_value_pairs = list(criteriaDic.items())
        for n in range(0, len(table_data)):
            if key_value_pairs[m][1] == 'Beneficial':
                norm_deci_mat[n][m] = table_data[n][m]/mm_per_sco_cri[m]
            else:
                norm_deci_mat[n][m] = mm_per_sco_cri[m]/table_data[n][m]
    # weightage normalized decision matrix computation
    weig_norm_dec_mat = copy.deepcopy(norm_deci_mat)
    if 100 % len(criteriaName) == 0:
        weightage = 100/len(criteriaName)
        weightage_deci = weightage/100
        for p in range(0, len(norm_deci_mat[0])):
            for q in range(0, len(norm_deci_mat)):
                weig_norm_dec_mat[q][p] = norm_deci_mat[q][p] * weightage_deci
    else:
        weightage = 100/len(criteriaName)
        compu = weightage * 3
        reminder = 100 - compu
        weightage_remainder = weightage + reminder
        weightage_deci = weightage/100
        weig_rem_deci = weightage_remainder/100
        for p in range(0, len(norm_deci_mat[0])):
            for q in range(0, len(norm_deci_mat)):
                if p == 0:
                    weig_norm_dec_mat[q][p] = norm_deci_mat[q][p] * \
                                                weig_rem_deci
                else:
                    weig_norm_dec_mat[q][p] = norm_deci_mat[q][p] * \
                                                weightage_deci

    # computation of performance score from
    # weightage normalized decision matrix
    perf_score = []
    for a in range(len(weig_norm_dec_mat)):
        perf_score.append(sum(weig_norm_dec_mat[a]))
    best_perf_score = max(perf_score)
    indexx_best_perf_score = perf_score.index(best_perf_score)
    best_alternative = table_data[indexx_best_perf_score]
    return (best_alternative, best_perf_score)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
