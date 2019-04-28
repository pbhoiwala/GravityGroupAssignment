import json
from flask import jsonify
from firebase_admin import firestore
from google.cloud.firestore_v1beta1.document import DocumentSnapshot


class User:

    def __init__(self, fire_user: DocumentSnapshot):
        user = fire_user.to_dict()
        self._user_id = user['user_id']
        self._name = user['name']
        self._email = user['email']
        self._bio = user['bio']
        self._age = user['age']
        self._sex = user['sex']

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, bio: str):
        self._bio = bio

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, sex: str):
        self._sex = sex

    def to_json(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'bio': self.bio,
            'age': self.age,
            'sex': self.sex
        }

    def __eq__(self, other_user):
        return isinstance(other_user, User) and self.user_id == other_user.user_id

    def __hash__(self):
        return hash(self.user_id)
















