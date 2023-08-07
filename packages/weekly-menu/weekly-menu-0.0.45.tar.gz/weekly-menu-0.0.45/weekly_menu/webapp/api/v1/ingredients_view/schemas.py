import marshmallow_mongoengine as me

from marshmallow import Schema, fields

from ... import mongo
from ...models import IngredientView


class IngredientViewSchema(me.ModelSchema):

    class Meta:
        model = IngredientView
