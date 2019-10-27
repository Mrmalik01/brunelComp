from flask import Flask, request, send_file, jsonify
import requests
import numpy as np
from stegano import lsb
import json

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "uploads"
app.config['DATABASE'] =  'database/database.json'

@app.route("/login-request")
def login():
    hdr = request.headers
    username = hdr.get("username")
    password = hdr.get("password")
    try:
        file = open(app.config['DATABASE'], 'r')
        users = json.loads(file.read())
        if username in users:
            if users[username]['password'] == password:
                return jsonify({"message" : "user authorised"}), 200
            else:
                return jsonify({"message" : "user password is wrong"}), 401 
        return jsonify({"message" : "user does not exist"}), 404
    except:
        return jsonify({"message" : "user does not exist"}), 500

@app.route("/register", methods=['GET'])
def register():
    headers = request.headers
    username = headers.get("username")
    password = headers.get("password")
    public_key = headers.get("pubkey")
    read = True
    try:
        file = open(app.config['DATABASE'], 'r')
        users = json.loads(file.read())
        if username in users:
            print("User exist")
            file.close()
            return jsonify({"message" : "username already exist"}), 400
        else:
            users[username] = {
                "password" : password,
                "public_key" : public_key
            }
            print("User added")
            file.close()
            return jsonify({"message" : "user created"}), 201

    except:
        read = False
        file = open(app.config['DATABASE'], "w+")
        users = {username : {
            "password" : password,
            "public_key" : public_key
        }}
        file.write(json.dumps(users))
        file.close()
        print("New file saved")
        return jsonify({"message" : "user created"}), 201




@app.route("/users")
def getAllUsers():
    try:
        file = open(app.config['DATABASE'], 'r')
        users = json.loads(file.read())
        us = []
        for user in users:
            us.append({"username": user, "public_key" : users[user]['public_key']})
        result = {"users" : us}
        return result
    except:
        return jsonify({"message" : "no users"}), 404

import os
@app.route("/encrypt", methods=['POST'])
def encrypt():
    headers = request.headers
    msg = headers.get("coded-msg")
    image = request.files
    file = ""
    for file in image:
        file = image[file]
        break
    file.save(os.path.join(app.config["IMAGE_UPLOADS"], file.filename))
    print("Image saved")
    secret = lsb.hide(os.path.join(app.config["IMAGE_UPLOADS"], file.filename), str(msg))
    secret.save(os.path.join(app.config["IMAGE_UPLOADS"], "encodedImage.png"))
    print("Image encrypted")
    print(lsb.reveal(os.path.join(app.config["IMAGE_UPLOADS"], "encodedImage.png")))
    return send_file(os.path.join(app.config["IMAGE_UPLOADS"], "encodedImage.png"), mimetype='image/png')

@app.route("/decrypt", methods=['POST'])
def decrypt():
    image = request.files
    file = ""
    for file in image:
        file = image[file]
        break
    file.save(os.path.join(app.config["IMAGE_UPLOADS"], "encoded-"+file.filename))
    print("Image saved")
    msg = lsb.reveal(os.path.join(app.config["IMAGE_UPLOADS"], "encoded-"+file.filename))
    print("Image decrypted")
    return msg



if __name__ == "__main__":
    app.run(port=5000, debug=True)