# Gravity Group API Documentation

The goal of this exercise was to design an API for a dating service like Dil Mil. There are several endpoints that client app can use. Below is the breakdown and description on how to use them.


# Authentication



## `/login`
This endpoint can be used to login a user with their email and password.

Request Type: `POST`
Request Body: `form`
Parameters:
`email`: email address of the user
`password`: password of the account

Sample request:
```
POST: http://127.0.0.1:5000/login
form: {
    email: 'parth.v.bhoiwala@gmail.com',
    password: 'bhoiwala'
}
```
Sample response:
```
{
    "displayName": "",
    "email": "parth.v.bhoiwala@gmail.com",
    "expiresIn": "3600",
    "idToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjY1NmMzZGQyMWQwZmVmODgyZTA5ZTBkODY5MWNhNWM3ZjJiMGQ2MjEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZGlsbWlsIiwiYXVkIjoiZGlsbWlsIiwiYXV0aF90aW1lIjoxNTU2NDc1MDI0LCJ1c2VyX2lkIjoicllOSHA4MXpPd09JekZ3UG5pWEJaNlJSMXF5MSIsInN1YiI6InJZTkhwODF6T3dPSXpGd1BuaVhCWjZSUjFxeTEiLCJpYXQiOjE1NTY0NzUwMjQsImV4cCI6MTU1NjQ3ODYyNCwiZW1haWwiOiJwYXJ0aC52LmJob2l3YWxhQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJwYXJ0aC52LmJob2l3YWxhQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.f_yGB-L6J2c0nKdcZIJUc0Js4Fqe-C897rVGQJawQggPepL0O1NHd9bageH9_78GbNR-C6ppJ-5cX2kcoOtPNcxlLfc3khlmiAwjDS3J94AMpDoTDqsYs6WqfSAeaBJsbqP5zqo1aMR3U9Nkio1a9UnONGqfglrFDLGjoqom0dOJWukHXSQi1-2nR5Qxrxd1qQEixiiIIfIvnaDFx_JZ08L0PFo45y3uEnGw3lLTW-0i06OHXuPZ_gSRyqvsUcU1dczyzn_XBnDe8zzRzmlJ0KVUKPsRj9XzMVcy0LMOSrXwyocevHTynqcfTfL_wPK980IDE2WZh4J5N4k-ISCiww",
    "kind": "identitytoolkit#VerifyPasswordResponse",
    "localId": "rYNHp81zOwOIzFwPniXBZ6RR1qy1",
    "refreshToken": "AEu4IL051M7t7IFbrpav6Ql03JiD1FY8D7GVNico-SCP0d7Hr0DfQWRmvgReaIJloR9Tu1o92YzQgEvZZUmfwbuF3lhjp1wTlVAcUe3D0pJ5CHmsndzdlYmDoj6Fd2hcYR_4ddvYEZAMVT_vR_nH0LGU8b1SlPtdDZOg_tsTLqfA72cOr4PQmNDyY1DpkEbxrzK3dT11-0zs",
    "registered": true
}
```

# Get User Profiles

## `/users`
This endpoint can be used to get a list of all the users in the database.

Request Type: `GET`
Request Body: `-none-`

Sample request:
```
GET: http://127.0.0.1:5000/users
```
Sample response:
```[
    {
        "age": 19,
        "bio": "Junior at Harvard, favorite activity is scuba diving",
        "email": "jake@gmail.com",
        "name": "Jake Ballmer",
        "sex": "M",
        "user_id": "4bEurIdXSBVng0zpWB9GcDzgKks1"
    },
    {
        "age": 29,
        "bio": "Physician at UPenn, watching Netflix is my hobby",
        "email": "emily@gmail.com",
        "name": "Emily Davidson",
        "sex": "F",
        "user_id": "6fiAmbryEaRRFdjfeK8h1tnFj9m1"
    },
    {
        "age": 31,
        "bio": "Architect engineer, loves cooking food",
        "email": "amanda@gmail.com",
        "name": "Amanda Johnson",
        "sex": "F",
        "user_id": "9fmBjsJWuOWA2eS242hEOnXwkEt1"
    },
    {
        "age": 28,
        "bio": "DiCaprio 2, all day, J.I.D",
        "email": "nancy@gmail.com",
        "name": "Nancy DiCaprio",
        "sex": "F",
        "user_id": "Bp75dPhTmWWs88MxHQS2rNlqg9p2"
    },
    {
        "age": 21,
        "bio": "I love art",
        "email": "mary.jane@gmail.com",
        "name": "Mary Jane",
        "sex": "F",
        "user_id": "DxJEk5NAFufZYpH7jXjPTtpzV3r1"
    },
    {
        "age": 26,
        "bio": "Senior @ Dxrexel, Philly, Android, UI, Graphics",
        "email": "michael@gmail.com",
        "name": "Michael DiCioccio",
        "sex": "M",
        "user_id": "HuHRWFGH8yaHm8pOVqjspPtKD4g1"
    },
    {
        "age": 21,
        "bio": "Pursuing business at Yale, SRK fan",
        "email": "priyanka@gmail.com",
        "name": "Priyanka Shah",
        "sex": "F",
        "user_id": "amxiXfkMy7cExPDh8ju1JfQ76MJ3"
    },
    {
        "age": 24,
        "bio": "I love sports, and iOS dev, Ex Intern @Box",
        "email": "satish@gmail.com",
        "name": "Satish Boggarapu",
        "sex": "M",
        "user_id": "otnRgXkDbhQ7SmWesMIBpajfD7d2"
    },
    {
        "age": 23,
        "bio": "Android dev, love coffee and biking, #cricket fan",
        "email": "parth.v.bhoiwala@gmail.com",
        "name": "Parth Shah",
        "sex": "M",
        "user_id": "rYNHp81zOwOIzFwPniXBZ6RR1qy1"
    },
    {
        "age": 30,
        "bio": "Actor, Chef, Runner #marvel fan",
        "email": "rohit@gmail.com",
        "name": "Rohit Sharma",
        "sex": "M",
        "user_id": "x7jnlNxtVff4ZVKv4gGcy4Ffqzz1"
    }
]
```

