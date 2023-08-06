import sys
import typing

GenericType = typing.TypeVar("GenericType")


class PropertyPanel:
    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    def draw(self, context):
        ''' 

        '''
        pass

    def poll(self, context):
        ''' 

        '''
        pass


def draw(layout, context, context_member, property_type, use_edit):
    ''' 

    '''

    pass


def rna_idprop_context_value(context, context_member, property_type):
    ''' 

    '''

    pass


def rna_idprop_has_properties(rna_item):
    ''' 

    '''

    pass


def rna_idprop_ui_del(item):
    ''' 

    '''

    pass


def rna_idprop_ui_get(item, create):
    ''' 

    '''

    pass


def rna_idprop_ui_prop_clear(item, prop, remove):
    ''' 

    '''

    pass


def rna_idprop_ui_prop_get(item, prop, create):
    ''' 

    '''

    pass


def rna_idprop_ui_prop_update(item, prop):
    ''' 

    '''

    pass
