from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return {"data": "Hello World"} # return a json format
    def post(self):
        return {"data": "Hello Posted"} 
    
    
api.add_resource(Hello, "/hello")

if __name__ == "__main__":
    app.run(debug=True)
 

