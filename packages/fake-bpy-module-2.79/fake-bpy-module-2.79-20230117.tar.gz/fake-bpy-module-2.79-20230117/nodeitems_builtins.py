import sys
import typing
import nodeitems_utils

GenericType = typing.TypeVar("GenericType")


class SortedNodeCategory(nodeitems_utils.NodeCategory):
    def poll(self, context):
        ''' 

        '''
        pass


class CompositorNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        ''' 

        '''
        pass


class ShaderNewNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        ''' 

        '''
        pass


class ShaderOldNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        ''' 

        '''
        pass


class TextureNodeCategory(SortedNodeCategory, nodeitems_utils.NodeCategory):
    def poll(self, context):
        ''' 

        '''
        pass


def group_input_output_item_poll(context):
    ''' 

    '''

    pass


def group_tools_draw(layout, context):
    ''' 

    '''

    pass


def line_style_shader_nodes_poll(context):
    ''' 

    '''

    pass


def node_group_items(context):
    ''' 

    '''

    pass


def object_shader_nodes_poll(context):
    ''' 

    '''

    pass


def register():
    ''' 

    '''

    pass


def unregister():
    ''' 

    '''

    pass


def world_shader_nodes_poll(context):
    ''' 

    '''

    pass
