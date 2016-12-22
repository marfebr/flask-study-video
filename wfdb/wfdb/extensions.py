from flask_login import LoginManager
from flask_principal import Principal, Permission, RoleNeed

from flask_admin import Admin

from flask_restful import Api

from flask_debugtoolbar import DebugToolbarExtension

from flask_cache import Cache

from flask_assets import Environment

from flask_mail import Mail
#from wfdb.models import User


login_manager = LoginManager()
login_manager.login_view = 'main.login'
toolbar = DebugToolbarExtension()

cache  = Cache()
assets_env = Environment()

mail  = Mail()

rest_api = Api()
admin = Admin()

principal = Principal()


admin_permission = Permission(RoleNeed('admin'))
default_permission = Permission(RoleNeed('default'))


#def load_user(userid):
#    return User.query.get(userid)
