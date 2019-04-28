from time import time
from flask import Blueprint, request, jsonify
from util import fire, Status

dislike_app = Blueprint('dislike_app', __name__, template_folder='templates')


@dislike_app.route('/dislike', methods=['POST'])
def dislike_user():
    """When a person dislikes another person, the person who disliked is the current_user
   and the person who got disliked is the disliked_user. In the database for current_user's
   DISLIKES, the disliked_person's user_id is added and in disliked_user's DISLIKED_BY table.
   Params: 'current_user_id' and 'disliked_user_id' passed in using form
   Return: Status OK if the task is successful"""
    
    cur_time = time()
    current_user_id, disliked_user_id = request.form.get('current_user_id'), request.form.get('disliked_user_id')
    if current_user_id is None or disliked_user_id is None:
        return Status.MISSING_ATTR_USER_ID_DISLIKE.jsonify()

    current_user_dislikes = fire.db.collection(u'USERS').document(current_user_id).collection(u'DISLIKES').document(
        disliked_user_id)
    current_user_dislikes.set({'timestamp': cur_time})

    disliked_by = fire.db.collection(u'USERS').document(disliked_user_id).collection(u'DISLIKED_BY').document(
        current_user_id)
    disliked_by.set({'timestamp': cur_time})

    return jsonify(Status.ACTION_SUCCESSFUL.to_json())


@dislike_app.route('/dislikes', methods=['GET'])
def get_dislikes():
    """Gets dislikes made by the given user
    Params: 'user_id' passed in using form
    Return: List of users that were disliked by given user"""

    user_id = request.form.get('user_id')
    if user_id is None:
        return Status.MISSING_ATTR_USER_ID.jsonify()

    users = fire.get_dislikes(user_id)

    if not users:
        return Status.NO_DISLIKES.jsonify()
    else:
        return jsonify([user.to_json() for user in users])


@dislike_app.route('/dislikedby', methods=['GET'])
def get_disliked_by():
    """Gets list of users that disliked the given user
    Params: 'user_id' passed in using form
    Return: List of users that disliked the given user"""

    user_id = request.form.get('user_id')
    if user_id is None:
        return Status.MISSING_ATTR_USER_ID.jsonify()

    users = fire.get_disliked_by(user_id)

    if not users:
        return Status.NO_DISLIKES.jsonify()
    else:
        return jsonify([user.to_json() for user in users])


