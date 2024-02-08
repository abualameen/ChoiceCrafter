#!/usr/bin/python3
from models import storage
from models.criteria import Criteria
from models.alternative import Alternative
# from models.alternativevalue import AlternativeValue
from models.result import Result
import copy
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from flask import session
import secrets
import json
# from models.criteria import Criteria
# from models.alternative import Alternative



app = Flask(__name__)

# # Replace 'sqlite:///site.db' with your actual database URI
# CC_MYSQL_USER = getenv('CC_MYSQL_USER')
# CC_MYSQL_PWD = getenv('CC_MYSQL_PWD')
# CC_MYSQL_HOST = getenv('CC_MYSQL_HOST')
# CC_MYSQL_DB = getenv('CC_MYSQL_DB')

# DATABASE_URI = 'mysql+mysqldb://{}:{}@{}/{}'.format(CC_MYSQL_USER,CC_MYSQL_PWD,CC_MYSQL_HOST,CC_MYSQL_DB)
# engine = create_engine(DATABASE_URI)
# Base = declarative_base()
# class Alternative(Base):
#     __tablename__ = 'alternative'
#     id = Column(Integer, primary_key=True)
#     criteria_name = Column(String(100), nullable=False)
#     alternative_values = relationship('AlternativeValue', back_populates='alternative')
#     user_num = relationship('Result', back_populates='alternative')

# class AlternativeValue(Base):
#     __tablename__ = 'alternative_value'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('alternative.id'))
#     alternative_value = Column(Integer, nullable=False)
#     criteria_name = Column(String(100), nullable=False)
#     alternative = relationship('Alternative', back_populates='alternative_values')
#     # results = relationship('Result', back_populates='alternative_values') 
# class Result(Base):
#     __tablename__ = 'result'
#     id = Column(Integer, primary_key=True)
#     criteria_name = Column(String(100), nullable=False)
#     best_alternative = Column(Float, nullable=False)
#     performance_score = Column(Float, nullable=False)
#     user_id = Column(Integer, ForeignKey('alternative.id'))
#     alternative = relationship('Alternative', back_populates='user_num')
    

# class Criteria(Base):
#     __tablename__ = 'criteria'
#     id = Column(Integer, primary_key=True)
#     criteriaName = Column(String(100), nullable=False)
#     criteriaType = Column(String(20), nullable=False)


    # alternative_values = relationship('AlternativeValue', back_populates='results') 



# Base.metadata.create_all(engine)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


# Session = sessionmaker(bind=engine)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data = request.get_json()
        table_data = data.get('tableData')
        table_data = [[float(i) for i in sublist] for sublist in table_data]
        table_data1 = data.get('tableData1')
        sol = mcdm(table_data, table_data1)
        best_alternative = sol[0]
        best_performance_score = sol[1]
        best_alternative = [str(i) for i in best_alternative]
        table_data = [[str(i) for i in sublist] for sublist in table_data]
        criteriaName = []
        criterionType = []
        for i in range(len(table_data1)):
            if i % 2 == 0:
                criteriaName.append(table_data1[i])
            else:
                criterionType.append(table_data1[i])

        new_criteria = Criteria(criteriaName=json.dumps(criteriaName), criteriaType=json.dumps(criterionType))
        storage.new(new_criteria)

       
        # Save alternative and values
        criteriaName_json = json.dumps(criteriaName)
        best_alternative_json = json.dumps(best_alternative)

        # Create a new Result instance
        new_result = Result(criteria_name=criteriaName_json, best_alternative=best_alternative_json, performance_score=best_performance_score)
        storage.new(new_result)

        new_alternative = Alternative(
            criteria_values=json.dumps(table_data),
            criteria_name=json.dumps(criteriaName),
        )
        storage.new(new_alternative)
        storage.save()
        return jsonify({
            'best_alternative': best_alternative,
            'best_performance_score': best_performance_score,
            'message': 'Data received successfully'
        })
    return render_template('index.html')

def mcdm(table_data,table_data1):
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

    maxormin_per_score_criterias = []
    normalize_decision_matrix = copy.deepcopy(table_data)
    # sorting based on column i.e criteria value column wise
    for i in range(0, len(table_data[0])):
        s = []
        
        for j in range(0, len(table_data)):
            collumn_vals = table_data[j][i]
            s.append(collumn_vals)
        
        if criterionType[i] == 'Beneficial':
            maxormin_per_score_criterias.append(max(s))
        else:
            maxormin_per_score_criterias.append(min(s))
    for m in range(0, len(table_data[0])):
        key_value_pairs = list(criteriaDic.items())
        
        for n in range(0, len(table_data)):
            if key_value_pairs[m][1] == 'Beneficial':
                normalize_decision_matrix[n][m] = table_data[n][m]/maxormin_per_score_criterias[m]
            else:
                normalize_decision_matrix[n][m] = maxormin_per_score_criterias[m]/table_data[n][m]
    #weightage normalized decision matrix computation
    weightage_normalized_decision_matrix = copy.copy(normalize_decision_matrix)
    if 100 % len(criteriaName) == 0:
        weightage = 100/len(criteriaName)
        weightage_deci = weightage/100
        for p in range(0, len(normalize_decision_matrix[0])):
            for q in range(0, len(normalize_decision_matrix)):
                weightage_normalized_decision_matrix[q][p] = normalize_decision_matrix[q][p] * weightage_deci
    else:
        weightage = 100/len(criteriaName)
        compu = weightage * 3
        reminder = 100 - compu
        weightage_remainder = weightage + reminder
        weightage_deci = weightage/100
        weightage_remainder_deci = weightage_remainder/100
        for p in range(0, len(normalize_decision_matrix[0])):
            for q in range(0, len(normalize_decision_matrix)):
                if p == 0:
                    weightage_normalized_decision_matrix[q][p] = normalize_decision_matrix[q][p] * weightage_remainder_deci 
                else:
                    weightage_normalized_decision_matrix[q][p] = normalize_decision_matrix[q][p] * weightage_deci

    # computation of performance score from weightage normalized decision matrix
    performance_score = []
    for a in range(len(weightage_normalized_decision_matrix)):
        # for b in range(len(weightage_normalized_decision_matrix[0])):
        performance_score.append(sum(weightage_normalized_decision_matrix[a]))
    best_performance_score = max(performance_score)
    indexx_best_performance_score = performance_score.index(best_performance_score)
    best_alternative = table_data[indexx_best_performance_score]
    return (best_alternative, best_performance_score )




if __name__ == '__main__':
    # app.secret_key = secrets.token_hex(16)  # 16 bytes for a reasonably strong secret key
    app.run(host='0.0.0.0', port=5005, debug=True)
