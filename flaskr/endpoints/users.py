from flask_restful import Resource, request

from ..mongo import mongo
from ..forms.user_form import UserForm


class User(Resource):
    def get(self, first_name):
        user = mongo.db.users.find_one_or_404({
            'first_name': first_name
        })

        output = {
            'result': {
                'first_name': user['first_name'],
                'last_name': user['last_name'],
            }
        }

        return output, 200


class UserList(Resource):
    def get(self):
        """
        Gets a list of users
        :return:
        """
        users = []

        for u in mongo.db.users.find():
            users.append({
                'first_name': u['first_name'],
                'last_name': u['last_name']
            })

        output = {'results': users}

        return output, 200

    def post(self):
        """
        Creates a new user
        :return:
        """
        form = UserForm(request.form)

        if not form.validate():
            return 'ko', 400

        _id = mongo.db.users.insert({
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name']
        })

        last_user = mongo.db.users.find_one({'_id': _id})

        output = {
            'result': {
                'first_name': last_user['first_name'],
                'last_name': last_user['last_name'],
            }
        }

        return output, 201
