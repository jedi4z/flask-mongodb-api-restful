from flask_restful import Api

from .users import UserList

api = Api(prefix='/api/v1')
api.add_resource(UserList, '/user')
