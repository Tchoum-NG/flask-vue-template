from flask import Flask, jsonify, Response, json
from flask_cors import CORS
from pymongo import MongoClient
app = Flask(__name__)

DEBUG = True

CORS(app, resources={r'/*': {'origins': '*'}})

dbdetails = {
        "database": "cookbook",
        "collection": "recipes",
    }

@app.route('/', methods=['GET'])
def home():
    return jsonify('test')

@app.route('/apitest')
def apitest():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')

@app.route('/readall', methods=['GET'])
def read_all():
    response = MongoAPI(dbdetails).read()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

class MongoAPI:

    def __init__(self, data):
        self.client = MongoClient("mongodb://localhost:5001/")
        database = dbdetails['database']
        collection = dbdetails['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read(self):
        documents = self.collection.find()
        print("READ")
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def delete(self, data):
        filt = data['Document']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output


if __name__ == '__main__':
    app.run(debug=True, port= 5000, host='0.0.0.0')