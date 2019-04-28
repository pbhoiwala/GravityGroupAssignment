from flask import Blueprint, jsonify, request
from util import Status, fire

user_app = Blueprint('user_app', __name__, template_folder='templates')


@user_app.route('/users', methods=['GET'])
def get_all_users():
    """Gets all the users in the Firebase database
    Params: None
    Return: List of Users
    """

    users = [user.to_json() for user in fire.get_all_users()]
    return jsonify(users)


@user_app.route('/user', methods=['GET'])
def get_user():
    """Gets a specific user with the given email or user_id
    Params: URL query parameters with key 'email' or 'user_id'
    Return: User corresponding to the email or user_id
    """

    email = request.args.get('email')
    user_id = request.args.get('user_id')

    if email is not None:
        return jsonify(fire.get_user_by_email(email).to_json())
    elif user_id is not None:
        return jsonify(fire.get_user_by_id(user_id).to_json())
    else:
        return Status.MISSING_ATTR_GET_USER.to_json()


@user_app.route('/users/filter', methods=['GET'])
def get_users_filter():
    """Gets a list of users with given filters
    Params: URL query parameters with key 'min_age', 'max_age' or 'sex'
    Return: Users that fall under teh parameters above"""

    min_age = request.args.get('min_age')
    if not min_age:
        min_age = 0

    max_age = request.args.get('max_age')
    if not max_age:
        max_age = 100

    sex = request.args.get('sex')
    filtered = fire.get_users_with_filter(int(min_age), int(max_age), sex)
    return jsonify([user.to_json() for user in filtered])






