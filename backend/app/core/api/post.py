from flask_restx import fields

from app import rest_api


post_book = rest_api.model(
    "Books", {
        "name": fields.String(description='Name of book', required=True),
        "category": fields.String(description='Category of book', required=True),
        "author": fields.String(description='Author of book', required=False),
    }
)
