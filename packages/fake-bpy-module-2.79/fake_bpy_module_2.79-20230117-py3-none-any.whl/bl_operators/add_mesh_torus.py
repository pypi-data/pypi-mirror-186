import sys
import typing
import bpy_types
import bpy_extras.object_utils

GenericType = typing.TypeVar("GenericType")


class AddTorus(bpy_types.Operator, bpy_extras.object_utils.AddObjectHelper):
    abso_major_rad = None
    ''' '''

    abso_minor_rad = None
    ''' '''

    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    generate_uvs = None
    ''' '''

    id_data = None
    ''' '''

    layers = None
    ''' '''

    location = None
    ''' '''

    major_radius = None
    ''' '''

    major_segments = None
    ''' '''

    minor_radius = None
    ''' '''

    minor_segments = None
    ''' '''

    mode = None
    ''' '''

    order = None
    ''' '''

    rotation = None
    ''' '''

    view_align = None
    ''' '''

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def draw(self, context):
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

    def mode_update_callback(self, context):
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

    def poll(self, context):
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

    def view_align_update_callback(self, context):
        ''' 

        '''
        pass


def add_torus(major_rad, minor_rad, major_seg, minor_seg):
    ''' 

    '''

    pass


def add_uvs(mesh, minor_seg, major_seg):
    ''' 

    '''

    pass
