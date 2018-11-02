from flask_restful import Api

from .users import User, UserList

api = Api(prefix='/api/v1')
api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<first_name>')
