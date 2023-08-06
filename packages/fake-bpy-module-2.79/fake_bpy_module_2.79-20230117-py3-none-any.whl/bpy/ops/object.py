import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def add(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        type: typing.Optional[typing.Any] = 'EMPTY',
        view_align: typing.Union[bool, typing.Any] = False,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add an object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def add_named(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              linked: typing.Union[bool, typing.Any] = False,
              name: typing.Union[str, typing.Any] = ""):
    ''' Add named object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: typing.Union[bool, typing.Any]
    :param name: Name, Object name to add
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def align(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: typing.Optional[bool] = None,
          *,
          bb_quality: typing.Union[bool, typing.Any] = True,
          align_mode: typing.Optional[typing.Any] = 'OPT_2',
          relative_to: typing.Optional[typing.Any] = 'OPT_4',
          align_axis: typing.Optional[typing.Any] = {}):
    ''' Align Objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param bb_quality: High Quality, Enables high quality calculation of the bounding box for perfect results on complex shape meshes with rotation/scale (Slow)
    :type bb_quality: typing.Union[bool, typing.Any]
    :param align_mode: Align Mode:, Side of object to use for alignment
    :type align_mode: typing.Optional[typing.Any]
    :param relative_to: Relative To:, Reference location to align to * ``OPT_1`` Scene Origin, Use the Scene Origin as the position for the selected objects to align to. * ``OPT_2`` 3D Cursor, Use the 3D cursor as the position for the selected objects to align to. * ``OPT_3`` Selection, Use the selected objects as the position for the selected objects to align to. * ``OPT_4`` Active, Use the active object as the position for the selected objects to align to.
    :type relative_to: typing.Optional[typing.Any]
    :param align_axis: Align, Align to axis
    :type align_axis: typing.Optional[typing.Any]
    '''

    pass


def anim_transforms_to_deltas(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: typing.Optional[bool] = None):
    ''' Convert object animation for normal transforms to delta transforms :file: `startup/bl_operators/object.py\:784 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/object.py$784>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def armature_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        view_align: typing.Union[bool, typing.Any] = False,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add an armature object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def bake(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         type: typing.Optional[typing.Any] = 'COMBINED',
         pass_filter: typing.Optional[typing.Any] = {},
         filepath: typing.Union[str, typing.Any] = "",
         width: typing.Optional[typing.Any] = 512,
         height: typing.Optional[typing.Any] = 512,
         margin: typing.Optional[typing.Any] = 16,
         use_selected_to_active: typing.Union[bool, typing.Any] = False,
         cage_extrusion: typing.Optional[typing.Any] = 0.0,
         cage_object: typing.Union[str, typing.Any] = "",
         normal_space: typing.Optional[typing.Any] = 'TANGENT',
         normal_r: typing.Optional[typing.Any] = 'POS_X',
         normal_g: typing.Optional[typing.Any] = 'POS_Y',
         normal_b: typing.Optional[typing.Any] = 'POS_Z',
         save_mode: typing.Optional[typing.Any] = 'INTERNAL',
         use_clear: typing.Union[bool, typing.Any] = False,
         use_cage: typing.Union[bool, typing.Any] = False,
         use_split_materials: typing.Union[bool, typing.Any] = False,
         use_automatic_name: typing.Union[bool, typing.Any] = False,
         uv_layer: typing.Union[str, typing.Any] = ""):
    ''' Bake image textures of selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine
    :type type: typing.Optional[typing.Any]
    :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes
    :type pass_filter: typing.Optional[typing.Any]
    :param filepath: File Path, Image filepath to use when saving externally
    :type filepath: typing.Union[str, typing.Any]
    :param width: Width, Horizontal dimension of the baking map (external only)
    :type width: typing.Optional[typing.Any]
    :param height: Height, Vertical dimension of the baking map (external only)
    :type height: typing.Optional[typing.Any]
    :param margin: Margin, Extends the baked result as a post process filter
    :type margin: typing.Optional[typing.Any]
    :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object
    :type use_selected_to_active: typing.Union[bool, typing.Any]
    :param cage_extrusion: Cage Extrusion, Distance to use for the inward ray cast when using selected to active
    :type cage_extrusion: typing.Optional[typing.Any]
    :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion
    :type cage_object: typing.Union[str, typing.Any]
    :param normal_space: Normal Space, Choose normal space for baking * ``OBJECT`` Object, Bake the normals in object space. * ``TANGENT`` Tangent, Bake the normals in tangent space.
    :type normal_space: typing.Optional[typing.Any]
    :param normal_r: R, Axis to bake in red channel
    :type normal_r: typing.Optional[typing.Any]
    :param normal_g: G, Axis to bake in green channel
    :type normal_g: typing.Optional[typing.Any]
    :param normal_b: B, Axis to bake in blue channel
    :type normal_b: typing.Optional[typing.Any]
    :param save_mode: Save Mode, Choose how to save the baking map * ``INTERNAL`` Internal, Save the baking map in an internal image data-block. * ``EXTERNAL`` External, Save the baking map in an external file.
    :type save_mode: typing.Optional[typing.Any]
    :param use_clear: Clear, Clear Images before baking (only for internal saving)
    :type use_clear: typing.Union[bool, typing.Any]
    :param use_cage: Cage, Cast rays to active object from a cage
    :type use_cage: typing.Union[bool, typing.Any]
    :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only)
    :type use_split_materials: typing.Union[bool, typing.Any]
    :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type
    :type use_automatic_name: typing.Union[bool, typing.Any]
    :param uv_layer: UV Layer, UV layer to override active
    :type uv_layer: typing.Union[str, typing.Any]
    '''

    pass


def bake_image(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Bake image textures of selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def camera_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        view_align: typing.Union[bool, typing.Any] = False,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add a camera object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def constraint_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   type: typing.Optional[typing.Any] = ''):
    ''' Add a constraint to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CAMERA_SOLVER`` Camera Solver. * ``FOLLOW_TRACK`` Follow Track. * ``OBJECT_SOLVER`` Object Solver. * ``COPY_LOCATION`` Copy Location, Copy the location of a target (with an optional offset), so that they move together. * ``COPY_ROTATION`` Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together. * ``COPY_SCALE`` Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount. * ``COPY_TRANSFORMS`` Copy Transforms, Copy all the transformations of a target, so that they move together. * ``LIMIT_DISTANCE`` Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only). * ``LIMIT_LOCATION`` Limit Location, Restrict movement along each axis within given ranges. * ``LIMIT_ROTATION`` Limit Rotation, Restrict rotation along each axis within given ranges. * ``LIMIT_SCALE`` Limit Scale, Restrict scaling along each axis with given ranges. * ``MAINTAIN_VOLUME`` Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes. * ``TRANSFORM`` Transformation, Use one transform property from target to control another (or same) property on owner. * ``TRANSFORM_CACHE`` Transform Cache, Look up the transformation matrix from an external file. * ``CLAMP_TO`` Clamp To, Restrict movements to lie along a curve by remapping location along curve's longest axis. * ``DAMPED_TRACK`` Damped Track, Point towards a target by performing the smallest rotation necessary. * ``IK`` Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only). * ``LOCKED_TRACK`` Locked Track, Rotate around the specified ('locked') axis to point towards a target. * ``SPLINE_IK`` Spline IK, Align chain of bones along a curve (Bones only). * ``STRETCH_TO`` Stretch To, Stretch along Y-Axis to point towards a target. * ``TRACK_TO`` Track To, Legacy tracking constraint prone to twisting artifacts. * ``ACTION`` Action, Use transform property of target to look up pose for owner from an Action. * ``CHILD_OF`` Child Of, Make target the 'detachable' parent of owner. * ``FLOOR`` Floor, Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross. * ``FOLLOW_PATH`` Follow Path, Use to animate an object/bone following a path. * ``PIVOT`` Pivot, Change pivot point for transforms (buggy). * ``RIGID_BODY_JOINT`` Rigid Body Joint, Use to define a Rigid Body Constraint (for Game Engine use only). * ``SHRINKWRAP`` Shrinkwrap, Restrict movements to surface of target mesh.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def constraint_add_with_targets(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = ''):
    ''' Add a constraint to the active object, with target (where applicable) set to the selected Objects/Bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CAMERA_SOLVER`` Camera Solver. * ``FOLLOW_TRACK`` Follow Track. * ``OBJECT_SOLVER`` Object Solver. * ``COPY_LOCATION`` Copy Location, Copy the location of a target (with an optional offset), so that they move together. * ``COPY_ROTATION`` Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together. * ``COPY_SCALE`` Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount. * ``COPY_TRANSFORMS`` Copy Transforms, Copy all the transformations of a target, so that they move together. * ``LIMIT_DISTANCE`` Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only). * ``LIMIT_LOCATION`` Limit Location, Restrict movement along each axis within given ranges. * ``LIMIT_ROTATION`` Limit Rotation, Restrict rotation along each axis within given ranges. * ``LIMIT_SCALE`` Limit Scale, Restrict scaling along each axis with given ranges. * ``MAINTAIN_VOLUME`` Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes. * ``TRANSFORM`` Transformation, Use one transform property from target to control another (or same) property on owner. * ``TRANSFORM_CACHE`` Transform Cache, Look up the transformation matrix from an external file. * ``CLAMP_TO`` Clamp To, Restrict movements to lie along a curve by remapping location along curve's longest axis. * ``DAMPED_TRACK`` Damped Track, Point towards a target by performing the smallest rotation necessary. * ``IK`` Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only). * ``LOCKED_TRACK`` Locked Track, Rotate around the specified ('locked') axis to point towards a target. * ``SPLINE_IK`` Spline IK, Align chain of bones along a curve (Bones only). * ``STRETCH_TO`` Stretch To, Stretch along Y-Axis to point towards a target. * ``TRACK_TO`` Track To, Legacy tracking constraint prone to twisting artifacts. * ``ACTION`` Action, Use transform property of target to look up pose for owner from an Action. * ``CHILD_OF`` Child Of, Make target the 'detachable' parent of owner. * ``FLOOR`` Floor, Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross. * ``FOLLOW_PATH`` Follow Path, Use to animate an object/bone following a path. * ``PIVOT`` Pivot, Change pivot point for transforms (buggy). * ``RIGID_BODY_JOINT`` Rigid Body Joint, Use to define a Rigid Body Constraint (for Game Engine use only). * ``SHRINKWRAP`` Shrinkwrap, Restrict movements to surface of target mesh.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def constraints_clear(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Clear all the constraints for the active Object only

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def constraints_copy(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Copy constraints to other selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def convert(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: typing.Optional[bool] = None,
            *,
            target: typing.Optional[typing.Any] = 'MESH',
            keep_original: typing.Union[bool, typing.Any] = False):
    ''' Convert selected objects to another type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param target: Target, Type of object to convert to
    :type target: typing.Optional[typing.Any]
    :param keep_original: Keep Original, Keep original objects instead of replacing them
    :type keep_original: typing.Union[bool, typing.Any]
    '''

    pass


def correctivesmooth_bind(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None,
                          *,
                          modifier: typing.Union[str, typing.Any] = ""):
    ''' Bind base pose in Corrective Smooth modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def data_transfer(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_reverse_transfer: typing.Union[bool, typing.Any] = False,
        use_freeze: typing.Union[bool, typing.Any] = False,
        data_type: typing.Optional[typing.Any] = '',
        use_create: typing.Union[bool, typing.Any] = True,
        vert_mapping: typing.Optional[typing.Any] = 'NEAREST',
        edge_mapping: typing.Optional[typing.Any] = 'NEAREST',
        loop_mapping: typing.Optional[typing.Any] = 'NEAREST_POLYNOR',
        poly_mapping: typing.Optional[typing.Any] = 'NEAREST',
        use_auto_transform: typing.Union[bool, typing.Any] = False,
        use_object_transform: typing.Union[bool, typing.Any] = True,
        use_max_distance: typing.Union[bool, typing.Any] = False,
        max_distance: typing.Optional[typing.Any] = 1.0,
        ray_radius: typing.Optional[typing.Any] = 0.0,
        islands_precision: typing.Optional[typing.Any] = 0.1,
        layers_select_src: typing.Optional[typing.Any] = 'ACTIVE',
        layers_select_dst: typing.Optional[typing.Any] = 'ACTIVE',
        mix_mode: typing.Optional[typing.Any] = 'REPLACE',
        mix_factor: typing.Optional[typing.Any] = 1.0):
    ''' Transfer data layer(s) (weights, edge sharp, ...) from active to selected meshes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one
    :type use_reverse_transfer: typing.Union[bool, typing.Any]
    :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry
    :type use_freeze: typing.Union[bool, typing.Any]
    :param data_type: Data Type, Which data to transfer * ``VGROUP_WEIGHTS`` Vertex Group(s), Transfer active or all vertex groups. * ``BEVEL_WEIGHT_VERT`` Bevel Weight, Transfer bevel weights. * ``SHARP_EDGE`` Sharp, Transfer sharp mark. * ``SEAM`` UV Seam, Transfer UV seam mark. * ``CREASE`` Subsurf Crease, Transfer crease values. * ``BEVEL_WEIGHT_EDGE`` Bevel Weight, Transfer bevel weights. * ``FREESTYLE_EDGE`` Freestyle Mark, Transfer Freestyle edge mark. * ``CUSTOM_NORMAL`` Custom Normals, Transfer custom normals. * ``VCOL`` VCol, Vertex (face corners) colors. * ``UV`` UVs, Transfer UV layers. * ``SMOOTH`` Smooth, Transfer flat/smooth mark. * ``FREESTYLE_FACE`` Freestyle Mark, Transfer Freestyle face mark.
    :type data_type: typing.Optional[typing.Any]
    :param use_create: Create Data, Add data layers on destination meshes if needed
    :type use_create: typing.Union[bool, typing.Any]
    :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones * ``TOPOLOGY`` Topology, Copy from identical topology meshes. * ``NEAREST`` Nearest vertex, Copy from closest vertex. * ``EDGE_NEAREST`` Nearest Edge Vertex, Copy from closest vertex of closest edge. * ``EDGEINTERP_NEAREST`` Nearest Edge Interpolated, Copy from interpolated values of vertices from closest point on closest edge. * ``POLY_NEAREST`` Nearest Face Vertex, Copy from closest vertex of closest face. * ``POLYINTERP_NEAREST`` Nearest Face Interpolated, Copy from interpolated values of vertices from closest point on closest face. * ``POLYINTERP_VNORPROJ`` Projected Face Interpolated, Copy from interpolated values of vertices from point on closest face hit by normal-projection.
    :type vert_mapping: typing.Optional[typing.Any]
    :param edge_mapping: Edge Mapping, Method used to map source edges to destination ones * ``TOPOLOGY`` Topology, Copy from identical topology meshes. * ``VERT_NEAREST`` Nearest Vertices, Copy from most similar edge (edge which vertices are the closest of destination edge's ones). * ``NEAREST`` Nearest Edge, Copy from closest edge (using midpoints). * ``POLY_NEAREST`` Nearest Face Edge, Copy from closest edge of closest face (using midpoints). * ``EDGEINTERP_VNORPROJ`` Projected Edge Interpolated, Interpolate all source edges hit by the projection of destination one along its own normal (from vertices).
    :type edge_mapping: typing.Optional[typing.Any]
    :param loop_mapping: Face Corner Mapping, Method used to map source faces' corners to destination ones * ``TOPOLOGY`` Topology, Copy from identical topology meshes. * ``NEAREST_NORMAL`` Nearest Corner And Best Matching Normal, Copy from nearest corner which has the best matching normal. * ``NEAREST_POLYNOR`` Nearest Corner And Best Matching Face Normal, Copy from nearest corner which has the face with the best matching normal to destination corner's face one. * ``NEAREST_POLY`` Nearest Corner Of Nearest Face, Copy from nearest corner of nearest polygon. * ``POLYINTERP_NEAREST`` Nearest Face Interpolated, Copy from interpolated corners of the nearest source polygon. * ``POLYINTERP_LNORPROJ`` Projected Face Interpolated, Copy from interpolated corners of the source polygon hit by corner normal projection.
    :type loop_mapping: typing.Optional[typing.Any]
    :param poly_mapping: Face Mapping, Method used to map source faces to destination ones * ``TOPOLOGY`` Topology, Copy from identical topology meshes. * ``NEAREST`` Nearest Face, Copy from nearest polygon (using center points). * ``NORMAL`` Best Normal-Matching, Copy from source polygon which normal is the closest to destination one. * ``POLYINTERP_PNORPROJ`` Projected Face Interpolated, Interpolate all source polygons intersected by the projection of destination one along its own normal.
    :type poly_mapping: typing.Optional[typing.Any]
    :param use_auto_transform: Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes (WARNING: results will never be as good as manual matching of objects)
    :type use_auto_transform: typing.Union[bool, typing.Any]
    :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space
    :type use_object_transform: typing.Union[bool, typing.Any]
    :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one
    :type use_max_distance: typing.Union[bool, typing.Any]
    :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings
    :type max_distance: typing.Optional[typing.Any]
    :param ray_radius: Ray Radius, 'Width' of rays (especially useful when raycasting against vertices or edges)
    :type ray_radius: typing.Optional[typing.Any]
    :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)
    :type islands_precision: typing.Optional[typing.Any]
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types * ``ACTIVE`` Active Layer, Only transfer active data layer. * ``ALL`` All Layers, Transfer all data layers. * ``BONE_SELECT`` Selected Pose Bones, Transfer all vertex groups used by selected pose bones. * ``BONE_DEFORM`` Deform Pose Bones, Transfer all vertex groups used by deform bones.
    :type layers_select_src: typing.Optional[typing.Any]
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers * ``ACTIVE`` Active Layer, Affect active data layer of all targets. * ``NAME`` By Name, Match target data layers to affect by name. * ``INDEX`` By Order, Match target data layers to affect by order (indices).
    :type layers_select_dst: typing.Optional[typing.Any]
    :param mix_mode: Mix Mode, How to affect destination elements with source values * ``REPLACE`` Replace, Overwrite all elements' data. * ``ABOVE_THRESHOLD`` Above Threshold, Only replace destination elements where data is above given threshold (exact behavior depends on data type). * ``BELOW_THRESHOLD`` Below Threshold, Only replace destination elements where data is below given threshold (exact behavior depends on data type). * ``MIX`` Mix, Mix source value into destination one, using given threshold as factor. * ``ADD`` Add, Add source value to destination one, using given threshold as factor. * ``SUB`` Subtract, Subtract source value to destination one, using given threshold as factor. * ``MUL`` Multiply, Multiply source value to destination one, using given threshold as factor.
    :type mix_mode: typing.Optional[typing.Any]
    :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)
    :type mix_factor: typing.Optional[typing.Any]
    '''

    pass


def datalayout_transfer(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = "",
        data_type: typing.Optional[typing.Any] = '',
        use_delete: typing.Union[bool, typing.Any] = False,
        layers_select_src: typing.Optional[typing.Any] = 'ACTIVE',
        layers_select_dst: typing.Optional[typing.Any] = 'ACTIVE'):
    ''' Transfer layout of data layer(s) from active to selected meshes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param data_type: Data Type, Which data to transfer * ``VGROUP_WEIGHTS`` Vertex Group(s), Transfer active or all vertex groups. * ``BEVEL_WEIGHT_VERT`` Bevel Weight, Transfer bevel weights. * ``SHARP_EDGE`` Sharp, Transfer sharp mark. * ``SEAM`` UV Seam, Transfer UV seam mark. * ``CREASE`` Subsurf Crease, Transfer crease values. * ``BEVEL_WEIGHT_EDGE`` Bevel Weight, Transfer bevel weights. * ``FREESTYLE_EDGE`` Freestyle Mark, Transfer Freestyle edge mark. * ``CUSTOM_NORMAL`` Custom Normals, Transfer custom normals. * ``VCOL`` VCol, Vertex (face corners) colors. * ``UV`` UVs, Transfer UV layers. * ``SMOOTH`` Smooth, Transfer flat/smooth mark. * ``FREESTYLE_FACE`` Freestyle Mark, Transfer Freestyle face mark.
    :type data_type: typing.Optional[typing.Any]
    :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source
    :type use_delete: typing.Union[bool, typing.Any]
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types * ``ACTIVE`` Active Layer, Only transfer active data layer. * ``ALL`` All Layers, Transfer all data layers. * ``BONE_SELECT`` Selected Pose Bones, Transfer all vertex groups used by selected pose bones. * ``BONE_DEFORM`` Deform Pose Bones, Transfer all vertex groups used by deform bones.
    :type layers_select_src: typing.Optional[typing.Any]
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers * ``ACTIVE`` Active Layer, Affect active data layer of all targets. * ``NAME`` By Name, Match target data layers to affect by name. * ``INDEX`` By Order, Match target data layers to affect by order (indices).
    :type layers_select_dst: typing.Optional[typing.Any]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           use_global: typing.Union[bool, typing.Any] = False):
    ''' Delete selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_global: Delete Globally, Remove object from all scenes
    :type use_global: typing.Union[bool, typing.Any]
    '''

    pass


def drop_named_image(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        relative_path: typing.Union[bool, typing.Any] = True,
        name: typing.Union[str, typing.Any] = "",
        view_align: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add an empty image type to scene with data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: Filepath, Path to image file
    :type filepath: typing.Union[str, typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Union[bool, typing.Any]
    :param name: Name, Image name to assign
    :type name: typing.Union[str, typing.Any]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def drop_named_material(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        name: typing.Union[str, typing.Any] = "Material"):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Material name to assign
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def dupli_offset_from_cursor(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: typing.Optional[bool] = None):
    ''' Set offset used for DupliGroup based on cursor position :file: `startup/bl_operators/object.py\:873 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/object.py$873>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              linked: typing.Union[bool, typing.Any] = False,
              mode: typing.Optional[typing.Any] = 'TRANSLATION'):
    ''' Duplicate selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: typing.Union[bool, typing.Any]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def duplicate_move(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   OBJECT_OT_duplicate: typing.Optional['duplicate'] = None,
                   TRANSFORM_OT_translate: typing.
                   Optional['bpy.ops.transform.translate'] = None):
    ''' Duplicate selected objects and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :type OBJECT_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def duplicate_move_linked(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        OBJECT_OT_duplicate: typing.Optional['duplicate'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Duplicate selected objects and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :type OBJECT_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def duplicates_make_real(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_base_parent: typing.Union[bool, typing.Any] = False,
        use_hierarchy: typing.Union[bool, typing.Any] = False):
    ''' Make dupli objects attached to this object real

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_base_parent: Parent, Parent newly created objects to the original duplicator
    :type use_base_parent: typing.Union[bool, typing.Any]
    :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships
    :type use_hierarchy: typing.Union[bool, typing.Any]
    '''

    pass


def editmode_toggle(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Toggle object's editmode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def effector_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'FORCE',
        radius: typing.Optional[typing.Any] = 1.0,
        view_align: typing.Union[bool, typing.Any] = False,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add an empty object with a physics effector to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def empty_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'PLAIN_AXES',
        radius: typing.Optional[typing.Any] = 1.0,
        view_align: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add an empty object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def explode_refresh(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    modifier: typing.Union[str, typing.Any] = ""):
    ''' Refresh data in the Explode modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def forcefield_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Toggle object's force field

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def game_physics_copy(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Copy game physics properties to other selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def game_property_clear(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Remove all game properties from all selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def game_property_copy(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       operation: typing.Optional[typing.Any] = 'COPY',
                       property: typing.Union[str, int, typing.Any] = ''):
    ''' Copy/merge/replace a game property from active object to all selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param operation: Operation
    :type operation: typing.Optional[typing.Any]
    :param property: Property, Properties to copy
    :type property: typing.Union[str, int, typing.Any]
    '''

    pass


def game_property_move(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       index: typing.Optional[typing.Any] = 0,
                       direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move game property

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param index: Index, Property index to move
    :type index: typing.Optional[typing.Any]
    :param direction: Direction, Direction for moving the property
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def game_property_new(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      type: typing.Optional[typing.Any] = 'FLOAT',
                      name: typing.Union[str, typing.Any] = ""):
    ''' Create a new property available to the game engine

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Type of game property to add * ``BOOL`` Boolean, Boolean Property. * ``INT`` Integer, Integer Property. * ``FLOAT`` Float, Floating-Point Property. * ``STRING`` String, String Property. * ``TIMER`` Timer, Timer Property.
    :type type: typing.Optional[typing.Any]
    :param name: Name, Name of the game property to add
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def game_property_remove(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None,
                         *,
                         index: typing.Optional[typing.Any] = 0):
    ''' Remove game property

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param index: Index, Property index to remove
    :type index: typing.Optional[typing.Any]
    '''

    pass


def group_add(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Add an object to a new group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def group_instance_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "Group",
        group: typing.Union[str, int, typing.Any] = '',
        view_align: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add a dupligroup instance

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Group name to add
    :type name: typing.Union[str, typing.Any]
    :param group: Group
    :type group: typing.Union[str, int, typing.Any]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def group_link(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               group: typing.Union[str, int, typing.Any] = ''):
    ''' Add an object to an existing group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group: Group
    :type group: typing.Union[str, int, typing.Any]
    '''

    pass


def group_remove(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Remove the active object from this group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def group_unlink(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Unlink the group from all objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def grouped_select(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Select all objects in group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def hide_render_clear(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Reveal the render object by setting the hide render flag

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def hide_render_clear_all(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None):
    ''' Reveal all render objects by setting the hide render flag :file: `startup/bl_operators/object.py\:682 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/object.py$682>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def hide_render_set(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    unselected: typing.Union[bool, typing.Any] = False):
    ''' Hide the render object by setting the hide render flag

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: typing.Union[bool, typing.Any]
    '''

    pass


def hide_view_clear(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Reveal the object by setting the hide flag

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def hide_view_set(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  unselected: typing.Union[bool, typing.Any] = False):
    ''' Hide the object by setting the hide flag

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: typing.Union[bool, typing.Any]
    '''

    pass


def hook_add_newob(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Hook selected vertices to a newly created object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def hook_add_selob(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   use_bone: typing.Union[bool, typing.Any] = False):
    ''' Hook selected vertices to the first selected object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_bone: Active Bone, Assign the hook to the hook objects active bone
    :type use_bone: typing.Union[bool, typing.Any]
    '''

    pass


def hook_assign(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                modifier: typing.Union[str, int, typing.Any] = ''):
    ''' Assign the selected vertices to a hook

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Union[str, int, typing.Any]
    '''

    pass


def hook_recenter(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  modifier: typing.Union[str, int, typing.Any] = ''):
    ''' Set hook center to cursor position

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Union[str, int, typing.Any]
    '''

    pass


def hook_remove(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                modifier: typing.Union[str, int, typing.Any] = ''):
    ''' Remove a hook from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to remove
    :type modifier: typing.Union[str, int, typing.Any]
    '''

    pass


def hook_reset(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               modifier: typing.Union[str, int, typing.Any] = ''):
    ''' Recalculate and clear offset transformation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: typing.Union[str, int, typing.Any]
    '''

    pass


def hook_select(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                modifier: typing.Union[str, int, typing.Any] = ''):
    ''' Select affected vertices on mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Modifier number to remove
    :type modifier: typing.Union[str, int, typing.Any]
    '''

    pass


def isolate_type_render(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Hide unselected render objects of same type as active by setting the hide render flag :file: `startup/bl_operators/object.py\:662 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/object.py$662>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def join(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None):
    ''' Join selected objects into active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def join_shapes(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Merge selected objects to shapes of active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def join_uvs(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Transfer UV Maps from active to selected objects (needs matching geometry) :file: `startup/bl_operators/object.py\:571 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/object.py$571>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def lamp_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'POINT',
        radius: typing.Optional[typing.Any] = 1.0,
        view_align: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add a lamp object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type * ``POINT`` Point, Omnidirectional point light source. * ``SUN`` Sun, Constant direction parallel ray light source. * ``SPOT`` Spot, Directional cone light source. * ``HEMI`` Hemi, 180 degree constant light source. * ``AREA`` Area, Directional area light source.
    :type type: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def laplaciandeform_bind(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None,
                         *,
                         modifier: typing.Union[str, typing.Any] = ""):
    ''' Bind mesh to system in laplacian deform modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def location_clear(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   clear_delta: typing.Union[bool, typing.Any] = False):
    ''' Clear the object's location

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform
    :type clear_delta: typing.Union[bool, typing.Any]
    '''

    pass


def lod_add(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: typing.Optional[bool] = None):
    ''' Add a level of detail to this object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def lod_by_name(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Add levels of detail to this object based on object names :file: `startup/bl_operators/object.py\:892 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/object.py$892>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def lod_clear_all(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Remove all levels of detail from this object :file: `startup/bl_operators/object.py\:942 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/object.py$942>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def lod_generate(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 count: typing.Optional[typing.Any] = 3,
                 target: typing.Optional[typing.Any] = 0.1,
                 package: typing.Union[bool, typing.Any] = False):
    ''' Generate levels of detail using the decimate modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param count: Count
    :type count: typing.Optional[typing.Any]
    :param target: Target Size
    :type target: typing.Optional[typing.Any]
    :param package: Package into Group
    :type package: typing.Union[bool, typing.Any]
    '''

    pass


def lod_remove(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               index: typing.Optional[typing.Any] = 1):
    ''' Remove a level of detail from this object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param index: Index
    :type index: typing.Optional[typing.Any]
    '''

    pass


def logic_bricks_copy(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Copy logic bricks to other selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def make_dupli_face(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Convert objects into dupli-face instanced :file: `startup/bl_operators/object.py\:650 <https://developer.blender.org/diffusion/B/browse/master/release/scripts /startup/bl_operators/object.py$650>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def make_links_data(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    type: typing.Optional[typing.Any] = 'OBDATA'):
    ''' Apply active object links to other selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def make_links_scene(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     scene: typing.Union[str, int, typing.Any] = ''):
    ''' Link selection to another scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param scene: Scene
    :type scene: typing.Union[str, int, typing.Any]
    '''

    pass


def make_local(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               type: typing.Optional[typing.Any] = 'SELECT_OBJECT'):
    ''' Make library linked data-blocks local to this file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def make_single_user(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     type: typing.Optional[typing.Any] = 'SELECTED_OBJECTS',
                     object: typing.Union[bool, typing.Any] = False,
                     obdata: typing.Union[bool, typing.Any] = False,
                     material: typing.Union[bool, typing.Any] = False,
                     texture: typing.Union[bool, typing.Any] = False,
                     animation: typing.Union[bool, typing.Any] = False):
    ''' Make linked data local to each object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param object: Object, Make single user objects
    :type object: typing.Union[bool, typing.Any]
    :param obdata: Object Data, Make single user object data
    :type obdata: typing.Union[bool, typing.Any]
    :param material: Materials, Make materials local to each data-block
    :type material: typing.Union[bool, typing.Any]
    :param texture: Textures, Make textures local to each material (needs 'Materials' to be set too)
    :type texture: typing.Union[bool, typing.Any]
    :param animation: Object Animation, Make animation data local to each object
    :type animation: typing.Union[bool, typing.Any]
    '''

    pass


def material_slot_add(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Add a new material slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_assign(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Assign active material slot to selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_copy(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None):
    ''' Copies materials to other selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_deselect(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: typing.Optional[bool] = None):
    ''' Deselect by active material slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_move(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move the active material up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to move the active material towards
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def material_slot_remove(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Remove the selected material slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_slot_select(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Select by active material slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def meshdeform_bind(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    modifier: typing.Union[str, typing.Any] = ""):
    ''' Bind mesh to cage in mesh deform modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def metaball_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'BALL',
        radius: typing.Optional[typing.Any] = 1.0,
        view_align: typing.Union[bool, typing.Any] = False,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add an metaball object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Primitive
    :type type: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def mode_set(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             mode: typing.Optional[typing.Any] = 'OBJECT',
             toggle: typing.Union[bool, typing.Any] = False):
    ''' Sets the object interaction mode

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``OBJECT`` Object Mode. * ``EDIT`` Edit Mode. * ``POSE`` Pose Mode. * ``SCULPT`` Sculpt Mode. * ``VERTEX_PAINT`` Vertex Paint. * ``WEIGHT_PAINT`` Weight Paint. * ``TEXTURE_PAINT`` Texture Paint. * ``PARTICLE_EDIT`` Particle Edit. * ``GPENCIL_EDIT`` Edit Strokes, Edit Grease Pencil Strokes.
    :type mode: typing.Optional[typing.Any]
    :param toggle: Toggle
    :type toggle: typing.Union[bool, typing.Any]
    '''

    pass


def modifier_add(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 type: typing.Optional[typing.Any] = 'SUBSURF'):
    ''' Add a procedural operation/effect to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type * ``DATA_TRANSFER`` Data Transfer. * ``MESH_CACHE`` Mesh Cache. * ``MESH_SEQUENCE_CACHE`` Mesh Sequence Cache. * ``NORMAL_EDIT`` Normal Edit. * ``UV_PROJECT`` UV Project. * ``UV_WARP`` UV Warp. * ``VERTEX_WEIGHT_EDIT`` Vertex Weight Edit. * ``VERTEX_WEIGHT_MIX`` Vertex Weight Mix. * ``VERTEX_WEIGHT_PROXIMITY`` Vertex Weight Proximity. * ``ARRAY`` Array. * ``BEVEL`` Bevel. * ``BOOLEAN`` Boolean. * ``BUILD`` Build. * ``DECIMATE`` Decimate. * ``EDGE_SPLIT`` Edge Split. * ``MASK`` Mask. * ``MIRROR`` Mirror. * ``MULTIRES`` Multiresolution. * ``REMESH`` Remesh. * ``SCREW`` Screw. * ``SKIN`` Skin. * ``SOLIDIFY`` Solidify. * ``SUBSURF`` Subdivision Surface. * ``TRIANGULATE`` Triangulate. * ``WIREFRAME`` Wireframe, Generate a wireframe on the edges of a mesh. * ``ARMATURE`` Armature. * ``CAST`` Cast. * ``CORRECTIVE_SMOOTH`` Corrective Smooth. * ``CURVE`` Curve. * ``DISPLACE`` Displace. * ``HOOK`` Hook. * ``LAPLACIANSMOOTH`` Laplacian Smooth. * ``LAPLACIANDEFORM`` Laplacian Deform. * ``LATTICE`` Lattice. * ``MESH_DEFORM`` Mesh Deform. * ``SHRINKWRAP`` Shrinkwrap. * ``SIMPLE_DEFORM`` Simple Deform. * ``SMOOTH`` Smooth. * ``SURFACE_DEFORM`` Surface Deform. * ``WARP`` Warp. * ``WAVE`` Wave. * ``CLOTH`` Cloth. * ``COLLISION`` Collision. * ``DYNAMIC_PAINT`` Dynamic Paint. * ``EXPLODE`` Explode. * ``FLUID_SIMULATION`` Fluid Simulation. * ``OCEAN`` Ocean. * ``PARTICLE_INSTANCE`` Particle Instance. * ``PARTICLE_SYSTEM`` Particle System. * ``SMOKE`` Smoke. * ``SOFT_BODY`` Soft Body. * ``SURFACE`` Surface.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def modifier_apply(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   apply_as: typing.Optional[typing.Any] = 'DATA',
                   modifier: typing.Union[str, typing.Any] = ""):
    ''' Apply modifier and remove from the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param apply_as: Apply as, How to apply the modifier to the geometry * ``DATA`` Object Data, Apply modifier to the object's data. * ``SHAPE`` New Shape, Apply deform-only modifier to a new shape on this object.
    :type apply_as: typing.Optional[typing.Any]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_convert(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     modifier: typing.Union[str, typing.Any] = ""):
    ''' Convert particles to a mesh object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_copy(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  modifier: typing.Union[str, typing.Any] = ""):
    ''' Duplicate modifier at the same position in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_move_down(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       modifier: typing.Union[str, typing.Any] = ""):
    ''' Move modifier down in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_move_up(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     modifier: typing.Union[str, typing.Any] = ""):
    ''' Move modifier up in the stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def modifier_remove(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    modifier: typing.Union[str, typing.Any] = ""):
    ''' Remove a modifier from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def move_to_layer(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Move the object to different layers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def multires_base_apply(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        modifier: typing.Union[str, typing.Any] = ""):
    ''' Modify the base mesh to conform to the displaced mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def multires_external_pack(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: typing.Optional[bool] = None):
    ''' Pack displacements from an external file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def multires_external_save(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Union[bool, typing.Any] = True,
        filter_blender: typing.Union[bool, typing.Any] = False,
        filter_backup: typing.Union[bool, typing.Any] = False,
        filter_image: typing.Union[bool, typing.Any] = False,
        filter_movie: typing.Union[bool, typing.Any] = False,
        filter_python: typing.Union[bool, typing.Any] = False,
        filter_font: typing.Union[bool, typing.Any] = False,
        filter_sound: typing.Union[bool, typing.Any] = False,
        filter_text: typing.Union[bool, typing.Any] = False,
        filter_btx: typing.Union[bool, typing.Any] = True,
        filter_collada: typing.Union[bool, typing.Any] = False,
        filter_alembic: typing.Union[bool, typing.Any] = False,
        filter_folder: typing.Union[bool, typing.Any] = True,
        filter_blenlib: typing.Union[bool, typing.Any] = False,
        filemode: typing.Optional[typing.Any] = 9,
        relative_path: typing.Union[bool, typing.Any] = True,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Save displacements to an external file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Union[bool, typing.Any]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Union[bool, typing.Any]
    :param filter_image: Filter image files
    :type filter_image: typing.Union[bool, typing.Any]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Union[bool, typing.Any]
    :param filter_python: Filter python files
    :type filter_python: typing.Union[bool, typing.Any]
    :param filter_font: Filter font files
    :type filter_font: typing.Union[bool, typing.Any]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Union[bool, typing.Any]
    :param filter_text: Filter text files
    :type filter_text: typing.Union[bool, typing.Any]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Union[bool, typing.Any]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Union[bool, typing.Any]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Union[bool, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Union[bool, typing.Any]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: typing.Union[bool, typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def multires_higher_levels_delete(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        modifier: typing.Union[str, typing.Any] = ""):
    ''' Deletes the higher resolution mesh, potential loss of detail

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def multires_reshape(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     modifier: typing.Union[str, typing.Any] = ""):
    ''' Copy vertex coordinates from other object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def multires_subdivide(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       modifier: typing.Union[str, typing.Any] = ""):
    ''' Add a new level of subdivision

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def ocean_bake(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               modifier: typing.Union[str, typing.Any] = "",
               free: typing.Union[bool, typing.Any] = False):
    ''' Bake an image sequence of ocean data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    :param free: Free, Free the bake, rather than generating it
    :type free: typing.Union[bool, typing.Any]
    '''

    pass


def origin_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Clear the object's origin

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def origin_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               type: typing.Optional[typing.Any] = 'GEOMETRY_ORIGIN',
               center: typing.Optional[typing.Any] = 'MEDIAN'):
    ''' Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type * ``GEOMETRY_ORIGIN`` Geometry to Origin, Move object geometry to object origin. * ``ORIGIN_GEOMETRY`` Origin to Geometry, Calculate the center of geometry based on the current pivot point (median, otherwise bounding-box). * ``ORIGIN_CURSOR`` Origin to 3D Cursor, Move object origin to position of the 3D cursor. * ``ORIGIN_CENTER_OF_MASS`` Origin to Center of Mass (Surface), Calculate the center of mass from the surface area. * ``ORIGIN_CENTER_OF_VOLUME`` Origin to Center of Mass (Volume), Calculate the center of mass from the volume (must be manifold geometry with consistent normals).
    :type type: typing.Optional[typing.Any]
    :param center: Center
    :type center: typing.Optional[typing.Any]
    '''

    pass


def parent_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 type: typing.Optional[typing.Any] = 'CLEAR'):
    ''' Clear the object's parenting

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CLEAR`` Clear Parent, Completely clear the parenting relationship, including involved modifiers if any. * ``CLEAR_KEEP_TRANSFORM`` Clear and Keep Transformation, As 'Clear Parent', but keep the current visual transformations of the object. * ``CLEAR_INVERSE`` Clear Parent Inverse, Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def parent_no_inverse_set(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None):
    ''' Set the object's parenting without setting the inverse parent correction

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def parent_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               type: typing.Optional[typing.Any] = 'OBJECT',
               xmirror: typing.Union[bool, typing.Any] = False,
               keep_transform: typing.Union[bool, typing.Any] = False):
    ''' Set the object's parenting

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation
    :type xmirror: typing.Union[bool, typing.Any]
    :param keep_transform: Keep Transform, Apply transformation before parenting
    :type keep_transform: typing.Union[bool, typing.Any]
    '''

    pass


def particle_system_add(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Add a particle system

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def particle_system_remove(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: typing.Optional[bool] = None):
    ''' Remove the selected particle system

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def paths_calculate(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    start_frame: typing.Optional[typing.Any] = 1,
                    end_frame: typing.Optional[typing.Any] = 250):
    ''' Calculate motion paths for the selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param start_frame: Start, First frame to calculate object paths on
    :type start_frame: typing.Optional[typing.Any]
    :param end_frame: End, Last frame to calculate object paths on
    :type end_frame: typing.Optional[typing.Any]
    '''

    pass


def paths_clear(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                only_selected: typing.Union[bool, typing.Any] = False):
    ''' Clear path caches for all objects, hold Shift key for selected objects only

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param only_selected: Only Selected, Only clear paths from selected objects
    :type only_selected: typing.Union[bool, typing.Any]
    '''

    pass


def paths_update(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Recalculate paths for selected objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def posemode_toggle(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Enable or disable posing/selecting bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def proxy_make(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               object: typing.Union[str, int, typing.Any] = 'DEFAULT'):
    ''' Add empty object to become local replacement data of a library-linked object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param object: Proxy Object, Name of lib-linked/grouped object to make a proxy for
    :type object: typing.Union[str, int, typing.Any]
    '''

    pass


def quick_explode(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  style: typing.Optional[typing.Any] = 'EXPLODE',
                  amount: typing.Optional[typing.Any] = 100,
                  frame_duration: typing.Optional[typing.Any] = 50,
                  frame_start: typing.Optional[typing.Any] = 1,
                  frame_end: typing.Optional[typing.Any] = 10,
                  velocity: typing.Optional[typing.Any] = 1.0,
                  fade: typing.Union[bool, typing.Any] = True):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param style: Explode Style
    :type style: typing.Optional[typing.Any]
    :param amount: Amount of pieces
    :type amount: typing.Optional[typing.Any]
    :param frame_duration: Duration
    :type frame_duration: typing.Optional[typing.Any]
    :param frame_start: Start Frame
    :type frame_start: typing.Optional[typing.Any]
    :param frame_end: End Frame
    :type frame_end: typing.Optional[typing.Any]
    :param velocity: Outwards Velocity
    :type velocity: typing.Optional[typing.Any]
    :param fade: Fade, Fade the pieces over time
    :type fade: typing.Union[bool, typing.Any]
    '''

    pass


def quick_fluid(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                style: typing.Optional[typing.Any] = 'BASIC',
                initial_velocity: typing.Optional[typing.Any] = (0.0, 0.0,
                                                                 0.0),
                show_flows: typing.Union[bool, typing.Any] = False,
                start_baking: typing.Union[bool, typing.Any] = False):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param style: Fluid Style
    :type style: typing.Optional[typing.Any]
    :param initial_velocity: Initial Velocity, Initial velocity of the fluid
    :type initial_velocity: typing.Optional[typing.Any]
    :param show_flows: Render Fluid Objects, Keep the fluid objects visible during rendering
    :type show_flows: typing.Union[bool, typing.Any]
    :param start_baking: Start Fluid Bake, Start baking the fluid immediately after creating the domain object
    :type start_baking: typing.Union[bool, typing.Any]
    '''

    pass


def quick_fur(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              density: typing.Optional[typing.Any] = 'MEDIUM',
              view_percentage: typing.Optional[typing.Any] = 10,
              length: typing.Optional[typing.Any] = 0.1):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param density: Fur Density
    :type density: typing.Optional[typing.Any]
    :param view_percentage: View %
    :type view_percentage: typing.Optional[typing.Any]
    :param length: Length
    :type length: typing.Optional[typing.Any]
    '''

    pass


def quick_smoke(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                style: typing.Optional[typing.Any] = 'SMOKE',
                show_flows: typing.Union[bool, typing.Any] = False):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param style: Smoke Style
    :type style: typing.Optional[typing.Any]
    :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering
    :type show_flows: typing.Union[bool, typing.Any]
    '''

    pass


def randomize_transform(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        random_seed: typing.Optional[typing.Any] = 0,
                        use_delta: typing.Union[bool, typing.Any] = False,
                        use_loc: typing.Union[bool, typing.Any] = True,
                        loc: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
                        use_rot: typing.Union[bool, typing.Any] = True,
                        rot: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
                        use_scale: typing.Union[bool, typing.Any] = True,
                        scale_even: typing.Union[bool, typing.Any] = False,
                        scale: typing.Optional[typing.Any] = (1.0, 1.0, 1.0)):
    ''' Randomize objects loc/rot/scale

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param random_seed: Random Seed, Seed value for the random generator
    :type random_seed: typing.Optional[typing.Any]
    :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform
    :type use_delta: typing.Union[bool, typing.Any]
    :param use_loc: Randomize Location, Randomize the location values
    :type use_loc: typing.Union[bool, typing.Any]
    :param loc: Location, Maximum distance the objects can spread over each axis
    :type loc: typing.Optional[typing.Any]
    :param use_rot: Randomize Rotation, Randomize the rotation values
    :type use_rot: typing.Union[bool, typing.Any]
    :param rot: Rotation, Maximum rotation over each axis
    :type rot: typing.Optional[typing.Any]
    :param use_scale: Randomize Scale, Randomize the scale values
    :type use_scale: typing.Union[bool, typing.Any]
    :param scale_even: Scale Even, Use the same scale value for all axis
    :type scale_even: typing.Union[bool, typing.Any]
    :param scale: Scale, Maximum scale randomization over each axis
    :type scale: typing.Optional[typing.Any]
    '''

    pass


def rotation_clear(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   clear_delta: typing.Union[bool, typing.Any] = False):
    ''' Clear the object's rotation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform
    :type clear_delta: typing.Union[bool, typing.Any]
    '''

    pass


def scale_clear(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                clear_delta: typing.Union[bool, typing.Any] = False):
    ''' Clear the object's scale

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform
    :type clear_delta: typing.Union[bool, typing.Any]
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection of all visible objects in scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle, Toggle selection for all elements. * ``SELECT`` Select, Select all elements. * ``DESELECT`` Deselect, Deselect all elements. * ``INVERT`` Invert, Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_by_layer(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    match: typing.Optional[typing.Any] = 'EXACT',
                    extend: typing.Union[bool, typing.Any] = False,
                    layers: typing.Optional[typing.Any] = 1):
    ''' Select all visible objects on a layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param match: Match
    :type match: typing.Optional[typing.Any]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    :param layers: Layer
    :type layers: typing.Optional[typing.Any]
    '''

    pass


def select_by_type(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   extend: typing.Union[bool, typing.Any] = False,
                   type: typing.Optional[typing.Any] = 'MESH'):
    ''' Select all visible objects that are of a type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def select_camera(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  extend: typing.Union[bool, typing.Any] = False):
    ''' Select the active camera

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_grouped(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   extend: typing.Union[bool, typing.Any] = False,
                   type: typing.Optional[typing.Any] = 'CHILDREN_RECURSIVE'):
    ''' Select all visible objects grouped by various properties

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    :param type: Type * ``CHILDREN_RECURSIVE`` Children. * ``CHILDREN`` Immediate Children. * ``PARENT`` Parent. * ``SIBLINGS`` Siblings, Shared Parent. * ``TYPE`` Type, Shared object type. * ``LAYER`` Layer, Shared layers. * ``GROUP`` Group, Shared group. * ``HOOK`` Hook. * ``PASS`` Pass, Render pass Index. * ``COLOR`` Color, Object Color. * ``PROPERTIES`` Properties, Game Properties. * ``KEYINGSET`` Keying Set, Objects included in active Keying Set. * ``LAMP_TYPE`` Lamp Type, Matching lamp types.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def select_hierarchy(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     direction: typing.Optional[typing.Any] = 'PARENT',
                     extend: typing.Union[bool, typing.Any] = False):
    ''' Select object relative to the active object's position in the hierarchy

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to select in the hierarchy
    :type direction: typing.Optional[typing.Any]
    :param extend: Extend, Extend the existing selection
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Deselect objects at the boundaries of parent/child relationships

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  extend: typing.Union[bool, typing.Any] = False,
                  type: typing.Optional[typing.Any] = 'OBDATA'):
    ''' Select all visible objects that are linked

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def select_mirror(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  extend: typing.Union[bool, typing.Any] = False):
    ''' Select the Mirror objects of the selected object eg. L.sword -> R.sword

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Select connected parent/child objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_pattern(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   pattern: typing.Union[str, typing.Any] = "*",
                   case_sensitive: typing.Union[bool, typing.Any] = False,
                   extend: typing.Union[bool, typing.Any] = True):
    ''' Select objects matching a naming pattern

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param pattern: Pattern, Name filter using '*', '?' and '[abc]' unix style wildcards
    :type pattern: typing.Union[str, typing.Any]
    :param case_sensitive: Case Sensitive, Do a case sensitive compare
    :type case_sensitive: typing.Union[bool, typing.Any]
    :param extend: Extend, Extend the existing selection
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_random(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  percent: typing.Optional[typing.Any] = 50.0,
                  seed: typing.Optional[typing.Any] = 0,
                  action: typing.Optional[typing.Any] = 'SELECT'):
    ''' Set select on random visible objects

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param percent: Percent, Percentage of objects to select randomly
    :type percent: typing.Optional[typing.Any]
    :param seed: Random Seed, Seed for the random number generator
    :type seed: typing.Optional[typing.Any]
    :param action: Action, Selection action to execute * ``SELECT`` Select, Select all elements. * ``DESELECT`` Deselect, Deselect all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_same_group(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      group: typing.Union[str, typing.Any] = ""):
    ''' Select object in the same group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group: Group, Name of the group to select
    :type group: typing.Union[str, typing.Any]
    '''

    pass


def shade_flat(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Render and display faces uniform, using Face Normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def shade_smooth(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Render and display faces smooth, using interpolated Vertex Normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def shape_key_add(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  from_mix: typing.Union[bool, typing.Any] = True):
    ''' Add shape key to the object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param from_mix: From Mix, Create the new shape key from the existing mix of keys
    :type from_mix: typing.Union[bool, typing.Any]
    '''

    pass


def shape_key_clear(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Clear weights for all shape keys

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def shape_key_mirror(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     use_topology: typing.Union[bool, typing.Any] = False):
    ''' Mirror the current shape key along the local X axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: typing.Union[bool, typing.Any]
    '''

    pass


def shape_key_move(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   type: typing.Optional[typing.Any] = 'TOP'):
    ''' Move the active shape key up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type * ``TOP`` Top, Top of the list. * ``UP`` Up. * ``DOWN`` Down. * ``BOTTOM`` Bottom, Bottom of the list.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def shape_key_remove(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     all: typing.Union[bool, typing.Any] = False):
    ''' Remove shape key from the object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param all: All, Remove all shape keys
    :type all: typing.Union[bool, typing.Any]
    '''

    pass


def shape_key_retime(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Resets the timing for absolute shape keys

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def shape_key_transfer(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       mode: typing.Optional[typing.Any] = 'OFFSET',
                       use_clamp: typing.Union[bool, typing.Any] = False):
    ''' Copy another selected objects active shape to this one by applying the relative offsets

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Transformation Mode, Relative shape positions to the new shape method * ``OFFSET`` Offset, Apply the relative positional offset. * ``RELATIVE_FACE`` Relative Face, Calculate relative position (using faces). * ``RELATIVE_EDGE`` Relative Edge, Calculate relative position (using edges).
    :type mode: typing.Optional[typing.Any]
    :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape
    :type use_clamp: typing.Union[bool, typing.Any]
    '''

    pass


def skin_armature_create(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None,
                         *,
                         modifier: typing.Union[str, typing.Any] = ""):
    ''' Create an armature that parallels the skin layout

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def skin_loose_mark_clear(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None,
                          *,
                          action: typing.Optional[typing.Any] = 'MARK'):
    ''' Mark/clear selected vertices as loose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action * ``MARK`` Mark, Mark selected vertices as loose. * ``CLEAR`` Clear, Set selected vertices as not loose.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def skin_radii_equalize(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Make skin radii of selected vertices equal on each axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def skin_root_mark(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Mark selected vertices as roots

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def slow_parent_clear(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Clear the object's slow parent

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def slow_parent_set(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Set the object's slow parent

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def speaker_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        view_align: typing.Union[bool, typing.Any] = False,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add a speaker object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def subdivision_set(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    level: typing.Optional[typing.Any] = 1,
                    relative: typing.Union[bool, typing.Any] = False):
    ''' Sets a Subdivision Surface Level (1-5)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param level: Level
    :type level: typing.Optional[typing.Any]
    :param relative: Relative, Apply the subsurf level as an offset relative to the current level
    :type relative: typing.Union[bool, typing.Any]
    '''

    pass


def surfacedeform_bind(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       modifier: typing.Union[str, typing.Any] = ""):
    ''' Bind mesh to target in surface deform modifier

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: typing.Union[str, typing.Any]
    '''

    pass


def text_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        radius: typing.Optional[typing.Any] = 1.0,
        view_align: typing.Union[bool, typing.Any] = False,
        enter_editmode: typing.Union[bool, typing.Any] = False,
        location: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        rotation: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        layers: typing.Union[typing.List[bool], typing.Any] = (False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False,
                                                               False, False)):
    ''' Add a text object to the scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param view_align: Align to View, Align the new object to the view
    :type view_align: typing.Union[bool, typing.Any]
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: typing.Union[bool, typing.Any]
    :param location: Location, Location for the newly added object
    :type location: typing.Optional[typing.Any]
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: typing.Optional[typing.Any]
    :param layers: Layer
    :type layers: typing.Union[typing.List[bool], typing.Any]
    '''

    pass


def track_clear(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                type: typing.Optional[typing.Any] = 'CLEAR'):
    ''' Clear tracking constraint or flag from object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def track_set(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              type: typing.Optional[typing.Any] = 'DAMPTRACK'):
    ''' Make the object track another object, using various methods/constraints

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def transform_apply(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    location: typing.Union[bool, typing.Any] = False,
                    rotation: typing.Union[bool, typing.Any] = False,
                    scale: typing.Union[bool, typing.Any] = False):
    ''' Apply the object's transformation to its data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param location: Location
    :type location: typing.Union[bool, typing.Any]
    :param rotation: Rotation
    :type rotation: typing.Union[bool, typing.Any]
    :param scale: Scale
    :type scale: typing.Union[bool, typing.Any]
    '''

    pass


def transforms_to_deltas(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None,
                         *,
                         mode: typing.Optional[typing.Any] = 'ALL',
                         reset_values: typing.Union[bool, typing.Any] = True):
    ''' Convert normal object transforms to delta transforms, any existing delta transforms will be included as well

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Which transforms to transfer * ``ALL`` All Transforms, Transfer location, rotation, and scale transforms. * ``LOC`` Location, Transfer location transforms only. * ``ROT`` Rotation, Transfer rotation transforms only. * ``SCALE`` Scale, Transfer scale transforms only.
    :type mode: typing.Optional[typing.Any]
    :param reset_values: Reset Values, Clear transform values after transferring to deltas
    :type reset_values: typing.Union[bool, typing.Any]
    '''

    pass


def unlink_data(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_add(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Add a new vertex group to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_assign(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Assign the selected vertices to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_assign_new(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None):
    ''' Assign the selected vertices to a new vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_clean(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Union[str, int, typing.Any] = '',
        limit: typing.Optional[typing.Any] = 0.0,
        keep_single: typing.Union[bool, typing.Any] = False):
    ''' Remove vertex group assignments which are not required

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: typing.Union[str, int, typing.Any]
    :param limit: Limit, Remove vertices which weight is below or equal to this limit
    :type limit: typing.Optional[typing.Any]
    :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning
    :type keep_single: typing.Union[bool, typing.Any]
    '''

    pass


def vertex_group_copy(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Make a copy of the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_copy_to_linked(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Replace vertex groups of all users of the same geometry data by vertex groups of active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_copy_to_selected(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Replace vertex groups of selected objects by vertex groups of active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_deselect(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None):
    ''' Deselect all selected vertices assigned to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_fix(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     dist: typing.Optional[typing.Any] = 0.0,
                     strength: typing.Optional[typing.Any] = 1.0,
                     accuracy: typing.Optional[typing.Any] = 1.0):
    ''' Modify the position of selected vertices by changing only their respective groups' weights (this tool may be slow for many vertices)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param dist: Distance, The distance to move to
    :type dist: typing.Optional[typing.Any]
    :param strength: Strength, The distance moved can be changed by this multiplier
    :type strength: typing.Optional[typing.Any]
    :param accuracy: Change Sensitivity, Change the amount weights are altered with each iteration: lower values are slower
    :type accuracy: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_invert(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Union[str, int, typing.Any] = '',
        auto_assign: typing.Union[bool, typing.Any] = True,
        auto_remove: typing.Union[bool, typing.Any] = True):
    ''' Invert active vertex group's weights

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: typing.Union[str, int, typing.Any]
    :param auto_assign: Add Weights, Add verts from groups that have zero weight before inverting
    :type auto_assign: typing.Union[bool, typing.Any]
    :param auto_remove: Remove Weights, Remove verts from groups that have zero weight after inverting
    :type auto_remove: typing.Union[bool, typing.Any]
    '''

    pass


def vertex_group_levels(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Union[str, int, typing.Any] = '',
        offset: typing.Optional[typing.Any] = 0.0,
        gain: typing.Optional[typing.Any] = 1.0):
    ''' Add some offset and multiply with some gain the weights of the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: typing.Union[str, int, typing.Any]
    :param offset: Offset, Value to add to weights
    :type offset: typing.Optional[typing.Any]
    :param gain: Gain, Value to multiply weights by
    :type gain: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_limit_total(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Union[str, int, typing.Any] = '',
        limit: typing.Optional[typing.Any] = 4):
    ''' Limit deform weights associated with a vertex to a specified number by removing lowest weights

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: typing.Union[str, int, typing.Any]
    :param limit: Limit, Maximum number of deform weights
    :type limit: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_lock(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change the lock state of all vertex groups of active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action, Lock action to execute on vertex groups * ``TOGGLE`` Toggle, Unlock all vertex groups if there is at least one locked group, lock all in other case. * ``LOCK`` Lock, Lock all vertex groups. * ``UNLOCK`` Unlock, Unlock all vertex groups. * ``INVERT`` Invert, Invert the lock state of all vertex groups.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_mirror(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        mirror_weights: typing.Union[bool, typing.Any] = True,
        flip_group_names: typing.Union[bool, typing.Any] = True,
        all_groups: typing.Union[bool, typing.Any] = False,
        use_topology: typing.Union[bool, typing.Any] = False):
    ''' Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mirror_weights: Mirror Weights, Mirror weights
    :type mirror_weights: typing.Union[bool, typing.Any]
    :param flip_group_names: Flip Group Names, Flip vertex group names
    :type flip_group_names: typing.Union[bool, typing.Any]
    :param all_groups: All Groups, Mirror all vertex groups weights
    :type all_groups: typing.Union[bool, typing.Any]
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: typing.Union[bool, typing.Any]
    '''

    pass


def vertex_group_move(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move the active vertex group up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction to move the active vertex group towards
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_normalize(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: typing.Optional[bool] = None):
    ''' Normalize weights of the active vertex group, so that the highest ones are now 1.0

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_normalize_all(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Union[str, int, typing.Any] = '',
        lock_active: typing.Union[bool, typing.Any] = True):
    ''' Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: typing.Union[str, int, typing.Any]
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    :type lock_active: typing.Union[bool, typing.Any]
    '''

    pass


def vertex_group_quantize(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Union[str, int, typing.Any] = '',
        steps: typing.Optional[typing.Any] = 4):
    ''' Set weights to a fixed number of steps

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: typing.Union[str, int, typing.Any]
    :param steps: Steps, Number of steps between 0 and 1
    :type steps: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_remove(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        all: typing.Union[bool, typing.Any] = False,
                        all_unlocked: typing.Union[bool, typing.Any] = False):
    ''' Delete the active or all vertex groups from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param all: All, Remove all vertex groups
    :type all: typing.Union[bool, typing.Any]
    :param all_unlocked: All Unlocked, Remove all unlocked vertex groups
    :type all_unlocked: typing.Union[bool, typing.Any]
    '''

    pass


def vertex_group_remove_from(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        use_all_groups: typing.Union[bool, typing.Any] = False,
        use_all_verts: typing.Union[bool, typing.Any] = False):
    ''' Remove the selected vertices from active or all vertex group(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_all_groups: All Groups, Remove from all groups
    :type use_all_groups: typing.Union[bool, typing.Any]
    :param use_all_verts: All Verts, Clear the active group
    :type use_all_verts: typing.Union[bool, typing.Any]
    '''

    pass


def vertex_group_select(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Select all the vertices assigned to the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_group_set_active(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None,
                            *,
                            group: typing.Union[str, int, typing.Any] = ''):
    ''' Set the active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group: Group, Vertex group to set as active
    :type group: typing.Union[str, int, typing.Any]
    '''

    pass


def vertex_group_smooth(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        group_select_mode: typing.Union[str, int, typing.Any] = '',
        factor: typing.Optional[typing.Any] = 0.5,
        repeat: typing.Optional[typing.Any] = 1,
        expand: typing.Optional[typing.Any] = 0.0,
        source: typing.Optional[typing.Any] = 'ALL'):
    ''' Smooth weights for selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: typing.Union[str, int, typing.Any]
    :param factor: Factor
    :type factor: typing.Optional[typing.Any]
    :param repeat: Iterations
    :type repeat: typing.Optional[typing.Any]
    :param expand: Expand/Contract, Expand/contract weights
    :type expand: typing.Optional[typing.Any]
    :param source: Source, Vertices to mix with
    :type source: typing.Optional[typing.Any]
    '''

    pass


def vertex_group_sort(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      sort_type: typing.Optional[typing.Any] = 'NAME'):
    ''' Sort vertex groups

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param sort_type: Sort type, Sort type
    :type sort_type: typing.Optional[typing.Any]
    '''

    pass


def vertex_parent_set(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Parent selected objects to the selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_weight_copy(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None):
    ''' Copy weights from active to selected

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_weight_delete(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None,
                         *,
                         weight_group: typing.Optional[typing.Any] = -1):
    ''' Delete this weight from the vertex (disabled if vertex group is locked)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: typing.Optional[typing.Any]
    '''

    pass


def vertex_weight_normalize_active_vertex(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Normalize active vertex's weights

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_weight_paste(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        weight_group: typing.Optional[typing.Any] = -1):
    ''' Copy this group's weight to other selected verts (disabled if vertex group is locked)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: typing.Optional[typing.Any]
    '''

    pass


def vertex_weight_set_active(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: typing.Optional[bool] = None,
                             *,
                             weight_group: typing.Optional[typing.Any] = -1):
    ''' Set as active vertex group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: typing.Optional[typing.Any]
    '''

    pass


def visual_transform_apply(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: typing.Optional[bool] = None):
    ''' Apply the object's visual transformation to its data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
