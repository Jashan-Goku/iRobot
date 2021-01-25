import sys
from flask import Flask
from flask_restx import Resource, Api
from flask_cors import CORS

APP = Flask(__name__)
api = Api(APP, title="iRobot Food Ordering Project")
CORS(APP)
sys.path.insert(0, '')


@api.route('/basic')
class Setup(Resource):
    """
    This is to check application is up or not
    """
    def get(self):
        response = "Application is working"
        return response


if __name__ == '__main__':
    APP.run()