## `/user`
This endpoint can be used to get a specific user's profile.

Request Type: `GET`
Request Body: `-none-`
URL Parameters:
`email`: email address of the user
`user_id`: user id of the user

Sample request (by email):
```
GET: http://127.0.0.1:5000/user?email=parth.v.bhoiwala@gmail.com
```
Sample response:
```
{
    "age": 23,
    "bio": "Android dev, love coffee and biking, #cricket fan",
    "email": "parth.v.bhoiwala@gmail.com",
    "name": "Parth Shah",
    "sex": "M",
    "user_id": "rYNHp81zOwOIzFwPniXBZ6RR1qy1"
}
```
Sample request (by user id):
```
GET: http://127.0.0.1:5000/user?user_id=6fiAmbryEaRRFdjfeK8h1tnFj9m1
```
Sample response
:
```
{
    "age": 29,
    "bio": "Physician at UPenn, watching Netflix is my hobby",
    "email": "emily@gmail.com",
    "name": "Emily Davidson",
    "sex": "F",
    "user_id": "6fiAmbryEaRRFdjfeK8h1tnFj9m1"
}
```
## `/users/filter`
This endpoint can be used to get a list of users filtered by age and sex.

Request Type: `GET`
Request Body: `-none-`
URL Parameters:
`min_age`: minimum age to filter the users by
`max_age`: maximum age to filter the users by
`sex`: filter users by 'M' or 'F' for Male or Female, respectively

Sample request:
```
GET: http://127.0.0.1:5000/users/filter?min_age=25&max_age=30&sex=F
```
Sample response:
```
[
    {
        "age": 28,
        "bio": "DiCaprio 2, all day, J.I.D",
        "email": "nancy@gmail.com",
        "name": "Nancy DiCaprio",
        "sex": "F",
        "user_id": "Bp75dPhTmWWs88MxHQS2rNlqg9p2"
    },
    {
        "age": 29,
        "bio": "Physician at UPenn, watching Netflix is my hobby",
        "email": "emily@gmail.com",
        "name": "Emily Davidson",
        "sex": "F",
        "user_id": "6fiAmbryEaRRFdjfeK8h1tnFj9m1"
    }
]
```

# Liking 


## `/like`
This endpoint can be used to make a user1 like user2.

Request Type: `POST`
Request Body: `form`
Parameters:
`current_user_id`: user id of the user who performed the like
`liked_user_id`: user id of the user who got liked

Sample request:
```
POST: http://127.0.0.1:5000/like
form: {
    current_user_id: 'x7jnlNxtVff4ZVKv4gGcy4Ffqzz1',
    liked_user_id: 'Bp75dPhTmWWs88MxHQS2rNlqg9p2'
}
```
> In this case, `current_user_id` is "Rohit Sharma" and `liked_user_id` is "Nancy DiCaprio"

Sample Response:
```
{
    "code": 15,
    "message": "Action successfully processed"
}
```

## `/likes`
This endpoint can be used to get a list of users that a given user has liked.
Request Type: `GET`
Request Body: `form`
Parameters:
`user_id`: user id of the user whose likes to fetch

Sample request:
```
GET: http://127.0.0.1:5000/likes
form: {
    user_id: 'rYNHp81zOwOIzFwPniXBZ6RR1qy1',
}
```
> In this case, `user_id` is "Parth Shah"

