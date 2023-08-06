import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class LightMapPack(bpy_types.Operator):
    PREF_APPLY_IMAGE = None
    ''' '''

    PREF_BOX_DIV = None
    ''' '''

    PREF_CONTEXT = None
    ''' '''

    PREF_IMG_PX_SIZE = None
    ''' '''

    PREF_MARGIN_DIV = None
    ''' '''

    PREF_NEW_UVLAYER = None
    ''' '''

    PREF_PACK_IN_ONE = None
    ''' '''

    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    order = None
    ''' '''

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class prettyface:
    children = None
    ''' '''

    has_parent = None
    ''' '''

    height = None
    ''' '''

    rot = None
    ''' '''

    uv = None
    ''' '''

    width = None
    ''' '''

    xoff = None
    ''' '''

    yoff = None
    ''' '''

    def place(self, xoff, yoff, xfac, yfac, margin_w, margin_h):
        ''' 

        '''
        pass

    def spin(self):
        ''' 

        '''
        pass


def lightmap_uvpack(meshes, PREF_SEL_ONLY, PREF_NEW_UVLAYER, PREF_PACK_IN_ONE,
                    PREF_APPLY_IMAGE, PREF_IMG_PX_SIZE, PREF_BOX_DIV,
                    PREF_MARGIN_DIV):
    ''' 

    '''

    pass


def unwrap(operator, context, kwargs):
    ''' 

    '''

    pass
