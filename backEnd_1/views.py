from flask import jsonify, request
from backEnd_1 import app
import datetime
CATEGORIES = [
    {
        "id": 1,
        "name": "Food",
    },
]

USERS = [
    {
        "id": 1,
        "name": "Sofiia Vozniak",
    },
]

RECORDS = [
    {
        "id": 1,
        "userID": 1,
        "categoryID": 1,
        "date": datetime.datetime.now(),
        "cost": 100,
    },
]

# GET /categories, /users, /records
# POST /category, /user, /record

@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})

@app.route("/category", methods=['POST'])
def create_category():
    request_data = request.get_json()
    CATEGORIES.append(request_data)
    return jsonify({request_data})

@app.route("/users")
def get_users():
    return jsonify({"users": USERS})

@app.route("/user", methods=['POST'])
def create_user():
    request_data = request.get_json()
    USERS.append(request_data)
    return jsonify({request_data})

@app.route("/records")
def get_records():
    return jsonify({"records": RECORDS})

@app.route("/record", methods=['POST'])
def create_record():
    request_data = request.get_json()
    RECORDS.append(request_data)
    return jsonify({request_data})