from project import app, db
from flask import request, jsonify
from project.models import User, Company



@app.route('/', methods=['GET'])
def home():
    result = {'msg' : 'Hello world'}
    return jsonify(result)
    
@app.route('/allcomputers', methods = ['GET'])
def fetch_all():
    #initializing all data structure
    dictbody ={}
    result = []

    #get query object for all companies in the database
    all_computers = Company.query.order_by(Company.id).all()

    #loop through all the items in the query object if record exists
    if all_computers:
        for computer in all_computers:
            dictbody['id'] = computer.id
            dictbody['name'] = computer.name
            dictbody['price'] = computer.price
            dictbody['ram_size'] = str(computer.ram_size) + 'GB'
            dictbody['disk_size'] = str(computer.disk_size) + 'GB'
            dictbody['qty'] = computer.qty
            result.append(dictbody)

        #serializing for json type
        return jsonify(result)

@app.route('/allcomputers/<id>', methods = ['GET'])
def fetch_detail(id):
    #initializing all data structure
    dictbody ={}
    result = []

    #get query object for all companies in the database
    computer = Company.query.filter_by(id = id).first()

    #loop through all the items in the query object if record exists
    if computer:
    # for computer in computers:
        dictbody['id'] = computer.id
        dictbody['name'] = computer.name
        dictbody['price'] = computer.price
        dictbody['ram_size'] = str(computer.ram_size) + 'GB'
        dictbody['disk_size'] = str(computer.disk_size) + 'GB'
        dictbody['qty'] = computer.qty
        result.append(dictbody)
            
        #serializing for json type
        return jsonify(result) 


if __name__ == '__main__':
    app.run()