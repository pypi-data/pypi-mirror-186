import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class ModifierButtonsPanel:
    bl_context = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_space_type = None
    ''' '''


class DATA_PT_modifiers(ModifierButtonsPanel, bpy_types.Panel,
                        bpy_types._GenericUI):
    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
    ''' '''

    def ARMATURE(self, layout, ob, md):
        ''' 

        '''
        pass

    def ARRAY(self, layout, ob, md):
        ''' 

        '''
        pass

    def BEVEL(self, layout, ob, md):
        ''' 

        '''
        pass

    def BOOLEAN(self, layout, ob, md):
        ''' 

        '''
        pass

    def BUILD(self, layout, ob, md):
        ''' 

        '''
        pass

    def CAST(self, layout, ob, md):
        ''' 

        '''
        pass

    def CLOTH(self, layout, ob, md):
        ''' 

        '''
        pass

    def COLLISION(self, layout, ob, md):
        ''' 

        '''
        pass

    def CORRECTIVE_SMOOTH(self, layout, ob, md):
        ''' 

        '''
        pass

    def CURVE(self, layout, ob, md):
        ''' 

        '''
        pass

    def DATA_TRANSFER(self, layout, ob, md):
        ''' 

        '''
        pass

    def DECIMATE(self, layout, ob, md):
        ''' 

        '''
        pass

    def DISPLACE(self, layout, ob, md):
        ''' 

        '''
        pass

    def DYNAMIC_PAINT(self, layout, ob, md):
        ''' 

        '''
        pass

    def EDGE_SPLIT(self, layout, ob, md):
        ''' 

        '''
        pass

    def EXPLODE(self, layout, ob, md):
        ''' 

        '''
        pass

    def FLUID_SIMULATION(self, layout, ob, md):
        ''' 

        '''
        pass

    def HOOK(self, layout, ob, md):
        ''' 

        '''
        pass

    def LAPLACIANDEFORM(self, layout, ob, md):
        ''' 

        '''
        pass

    def LAPLACIANSMOOTH(self, layout, ob, md):
        ''' 

        '''
        pass

    def LATTICE(self, layout, ob, md):
        ''' 

        '''
        pass

    def MASK(self, layout, ob, md):
        ''' 

        '''
        pass

    def MESH_CACHE(self, layout, ob, md):
        ''' 

        '''
        pass

    def MESH_DEFORM(self, layout, ob, md):
        ''' 

        '''
        pass

    def MESH_SEQUENCE_CACHE(self, layout, ob, md):
        ''' 

        '''
        pass

    def MIRROR(self, layout, ob, md):
        ''' 

        '''
        pass

    def MULTIRES(self, layout, ob, md):
        ''' 

        '''
        pass

    def NORMAL_EDIT(self, layout, ob, md):
        ''' 

        '''
        pass

    def OCEAN(self, layout, ob, md):
        ''' 

        '''
        pass

    def PARTICLE_INSTANCE(self, layout, ob, md):
        ''' 

        '''
        pass

    def PARTICLE_SYSTEM(self, layout, ob, md):
        ''' 

        '''
        pass

    def REMESH(self, layout, ob, md):
        ''' 

        '''
        pass

    def SCREW(self, layout, ob, md):
        ''' 

        '''
        pass

    def SHRINKWRAP(self, layout, ob, md):
        ''' 

        '''
        pass

    def SIMPLE_DEFORM(self, layout, ob, md):
        ''' 

        '''
        pass

    def SKIN(self, layout, ob, md):
        ''' 

        '''
        pass

    def SMOKE(self, layout, ob, md):
        ''' 

        '''
        pass

    def SMOOTH(self, layout, ob, md):
        ''' 

        '''
        pass

    def SOFT_BODY(self, layout, ob, md):
        ''' 

        '''
        pass

    def SOLIDIFY(self, layout, ob, md):
        ''' 

        '''
        pass

    def SUBSURF(self, layout, ob, md):
        ''' 

        '''
        pass

    def SURFACE(self, layout, ob, md):
        ''' 

        '''
        pass

    def SURFACE_DEFORM(self, layout, ob, md):
        ''' 

        '''
        pass

    def TRIANGULATE(self, layout, ob, md):
        ''' 

        '''
        pass

    def UV_PROJECT(self, layout, ob, md):
        ''' 

        '''
        pass

    def UV_WARP(self, layout, ob, md):
        ''' 

        '''
        pass

    def VERTEX_WEIGHT_EDIT(self, layout, ob, md):
        ''' 

        '''
        pass

    def VERTEX_WEIGHT_MIX(self, layout, ob, md):
        ''' 

        '''
        pass

    def VERTEX_WEIGHT_PROXIMITY(self, layout, ob, md):
        ''' 

        '''
        pass

    def WARP(self, layout, ob, md):
        ''' 

        '''
        pass

    def WAVE(self, layout, ob, md):
        ''' 

        '''
        pass

    def WIREFRAME(self, layout, ob, md):
        ''' 

        '''
        pass

    def append(self, draw_func):
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

    def get(self):
        ''' 

        '''
        pass

    def is_extended(self):
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

    def prepend(self, draw_func):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def remove(self, draw_func):
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

    def vertex_weight_mask(self, layout, ob, md):
        ''' 

        '''
        pass
