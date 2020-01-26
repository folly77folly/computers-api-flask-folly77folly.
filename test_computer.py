import unittest
from app import fetch_all, addcomputer
import requests, json
from flask import jsonify



class TestingComputers(unittest.TestCase):
    #initializing a va
    computerids = None

    def setUp(self):

        # setting up variables to be used in api post request
        self.computer = {
                        "name": "MacBooks Pro (13-inch, 2017, Two Thunderbolt 3 ports)",
                        "price": 600000,
                        "ram_size": 2,
                        "disk_size": 500,
                        "quantity": 10
                        }    

        self.head = {'Content-Type': 'application/json'}

    def test_add_computer(self):
        #convert data to json
        data =  json.dumps(self.computer)
        head =  (self.head)

        #making the post request
        response = requests.post('http://127.0.0.1:5000/addcomputer', data = data, headers = head)

        #converting response to dictionary
        result=json.loads(response.text)

        #get the id from the response
        computerid = result['id']
        TestingComputers.computerids = computerid


        #testing the requests
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(result, { "message": "ok", "status": 200, 'id': computerid})


    def test_all_computers(self):

        #send a request to the test url
        response = requests.get('http://127.0.0.1:5000/computers')

        #converting response to dictionary
        result = json.loads(response.text)
        result2 = result['data'][0]

        #get the id from the response
        computerid = result['data'][0]['id']

        #checking for correctness of status code
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(result2, {'id': computerid, 'name': 'MacBooks Pro (13-inch, 2017, Two Thunderbolt 3 ports)', 'price': 600000, 'ram_size': '2GB', 'disk_size': '500GB', 'qty': 10})

    def test_fetch_detail(self):
        cid = TestingComputers.computerids

        #send a request to the test url
        response = requests.get(f'http://127.0.0.1:5000/computer/{cid}')

        #converting response to dictionary
        result = json.loads(response.text)
        result2 = result['data'][0]


        #checking for correctness of status code
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(result2, {'id': cid, 'name': 'MacBooks Pro (13-inch, 2017, Two Thunderbolt 3 ports)', 'price': 600000, 'ram_size': '2GB', 'disk_size': '500GB', 'qty': 10})


if __name__ == '__main__':
    unittest.main()
    


