import json

import firebase_admin
import requests
from firebase_admin import credentials, firestore, auth

from model.User import User
from util import Status, key

cred = credentials.Certificate('util/dilmil-firebase-adminsdk-e104a-9efd465be8.json')
firebase_admin.initialize_app(credential=cred)
db = firestore.client()

AUTH_URL = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key='


def login(email, password):
    request_ref = AUTH_URL + key.API_KEY
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True})
    request_object = requests.post(request_ref, headers=headers, data=data)
    # raise_detailed_error(request_object)
    current_user = request_object.json()
    return current_user


def get_all_users() -> list:
    fire_users = db.collection(u'USERS').get()
    users = []
    for fire_user in fire_users:
        user = User(fire_user)
        users.append(user)
    return users


def get_user_by_id(user_id: str) -> User:
    fire_user = db.collection(u'USERS').document(user_id).get()
    if fire_user.exists:
        user = User(fire_user)
        return user
    else:
        return Status.USER_ID_NOT_FOUND


def get_user_by_email(user_email: str) -> User:
    try:
        user = auth.get_user_by_email(user_email)
        return get_user_by_id(user.uid)
    except auth.AuthError:
        return Status.EMAIL_NOT_FOUND.jsonify()


def get_users_with_filter(min_age: int, max_age: int, sex: str) -> list:
    users_ref = db.collection(u'USERS')
    if sex:
        users_ref = users_ref.where(u'age', u'>=', min_age).where(u'age', u'<=', max_age).where(u'sex', u'==', sex)
    else:
        users_ref = users_ref.where(u'age', u'>=', min_age).where(u'age', u'<=', max_age)
    filtered_user_docs = users_ref.get()
    return [User(fire_user) for fire_user in filtered_user_docs]


def get_likes(user_id):
    users = []
    user_likes = db.collection(u'USERS').document(user_id).collection(u'LIKES').get()

    for liked_user_id in user_likes:
        fire_user_doc = db.collection(u'USERS').document(liked_user_id.id).get()
        user = User(fire_user_doc)
        users.append(user)
    return users


def get_liked_by(user_id):
    users = []
    user_likes = db.collection(u'USERS').document(user_id).collection(u'LIKED_BY').get()

    for liker_user_id in user_likes:
        fire_user_doc = db.collection(u'USERS').document(liker_user_id.id).get()
        user = User(fire_user_doc)
        users.append(user)
    return users


def get_dislikes(user_id):
    users = []
    user_dislikes = db.collection(u'USERS').document(user_id).collection(u'DISLIKES').get()

    for disliked_user_id in user_dislikes:
        fire_user_doc = db.collection(u'USERS').document(disliked_user_id.id).get()
        user = User(fire_user_doc)
        users.append(user)
    return users


def get_disliked_by(user_id):
    users = []
    user_dislikes = db.collection(u'USERS').document(user_id).collection(u'DISLIKED_BY').get()

    for disliker_user_id in user_dislikes:
        fire_user_doc = db.collection(u'USERS').document(disliker_user_id.id).get()
        user = User(fire_user_doc)
        users.append(user)
    return users


def get_matches(user_id):
    likes = get_likes(user_id)
    liked_by = get_liked_by(user_id)

    matches = list(set(likes).intersection(liked_by))
    return matches


def get_potential_matches(user_id):
    curr_user = get_user_by_id(user_id)
    if isinstance(curr_user, User):
        min_potential_age = curr_user.age - 5
        max_potential_age = curr_user.age + 5
        potential_sex = 'F' if curr_user.sex == 'M' else 'M'

        users_ref = db.collection(u'USERS')
        users_ref = users_ref\
            .where(u'age', u'>=', min_potential_age)\
            .where(u'age', u'<=', max_potential_age)\
            .where(u'sex', u'==', potential_sex)

        users = users_ref.get()
        return [User(user) for user in users]
    else:
        return Status.USER_ID_NOT_FOUND


def update_name(user_id, user_new_name):
    curr_user = get_user_by_id(user_id)
    curr_user.name = user_new_name
    db.collection(u'USERS').document(user_id).set(curr_user.to_json())
    return Status.UPDATE_SUCCESSFUL.to_json()


def update_age(user_id, user_new_age):
    curr_user = get_user_by_id(user_id)
    curr_user.age = int(user_new_age)
    db.collection(u'USERS').document(user_id).set(curr_user.to_json())
    return Status.UPDATE_SUCCESSFUL.to_json()


def update_bio(user_id, user_new_bio):
    curr_user = get_user_by_id(user_id)
    curr_user.bio = user_new_bio
    db.collection(u'USERS').document(user_id).set(curr_user.to_json())
    return Status.UPDATE_SUCCESSFUL.to_json()


def add_stub_user_data():
    user1 = auth.create_user(
        email='jake@gmail.com',
        email_verified=False,
        password='password',
        disabled=False)

    user1_json = {
        'name': 'Jake Ballmer',
        'age': 19,
        'bio': 'Junior at Harvard, favorite activity is scuba diving',
        'sex': 'M',
        'email': user1.email,
        'user_id': user1.uid
    }

    user2 = auth.create_user(
        email='emily@gmail.com',
        email_verified=False,
        password='password',
        disabled=False)

    user2_json = {
        'name': 'Emily Davidson',
        'age': 29,
        'bio': 'Physician at UPenn, watching Netflix is my hobby',
        'sex': 'F',
        'email': user2.email,
        'user_id': user2.uid
    }

    user3 = auth.create_user(
        email='amanda@gmail.com',
        email_verified=False,
        password='password',
        disabled=False)

    user3_json = {
        'name': 'Amanda Johnson',
        'age': 31,
        'bio': 'Architect engineer, loves cooking food',
        'sex': 'F',
        'email': user3.email,
        'user_id': user3.uid
    }

    user4 = auth.create_user(
        email='priyanka@gmail.com',
        email_verified=False,
        password='password',
        disabled=False)

    user4_json = {
        'name': 'Priyanka Shah',
        'age': 21,
        'bio': 'Pursuing business at Yale, SRK fan',
        'sex': 'F',
        'email': user4.email,
        'user_id': user4.uid
    }

    user5 = auth.create_user(
        email='rohit@gmail.com',
        email_verified=False,
        password='password',
        disabled=False)

    user5_json = {
        'name': 'Rohit Sharma',
        'age': 30,
        'bio': 'Actor, Chef, Runner #marvel fan',
        'sex': 'M',
        'email': user5.email,
        'user_id': user5.uid
    }

    db.collection(u'USERS').document(user1.uid).set(user1_json)
    db.collection(u'USERS').document(user2.uid).set(user2_json)
    db.collection(u'USERS').document(user3.uid).set(user3_json)
    db.collection(u'USERS').document(user4.uid).set(user4_json)
    db.collection(u'USERS').document(user5.uid).set(user5_json)
