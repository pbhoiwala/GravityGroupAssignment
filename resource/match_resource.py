from flask import Blueprint, request, jsonify
from util import fire, Status

match_app = Blueprint('match_app', __name__, template_folder='templates')


@match_app.route('/matches', methods=['GET'])
def get_matches_for_user():
    """Gets matches for the given user
    Params: 'user_id' passed in using form
    Return: List of Users that have matched with the current user
    """

    user_id = request.form.get('user_id')

    if user_id is None:
        return Status.MISSING_ATTR_GET_USER.jsonify()

    matches = fire.get_matches(user_id)

    if not matches:
        return Status.NO_MATCHES.jsonify()
    else:
        return jsonify([user.to_json() for user in matches])


@match_app.route('/potential_matches', methods=['GET'])
def get_potential_matches_for_user():
    """Gets potential matches for the given user
    The potential users are of opposite gender and their
    age is 5 years older or younger than given user
    Params: 'user_id" passed in using form
    Return: List of potential Users"""

    user_id = request.form.get('user_id')

    if user_id is None:
        return Status.MISSING_ATTR_GET_USER.jsonify()

    potential_matches = fire.get_potential_matches(user_id)

    if not potential_matches:
        return Status.NO_POTENTIAL_MATCHES.jsonify()
    else:
        return jsonify([user.to_json() for user in potential_matches])