Sample Response:
```
[
    {
        "age": 28,
        "bio": "DiCaprio 2, all day, J.I.D",
        "email": "nancy@gmail.com",
        "name": "Nancy DiCaprio",
        "sex": "F",
        "user_id": "Bp75dPhTmWWs88MxHQS2rNlqg9p2"
    },
    {
        "age": 21,
        "bio": "I love art",
        "email": "mary.jane@gmail.com",
        "name": "Mary Jane",
        "sex": "F",
        "user_id": "DxJEk5NAFufZYpH7jXjPTtpzV3r1"
    }
]
```

## `/likedby`
This endpoint can be used to get a list of users who have liked a given user.
Request Type: `GET`
Request Body: `form`
Parameters:
`user_id`: user id of the user whose likers to fetch

Sample request:
```
GET: http://127.0.0.1:5000/likedby
form: {
    user_id: 'Bp75dPhTmWWs88MxHQS2rNlqg9p2',
}
```
> In this case, `user_id` is "Nancy DiCaprio"

Sample Response:
```
[
    {
        "age": 23,
        "bio": "Android dev, love coffee and biking, #cricket fan",
        "email": "parth.v.bhoiwala@gmail.com",
        "name": "Parth Shah",
        "sex": "M",
        "user_id": "rYNHp81zOwOIzFwPniXBZ6RR1qy1"
    },
    {
        "age": 30,
        "bio": "Actor, Chef, Runner #marvel fan",
        "email": "rohit@gmail.com",
        "name": "Rohit Sharma",
        "sex": "M",
        "user_id": "x7jnlNxtVff4ZVKv4gGcy4Ffqzz1"
    }
]
```


# Disliking

## `/dislike`
This endpoint can be used to make a user1 dislike user2.

Request Type: `POST`
Request Body: `form`
Parameters:
`current_user_id`: user id of the user who performed the dislike
`disliked_user_id`: user id of the user who got disliked

Sample request:
```
POST: http://127.0.0.1:5000/dislike
form: {
    current_user_id: 'amxiXfkMy7cExPDh8ju1JfQ76MJ3',
    disliked_user_id: '4bEurIdXSBVng0zpWB9GcDzgKks1'
}
```
> In this case, `current_user_id` is "Priyanka Shah" and `disliked_user_id` is "Jake Ballmer"

Sample Response:
```
{
    "code": 15,
    "message": "Action successfully processed"
}
```

## `/dislikes`
This endpoint can be used to get a list of users that a given user has disliked.
Request Type: `GET`
Request Body: `form`
Parameters:
`user_id`: user id of the user whose dislikes to fetch

Sample request:
```
GET: http://127.0.0.1:5000/dislikes
form: {
    user_id: 'amxiXfkMy7cExPDh8ju1JfQ76MJ3',
}
```
> In this case, `user_id` is "Priyanka Shah"

Sample Response:
```
[
    {
        "age": 19,
        "bio": "Junior at Harvard, favorite activity is scuba diving",
        "email": "jake@gmail.com",
        "name": "Jake Ballmer",
        "sex": "M",
        "user_id": "4bEurIdXSBVng0zpWB9GcDzgKks1"
    }
]
```
## `/dislikedby`
This endpoint can be used to get a list of users who have disliked a given user.
Request Type: `GET`
Request Body: `form`
Parameters:
`user_id`: user id of the user whose dislikers to fetch

Sample request:
```
GET: http://127.0.0.1:5000/dislikedby
form: {
    user_id: 'Bp75dPhTmWWs88MxHQS2rNlqg9p2',
}
```
> In this case, `user_id` is "Jake Ballmer"

Sample Response:
```
[
    {
        "age": 21,
        "bio": "Pursuing business at Yale, SRK fan",
        "email": "priyanka@gmail.com",
        "name": "Priyanka Shah",
        "sex": "F",
        "user_id": "amxiXfkMy7cExPDh8ju1JfQ76MJ3"
    }
]
```

## Matches

## `/matches`
This endpoint can be used to get a list of users who have been matched with the given user.
Request Type: `GET`
Request Body: `form`
Parameters:
`user_id`: user id of the user whose matches to fetch

Sample request:
```
GET: http://127.0.0.1:5000/matches
form: {
    user_id: 'rYNHp81zOwOIzFwPniXBZ6RR1qy13',
}
```
> In this case, `user_id` is "Parth Shah"

Sample Response:
```
[
    {
        "age": 21,
        "bio": "I love art",
        "email": "mary.jane@gmail.com",
        "name": "Mary Jane",
        "sex": "F",
        "user_id": "DxJEk5NAFufZYpH7jXjPTtpzV3r1"
    }
]
```

