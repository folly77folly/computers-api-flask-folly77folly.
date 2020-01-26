from project import app
from flask import request, jsonify



@app.route('/', methods=['GET'])
def home():
    result = {'msg' : 'Hello world'}
    return jsonify(result)
    

