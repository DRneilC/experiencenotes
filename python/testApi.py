#!/usr/bin/python3
#coding=utf-8

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__);
api = Api(app);

class HelloWorld (Resource):
    def post(self):
        return {"hello": "world"}

api.add_resource(HelloWorld, '/');

if __name__ == '__main__':
    app.run(debug=True)
