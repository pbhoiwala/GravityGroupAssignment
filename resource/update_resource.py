from flask import Blueprint, jsonify, request
from util import fire, Status

update_app = Blueprint('update_app', __name__, template_folder='templates')


@update_app.route('/user/update/name', methods=['POST'])
def update_user_name():

    user_id = request.form.get('user_id')
    user_new_name = request.form.get('new_name')

    if user_id is None:
        return Status.MISSING_ATTR_USER_ID.jsonify()
    if user_new_name is None:
        return Status.MISSING_ATTR_NEW_NAME.jsonify()

    return jsonify(fire.update_name(user_id, user_new_name))


@update_app.route('/user/update/age', methods=['POST'])
def update_user_age():

    user_id = request.form.get('user_id')
    user_new_age = request.form.get('new_age')

    if user_id is None:
        return Status.MISSING_ATTR_USER_ID.jsonify()
    if user_new_age is None:
        return Status.MISSING_ATTR_NEW_AGE.jsonify()

    return jsonify(fire.update_age(user_id, user_new_age))


@update_app.route('/user/update/bio', methods=['POST'])
def update_user_bio():

    user_id = request.form.get('user_id')
    user_new_bio = request.form.get('new_bio')

    if user_id is None:
        return Status.MISSING_ATTR_USER_ID.jsonify()
    if user_new_bio is None:
        return Status.MISSING_ATTR_NEW_BIO.jsonify()

    return jsonify(fire.update_bio(user_id, user_new_bio))



