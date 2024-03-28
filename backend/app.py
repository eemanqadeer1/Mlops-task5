from flask import Flask, request,jsonify  
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["mydatabase"]
collection = db["userdata"]

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    print(email)

    # Inserting data into MongoDB
    collection.insert_one({'name': name, 'email': email})

    return 'Data received and stored successfully!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
