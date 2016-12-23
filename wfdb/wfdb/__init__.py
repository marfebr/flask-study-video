import os

from flask import Flask

from flask_login import current_user
from flask_principal import identity_loaded, UserNeed, RoleNeed

from flask_admin.contrib.fileadmin import FileAdmin 

from wfdb.models import (
    db,
    User,
    Post,
    Actor,
    Role,
    MovieRole,
    Tag,
    Comment
    )
from wfdb.controllers.main import main_blueprint
from wfdb.controllers.blog import blog_blueprint

from wfdb.extensions import (
    login_manager,
    principal,
    rest_api,
    admin,
    toolbar,
    cache,
    assets_env,
    mail, celery
    )


from wfdb.assets import main_js, main_css

from wfdb.controllers.rest.movie import MovieAPI
from wfdb.controllers.rest.actor import ActorAPI

from wfdb.controllers.rest.auth import AuthAPI

from wfdb.tasks import echo

from wfdb.controllers.admin import ModelView, CustomView, CustomModelView, ActorView, UserView, CustomFileView

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    login_manager.init_app(app)
    principal.init_app(app)
    admin.init_app(app)
    toolbar.init_app(app)
    cache.init_app(app)
    assets_env.init_app(app)
    mail.init_app(app)
    celery.init_app(app)


    assets_env.register('main_js', main_js)
    assets_env.register('main_css', main_css)

    rest_api.add_resource(
        AuthAPI,
        '/api/auth',
        )
    rest_api.add_resource(
        MovieAPI, 
        '/api/movie/',
        '/api/movie/<int:movie_id>'
        )

    rest_api.add_resource(
        ActorAPI,
        '/api/actor',
        '/api/actor/<int:actor_id>'
        )
   

    rest_api.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(blog_blueprint)

    admin.add_view(
        CustomView()
        )
    admin.add_view(
        UserView(
            User, db.session
        )
    )
    admin.add_view(
        ActorView(
            Actor, db.session
        )
    )
    models = [
        Post,
        Role,
        MovieRole,
        Tag,
        Comment
    ]
    for model in models:
        admin.add_view(
            CustomModelView(model, db.session, category='models')
            )

    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    admin.add_view(
        CustomFileView(
            static_dir,
            '/static/',
            name="Static FIles"
        )
        )

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        #identidade do objeto corrente
        identity.user = current_user
        #Add userNeed to the identity
        if hasattr(current_user,'id'):
            identity.provides.add(UserNeed(current_user.id))
        
        #add rules in user
        if hasattr(current_user,'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

    return app

if __name__ == "__main__":
    app.run(debug=True)
