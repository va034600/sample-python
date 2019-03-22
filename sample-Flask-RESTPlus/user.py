import datetime
from flask import request
from flask_restplus import Resource, fields, Namespace

user_namespace = Namespace('users')

user_model = user_namespace.model('User MODEL', {
    'user_id': fields.Integer(description='ユーザID'),
    'user_name': fields.String(description='ユーザ名'),
    'created_date': fields.DateTime(
        description='作成日',
        example='2019-03-01T22:30:15.491Z'
    )
})

user_parameter = user_namespace.model('User POST', {
    'user_name': fields.String(
        required=True,
        description='ゆーざ名',
        example='ゆーざ'
    )
})


@user_namespace.route('/<int:user_id>')
class Example(Resource):
    @user_namespace.marshal_with(user_model)
    @user_namespace.expect(user_parameter)
    @user_namespace.doc(params={'user_id': 'ユーザid'})
    def post(self, user_id):
        """
        ユーザPOST
        """
        return {'user_id': user_id, "user_name": request.json['user_name'], "created_date": datetime.datetime.today()}
