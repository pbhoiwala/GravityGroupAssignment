from util import fire, Status
from flask import jsonify, request, Blueprint

login_app = Blueprint('login_app', __name__, template_folder='templates')


@login_app.route('/login', methods=['POST'])
def login_with_email_and_password():
    """Logs a user in with given email and password.
    Params: 'email' and 'password' passed in using a form
    Return: logged in user object"""

    email, password = request.form.get('email'), request.form.get('password')

    if email is None or password is None:
        return Status.MISSING_ATTR_AUTH.jsonify()

    current_user = fire.login(email, password)
    return jsonify(current_user)


