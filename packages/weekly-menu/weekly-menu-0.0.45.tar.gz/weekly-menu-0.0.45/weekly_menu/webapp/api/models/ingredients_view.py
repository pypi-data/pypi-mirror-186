from .. import mongo

from .base_document import BaseDocument


class IngredientView(mongo.Document):
    owner = mongo.ReferenceField('User', required=True)
    name = mongo.StringField(required=True)
    source = mongo.StringField(required=True)

    meta = {
        'collection': 'ingredients_view'
    }

    def __repr__(self):
        return "<IngredientView'{}'>".format(self.name)
