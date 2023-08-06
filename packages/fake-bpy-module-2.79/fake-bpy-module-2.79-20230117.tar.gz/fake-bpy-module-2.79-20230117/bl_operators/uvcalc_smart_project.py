import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class SmartProject(bpy_types.Operator):
    angle_limit = None
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

    island_margin = None
    ''' '''

    order = None
    ''' '''

    stretch_to_bounds = None
    ''' '''

    use_aspect = None
    ''' '''

    user_area_weight = None
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


class thickface:
    pass


def VectoQuat(vec):
    ''' 

    '''

    pass


def boundsIsland(faces):
    ''' 

    '''

    pass


def getUvIslands(faceGroups, me):
    ''' 

    '''

    pass


def island2Edge(island):
    ''' 

    '''

    pass


def islandIntersectUvIsland(source, target, SourceOffset):
    ''' 

    '''

    pass


def main(context, island_margin, projection_limit, user_area_weight,
         use_aspect, stretch_to_bounds):
    ''' 

    '''

    pass


def main_consts():
    ''' 

    '''

    pass


def mergeUvIslands(islandList):
    ''' 

    '''

    pass


def optiRotateUvIsland(faces):
    ''' 

    '''

    pass


def packIslands(islandList):
    ''' 

    '''

    pass


def pointInIsland(pt, island):
    ''' 

    '''

    pass


def pointInTri2D(v, v1, v2, v3):
    ''' 

    '''

    pass


def rotate_uvs(uv_points, angle):
    ''' 

    '''

    pass
