import sys
import typing

GenericType = typing.TypeVar("GenericType")


class MotionPathButtonsPanel:
    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_space_type = None
    ''' '''

    def draw_settings(self, context, avs, mpath, bones):
        ''' 

        '''
        pass


class OnionSkinButtonsPanel:
    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_space_type = None
    ''' '''

    def draw(self, context):
        ''' 

        '''
        pass