## `/potential_matches`
This endpoint can be used to get a list of users who could be potential matches for the given user.
Request Type: `GET`
Request Body: `form`
Parameters:
`user_id`: user id of the user whose potential matches to fetch

Sample request:
```
GET: http://127.0.0.1:5000/potential_matches
form: {
    user_id: '6fiAmbryEaRRFdjfeK8h1tnFj9m1',
}
```
> In this case, `user_id` is "Emily Davidson"

Sample Response:
```
[
    {
        "age": 24,
        "bio": "I love sports, and iOS dev, Ex Intern @Box",
        "email": "satish@gmail.com",
        "name": "Satish Boggarapu",
        "sex": "M",
        "user_id": "otnRgXkDbhQ7SmWesMIBpajfD7d2"
    },
    {
        "age": 26,
        "bio": "Senior @ Dxrexel, Philly, Android, UI, Graphics",
        "email": "michael@gmail.com",
        "name": "Michael DiCioccio",
        "sex": "M",
        "user_id": "HuHRWFGH8yaHm8pOVqjspPtKD4g1"
    },
    {
        "age": 30,
        "bio": "Actor, Chef, Runner #marvel fan",
        "email": "rohit@gmail.com",
        "name": "Rohit Sharma",
        "sex": "M",
        "user_id": "x7jnlNxtVff4ZVKv4gGcy4Ffqzz1"
    }
]
```

# Updating User Profile

## `/user/update/name`
This endpoint can be used to update a user's name.

Request Type: `POST`
Request Body: `form`
Parameters:
`user_id`: user id of the user whose name needs to be updated
`new_name`: new name of the user

Sample request:
```
POST: http://127.0.0.1:5000/user/update/name
form: {
    user_id: 'rYNHp81zOwOIzFwPniXBZ6RR1qy1',
    new_name: 'Parth Bhoiwala'
}
```
> In this case, `user_id` is "Parth Shah"


## `/user/update/bio`
This endpoint can be used to update a user's bio.

Request Type: `POST`
Request Body: `form`
Parameters:
`user_id`: user id of the user whose bio needs to be updated
`new_bio`: new bio of the user

Sample request:
```
POST: http://127.0.0.1:5000/user/update/bio
form: {
    user_id: 'rYNHp81zOwOIzFwPniXBZ6RR1qy1',
    new_bio: 'Android dev, I love coffee and biking, #cricket fan'
}
```
> In this case, `user_id` is "Parth Bhoiwala"


## `/user/update/age`
This endpoint can be used to update a user's age.

Request Type: `POST`
Request Body: `form`
Parameters:
`user_id`: user id of the user whose age needs to be updated
`new_age`: new age of the user

Sample request:
```
POST: http://127.0.0.1:5000/user/update/bio
form: {
    user_id: '9fmBjsJWuOWA2eS242hEOnXwkEt1',
    new_age: 32
}
```
> In this case, `user_id` is "Amanda Johnson"

#### Sample Response for the above endpoints:
```
{
    "code": 16,
    "message": "Update request successfully processed"
}
```
# Errors and Exceptions
Below are the error code and their corresponding messages that will be returned in case of invalid API request.


| Name | Code | Message  |
| ---- | ---- | ---- |
| MISSING_ATTR_USER_ID | 1| Missing attribute in request form. `user_id` must be passed in using form in the request|
| MISSING_ATTR_USER_ID_LIKE | 2| Missing attributes in request form. `current_user_id` and `liked_user_id` must be passed in using form in the request|
| MISSING_ATTR_USER_ID_DISLIKE | 3| Missing attributes in request form. `current_user_id` and `disliked_user_id` must be passed in using form in the request|
| MISSING_ATTR_AUTH | 4| Missing attributes in request form. `email` and `password` must be passed in using form in the request|
| MISSING_ATTR_GET_USER | 5| Missing attributes in request form. `email` or `user_id` must be passed in as the request parameters|
| EMAIL_NOT_FOUND | 6| User with the given email does not exist in the database|
| USER_ID_NOT_FOUND | 7| User with the given id does not exist in the database|
| NO_LIKES | 8|User has no likes|
| NO_DISLIKES | 9| User has no dislikes|
| NO_MATCHES | 10| User has no matches|
| NO_POTENTIAL_MATCHES | 11| No potential matches found for user|
| MISSING_ATTR_NEW_NAME | 12| Missing attributes in request form. `new_name` must be passed in using form in the request|
| MISSING_ATTR_NEW_AGE | 13| Missing attributes in request form. `new_age` must be passed in using form in the request|
| MISSING_ATTR_NEW_BIO | 14| Missing attributes in request form. `new_bio` must be passed in using form in the request|


