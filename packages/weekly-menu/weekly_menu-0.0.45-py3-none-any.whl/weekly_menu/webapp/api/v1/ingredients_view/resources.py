import pprint

from flask import jsonify
from flask_restful import Resource, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine.errors import NotUniqueError
from mongoengine.fields import ObjectIdField
from mongoengine.queryset.visitor import Q

from ..ingredients_view.schemas import IngredientViewSchema
from ...models import IngredientView, User
from ... import validate_payload, get_payload, paginated, parse_query_args, mongo, load_user_info, put_document, patch_document, search_on_model
from ...exceptions import DuplicateEntry, BadRequest, Forbidden


class IngredientsViewList(Resource):
    @jwt_required
    @parse_query_args
    @paginated
    @load_user_info
    def get(self, query_args, page_args, user_info: User):
        return search_on_model(IngredientView, Q(owner=str(user_info.id)), query_args, page_args)
