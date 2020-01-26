from project import app, db
from flask import request, jsonify
from project.models import User, Computer


@app.route('/addcomputer', methods=['POST'])
def addcomputer():
    
    # retriving all fields from send

    name = request.json['name']
    price = request.json['price']
    ram_size =request.json['ram_size']
    disk_size = request.json['disk_size']
    quantity = request.json['quantity']

    # creating a computer object
    newcomputer = Computer(name, price, ram_size, disk_size, quantity)

    #adding a new computer
    db.session.add(newcomputer)
    db.session.commit()

    return jsonify({'status' : 200,'message' : 'ok', 'id' : newcomputer.id})
    
@app.route('/computers', methods = ['GET'])
def fetch_all():

    #initializing all data structure
    dictbody ={}
    result = []

    #get query object for all companies in the database
    all_computers = Computer.query.order_by(Computer.id).all()

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
        return jsonify({'status' : 200,'message' : 'ok','data' : result})



@app.route('/computer/<id>', methods = ['GET'])
def fetch_detail(id):

    #initializing all data structure
    dictbody ={}
    result = []

    #get query object for all companies in the database
    computer = Computer.query.filter_by(id = id).first()

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
        return jsonify ({'status' : 200,'message' : 'ok','data' : result})


if __name__ == '__main__':
    app.run()