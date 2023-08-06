import sys
import typing

GenericType = typing.TypeVar("GenericType")


class NodeCategory:
    def poll(self, context):
        ''' 

        '''
        pass


class NodeItem:
    label = None
    ''' '''

    def draw(self, layout, context):
        ''' 

        '''
        pass


class NodeItemCustom:
    pass


def draw_node_categories_menu(context):
    ''' 

    '''

    pass


def node_categories_iter(context):
    ''' 

    '''

    pass


def node_items_iter(context):
    ''' 

    '''

    pass


def register_node_categories(identifier, cat_list):
    ''' 

    '''

    pass


def unregister_node_cat_types(cats):
    ''' 

    '''

    pass


def unregister_node_categories(identifier):
    ''' 

    '''

    pass
