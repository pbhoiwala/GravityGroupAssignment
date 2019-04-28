from time import time
from flask import Blueprint, request, jsonify
from util import Status, fire

like_app = Blueprint('like_app', __name__, template_folder='templates')


@like_app.route('/like', methods=['POST'])
def like_user():
    """When a person likes another person, the person who liked is the current_user
    and the person who got liked is the liked_user. In the database for current_user's
    LIKES, the liked_person's user_id is added and in liked_user's LIKED_BY table.
    Params: 'current_user_id' and 'liked_user_id' passed in using form
    Return: Status OK if the task is successful"""

    cur_time = time()
    current_user_id, liked_user_id = request.form.get('current_user_id'), request.form.get('liked_user_id')
    if current_user_id is None or liked_user_id is None:
        return Status.MISSING_ATTR_USER_ID_LIKE.jsonify()

    current_user_likes = fire.db.collection(u'USERS').document(current_user_id).collection(u'LIKES').document(liked_user_id)
    current_user_likes.set({'timestamp': cur_time})

    liked_by = fire.db.collection(u'USERS').document(liked_user_id).collection(u'LIKED_BY').document(current_user_id)
    liked_by.set({'timestamp': cur_time})

    return jsonify(Status.ACTION_SUCCESSFUL.to_json())


@like_app.route('/likes', methods=['GET'])
def get_likes():
    """Gets likes made by the given user
    Params: 'user_id' passed in using form
    Return: List of users that were liked by given user"""

    user_id = request.form.get('user_id')
    if user_id is None:
        return Status.MISSING_ATTR_USER_ID.jsonify()

    users = fire.get_likes(user_id)

    if not users:
        return Status.NO_LIKES.jsonify()
    else:
        return jsonify([user.to_json() for user in users])


@like_app.route('/likedby', methods=['GET'])
def get_liked_by():
    """Gets list of users that liked the given user
    Params: 'user_id' passed in using form
    Return: List of users that liked the given user"""

    user_id = request.form.get('user_id')
    if user_id is None:
        return Status.MISSING_ATTR_USER_ID.jsonify()

    users = fire.get_liked_by(user_id)

    if not users:
        return Status.NO_LIKES.jsonify()
    else:
        return jsonify([user.to_json() for user in users])

