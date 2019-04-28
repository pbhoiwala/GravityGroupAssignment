from flask import jsonify


class Status:

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def jsonify(self):
        e = {
            'code': self.code,
            'message': self.message
        }
        return jsonify(e)

    def to_json(self):
        e = {
            'code': self.code,
            'message': self.message
        }
        return e


MISSING_ATTR_USER_ID = Status(1, "Missing attribute in request form. 'user_id' must be passed in "
                              "using form in the request")

MISSING_ATTR_USER_ID_LIKE = Status(2, "Missing attributes in request form. 'current_user_id' and 'liked_user_id' "
                                      "must be passed in using form in the request")

MISSING_ATTR_USER_ID_DISLIKE = Status(3, "Missing attributes in request form. 'current_user_id' and 'disliked_user_id'"
                                      " must be passed in using form in the request")

MISSING_ATTR_AUTH = Status(4, "Missing attributes in request form. 'email' and 'password' "
                           "must be passed in using form in the request")

MISSING_ATTR_GET_USER = Status(5, "Missing attributes in request form. 'email' or 'user_id' "
                               "must be passed in as the request parameters")

EMAIL_NOT_FOUND = Status(6, "User with the given email does not exist in the database")

USER_ID_NOT_FOUND = Status(7, "User with the given id does not exist in the database")

NO_LIKES = Status(8, "User has no likes")

NO_DISLIKES = Status(9, "User has no dislikes")

NO_MATCHES = Status(10, "User has no matches")

NO_POTENTIAL_MATCHES = Status(11, "No potential matches found for user")

MISSING_ATTR_NEW_NAME = Status(12, "Missing attributes in request form. 'new_name' must be passed in using"
                                   "form in the request")

MISSING_ATTR_NEW_AGE = Status(13, "Missing attributes in request form. 'new_age' must be passed in using "
                                  "form in the request")

MISSING_ATTR_NEW_BIO = Status(14, "Missing attributes in request form. 'new_bio' must be passed in using "
                                  "form in the request")

ACTION_SUCCESSFUL = Status(15, "Action successfully processed")

UPDATE_SUCCESSFUL = Status(16, "Update request successfully processed")



