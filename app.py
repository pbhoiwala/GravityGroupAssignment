from flask import Flask, Blueprint

from resource.login_resource import login_app
from resource.user_resource import user_app
from resource.like_resource import like_app
from resource.dislike_resource import dislike_app
from resource.match_resource import match_app
from resource.update_resource import update_app

main_app = Blueprint('main_app', __name__, template_folder='templates')

gravity = Flask(__name__)
gravity.register_blueprint(main_app)
gravity.register_blueprint(login_app)
gravity.register_blueprint(user_app)
gravity.register_blueprint(like_app)
gravity.register_blueprint(dislike_app)
gravity.register_blueprint(match_app)
gravity.register_blueprint(update_app)


@gravity.route('/')
def hello_world():
    # TODO return docs here
    return 'Hello World!'


if __name__ == '__main__':
    gravity.run()

