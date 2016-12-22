from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from flask import abort, current_app
from flask_restful import Resource, abort

from wfdb.models import User, Role

from .parsers import user_auth_post_parser

def create_serializer():
    return Serializer(current_app.config['SECRET_KEY'], expires_in=604800)

class AuthAPI(Resource):
    def post(self):
        args = user_auth_post_parser.parse_args()
        user = User.query.filter_by(username=args['username']).one()

        if user.check_password(args['password']):
            s = create_serializer()
            return {"token": s.dumps({'id':user.id})}
        else:
            abort(404)

def abort_if_no_admin_auth(token):
    try:
        s = create_serializer()
        id = s.loads(token)['id']
    except Exception as e:
        abort(401,message="Token {}".format(e))
    
    user = User.query.get(id)

    if user is None:
        abort(401,message="User with if {} doesn't exists".format(id))
    
    
    admin_role = Role.query.filter_by(name='admin').one()

    if admin_role not in user.roles:
        abort(403)