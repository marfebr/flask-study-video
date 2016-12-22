from flask_restful import reqparse

token_parser = reqparse.RequestParser()

token_parser.add_argument(
    'token',
    type=str,
    required=True,
    help="Token is requered")



user_auth_post_parser = reqparse.RequestParser()

user_auth_post_parser.add_argument(
    'username',
    type=str,
    required=True,
    help='Username is required'
)

user_auth_post_parser.add_argument(
    'password',
    type=str,
    required=True,
    help='Password id required'
)


movie_post_parser = token_parser.copy()


movie_post_parser.add_argument(
    'name',
    type=str,
    required=True,
    help="Movie name is Required"
)

movie_post_parser.add_argument(
    'release_date',
    type=str,
    required=True,
    help="Release date is Required"
)

movie_post_parser.add_argument(
    'summary',
    type=str,
    required=True,
    help="Summary is Required"
)

movie_post_parser.add_argument(
    'director_id',
    type=int,
    required=True
    )


movie_put_parser = token_parser.copy()

movie_put_parser.add_argument(
    'name',
    type=str,
    help="Movie name is Required"
)

movie_put_parser.add_argument(
    'release_date',
    type=str,
    help="Release date is Required"
)

movie_put_parser.add_argument(
    'summary',
    type=str,
    help="Summary is Required"
)

movie_put_parser.add_argument(
    'director_id',
    type=int
    )

actor_post_parser = token_parser.copy()

actor_post_parser.add_argument(
    'first_name',
    type=str,
    required=True,
    help='First Name is required'
)

actor_post_parser.add_argument(
    'last_name',
    type=str,
    required=True,
    help='last_name is required'
)
actor_post_parser.add_argument(
    'birthday',
    type=str,
    required=True,
    help='birthday is required'
)
actor_post_parser.add_argument(
    'deathday',
    type=str
    
)
actor_post_parser.add_argument(
    'hometown',
    type=str
)

actor_post_parser.add_argument(
    'bio',
    type=str
)

actor_put_parser = token_parser.copy()

actor_put_parser.add_argument(
    'first_name',
    type=str
)

actor_put_parser.add_argument(
    'last_name',
    type=str
    
)
actor_put_parser.add_argument(
    'birthday',
    type=str
    
)
actor_put_parser.add_argument(
    'deathday',
    type=str
    
)
actor_put_parser.add_argument(
    'hometown',
    type=str
)

actor_put_parser.add_argument(
    'bio',
    type=str
)

