from .. import BASE_PATH


def create_module(app, api):

    from .resources import IngredientsViewList

    api.add_resource(
        IngredientsViewList,
        BASE_PATH + '/ingredients-view'
    )
