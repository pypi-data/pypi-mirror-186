import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def align(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: typing.Optional[bool] = None,
          *,
          axis: typing.Optional[typing.Any] = 'ALIGN_AUTO'):
    ''' Align selected UV vertices to an axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param axis: Axis, Axis to align UV locations on * ``ALIGN_S`` Straighten, Align UVs along the line defined by the endpoints. * ``ALIGN_T`` Straighten X, Align UVs along the line defined by the endpoints along the X axis. * ``ALIGN_U`` Straighten Y, Align UVs along the line defined by the endpoints along the Y axis. * ``ALIGN_AUTO`` Align Auto, Automatically choose the axis on which there is most alignment already. * ``ALIGN_X`` Align X, Align UVs on X axis. * ``ALIGN_Y`` Align Y, Align UVs on Y axis.
    :type axis: typing.Optional[typing.Any]
    '''

    pass


def average_islands_scale(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None):
    ''' Average the size of separate UV islands, based on their area in 3D space

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def circle_select(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  x: typing.Optional[typing.Any] = 0,
                  y: typing.Optional[typing.Any] = 0,
                  radius: typing.Optional[typing.Any] = 1,
                  gesture_mode: typing.Optional[typing.Any] = 0):
    ''' Select UV vertices using circle selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param x: X
    :type x: typing.Optional[typing.Any]
    :param y: Y
    :type y: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param gesture_mode: Gesture Mode
    :type gesture_mode: typing.Optional[typing.Any]
    '''

    pass


def cube_project(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 cube_size: typing.Optional[typing.Any] = 1.0,
                 correct_aspect: typing.Union[bool, typing.Any] = True,
                 clip_to_bounds: typing.Union[bool, typing.Any] = False,
                 scale_to_bounds: typing.Union[bool, typing.Any] = False):
    ''' Project the UV vertices of the mesh over the six faces of a cube

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param cube_size: Cube Size, Size of the cube to project on
    :type cube_size: typing.Optional[typing.Any]
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: typing.Union[bool, typing.Any]
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: typing.Union[bool, typing.Any]
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: typing.Union[bool, typing.Any]
    '''

    pass


def cursor_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               location: typing.Optional[typing.Any] = (0.0, 0.0)):
    ''' Set 2D cursor location

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param location: Location, Cursor location in normalized (0.0-1.0) coordinates
    :type location: typing.Optional[typing.Any]
    '''

    pass


def cylinder_project(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        direction: typing.Optional[typing.Any] = 'VIEW_ON_EQUATOR',
        align: typing.Optional[typing.Any] = 'POLAR_ZX',
        radius: typing.Optional[typing.Any] = 1.0,
        correct_aspect: typing.Union[bool, typing.Any] = True,
        clip_to_bounds: typing.Union[bool, typing.Any] = False,
        scale_to_bounds: typing.Union[bool, typing.Any] = False):
    ''' Project the UV vertices of the mesh over the curved wall of a cylinder

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction of the sphere or cylinder * ``VIEW_ON_EQUATOR`` View on Equator, 3D view is on the equator. * ``VIEW_ON_POLES`` View on Poles, 3D view is on the poles. * ``ALIGN_TO_OBJECT`` Align to Object, Align according to object transform.
    :type direction: typing.Optional[typing.Any]
    :param align: Align, How to determine rotation around the pole * ``POLAR_ZX`` Polar ZX, Polar 0 is X. * ``POLAR_ZY`` Polar ZY, Polar 0 is Y.
    :type align: typing.Optional[typing.Any]
    :param radius: Radius, Radius of the sphere or cylinder
    :type radius: typing.Optional[typing.Any]
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: typing.Union[bool, typing.Any]
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: typing.Union[bool, typing.Any]
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: typing.Union[bool, typing.Any]
    '''

    pass


def export_layout(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  filepath: typing.Union[str, typing.Any] = "",
                  check_existing: typing.Union[bool, typing.Any] = True,
                  export_all: typing.Union[bool, typing.Any] = False,
                  modified: typing.Union[bool, typing.Any] = False,
                  mode: typing.Optional[typing.Any] = 'PNG',
                  size: typing.Optional[typing.Any] = (1024, 1024),
                  opacity: typing.Optional[typing.Any] = 0.25,
                  tessellated: typing.Union[bool, typing.Any] = False):
    ''' Export UV layout to file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param export_all: All UVs, Export all UVs in this mesh (not just visible ones)
    :type export_all: typing.Union[bool, typing.Any]
    :param modified: Modified, Exports UVs from the modified mesh
    :type modified: typing.Union[bool, typing.Any]
    :param mode: Format, File format to export the UV layout to * ``SVG`` Scalable Vector Graphic (.svg), Export the UV layout to a vector SVG file. * ``EPS`` Encapsulate PostScript (.eps), Export the UV layout to a vector EPS file. * ``PNG`` PNG Image (.png), Export the UV layout to a bitmap image.
    :type mode: typing.Optional[typing.Any]
    :param size: size, Dimensions of the exported file
    :type size: typing.Optional[typing.Any]
    :param opacity: Fill Opacity, Set amount of opacity for exported UV layout
    :type opacity: typing.Optional[typing.Any]
    :param tessellated: Tessellated UVs, Export tessellated UVs instead of polygons ones
    :type tessellated: typing.Union[bool, typing.Any]
    '''

    pass


def follow_active_quads(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        mode: typing.Optional[typing.Any] = 'LENGTH_AVERAGE'):
    ''' Follow UVs from active quads along continuous face loops

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Edge Length Mode, Method to space UV edge loops * ``EVEN`` Even, Space all UVs evenly. * ``LENGTH`` Length, Average space UVs edge length of each loop. * ``LENGTH_AVERAGE`` Length Average, Average space UVs edge length of each loop.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def hide(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Union[bool, typing.Any] = False):
    ''' Hide (un)selected UV vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: typing.Union[bool, typing.Any]
    '''

    pass


def lightmap_pack(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  PREF_CONTEXT: typing.Optional[typing.Any] = 'SEL_FACES',
                  PREF_PACK_IN_ONE: typing.Union[bool, typing.Any] = True,
                  PREF_NEW_UVLAYER: typing.Union[bool, typing.Any] = False,
                  PREF_APPLY_IMAGE: typing.Union[bool, typing.Any] = False,
                  PREF_IMG_PX_SIZE: typing.Optional[typing.Any] = 512,
                  PREF_BOX_DIV: typing.Optional[typing.Any] = 12,
                  PREF_MARGIN_DIV: typing.Optional[typing.Any] = 0.1):
    ''' Pack each faces UV's into the UV bounds

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param PREF_CONTEXT: Selection * ``SEL_FACES`` Selected Faces, Space all UVs evenly. * ``ALL_FACES`` All Faces, Average space UVs edge length of each loop. * ``ALL_OBJECTS`` Selected Mesh Object, Average space UVs edge length of each loop.
    :type PREF_CONTEXT: typing.Optional[typing.Any]
    :param PREF_PACK_IN_ONE: Share Tex Space, Objects Share texture space, map all objects into 1 uvmap
    :type PREF_PACK_IN_ONE: typing.Union[bool, typing.Any]
    :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed
    :type PREF_NEW_UVLAYER: typing.Union[bool, typing.Any]
    :param PREF_APPLY_IMAGE: New Image, Assign new images for every mesh (only one if shared tex space enabled)
    :type PREF_APPLY_IMAGE: typing.Union[bool, typing.Any]
    :param PREF_IMG_PX_SIZE: Image Size, Width and Height for the new image
    :type PREF_IMG_PX_SIZE: typing.Optional[typing.Any]
    :param PREF_BOX_DIV: Pack Quality, Pre Packing before the complex boxpack
    :type PREF_BOX_DIV: typing.Optional[typing.Any]
    :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV
    :type PREF_MARGIN_DIV: typing.Optional[typing.Any]
    '''

    pass


def mark_seam(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              clear: typing.Union[bool, typing.Any] = False):
    ''' Mark selected UV edges as seams

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param clear: Clear Seams, Clear instead of marking seams
    :type clear: typing.Union[bool, typing.Any]
    '''

    pass


def minimize_stretch(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     fill_holes: typing.Union[bool, typing.Any] = True,
                     blend: typing.Optional[typing.Any] = 0.0,
                     iterations: typing.Optional[typing.Any] = 0):
    ''' Reduce UV stretching by relaxing angles

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param fill_holes: Fill Holes, Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
    :type fill_holes: typing.Union[bool, typing.Any]
    :param blend: Blend, Blend factor between stretch minimized and original
    :type blend: typing.Optional[typing.Any]
    :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively
    :type iterations: typing.Optional[typing.Any]
    '''

    pass


def pack_islands(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 rotate: typing.Union[bool, typing.Any] = True,
                 margin: typing.Optional[typing.Any] = 0.001):
    ''' Transform all islands so that they fill up the UV space as much as possible

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param rotate: Rotate, Rotate islands for best fit
    :type rotate: typing.Union[bool, typing.Any]
    :param margin: Margin, Space between islands
    :type margin: typing.Optional[typing.Any]
    '''

    pass


def pin(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        clear: typing.Union[bool, typing.Any] = False):
    ''' Set/clear selected UV vertices as anchored between multiple unwrap operations

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param clear: Clear, Clear pinning for the selection instead of setting it
    :type clear: typing.Union[bool, typing.Any]
    '''

    pass


def project_from_view(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      orthographic: typing.Union[bool, typing.Any] = False,
                      camera_bounds: typing.Union[bool, typing.Any] = True,
                      correct_aspect: typing.Union[bool, typing.Any] = True,
                      clip_to_bounds: typing.Union[bool, typing.Any] = False,
                      scale_to_bounds: typing.Union[bool, typing.Any] = False):
    ''' Project the UV vertices of the mesh as seen in current 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param orthographic: Orthographic, Use orthographic projection
    :type orthographic: typing.Union[bool, typing.Any]
    :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account
    :type camera_bounds: typing.Union[bool, typing.Any]
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: typing.Union[bool, typing.Any]
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: typing.Union[bool, typing.Any]
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: typing.Union[bool, typing.Any]
    '''

    pass


def remove_doubles(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   threshold: typing.Optional[typing.Any] = 0.02,
                   use_unselected: typing.Union[bool, typing.Any] = False):
    ''' Selected UV vertices that are within a radius of each other are welded together

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param threshold: Merge Distance, Maximum distance between welded vertices
    :type threshold: typing.Optional[typing.Any]
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: typing.Union[bool, typing.Any]
    '''

    pass


def reset(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: typing.Optional[bool] = None):
    ''' Reset UV projection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def reveal(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None):
    ''' Reveal all hidden UV vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def seams_from_islands(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       mark_seams: typing.Union[bool, typing.Any] = True,
                       mark_sharp: typing.Union[bool, typing.Any] = False):
    ''' Set mesh seams according to island setup in the UV editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mark_seams: Mark Seams, Mark boundary edges as seams
    :type mark_seams: typing.Union[bool, typing.Any]
    :param mark_sharp: Mark Sharp, Mark boundary edges as sharp
    :type mark_sharp: typing.Union[bool, typing.Any]
    '''

    pass


def select(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           extend: typing.Union[bool, typing.Any] = False,
           location: typing.Optional[typing.Any] = (0.0, 0.0)):
    ''' Select UV vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: typing.Union[bool, typing.Any]
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: typing.Optional[typing.Any]
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection of all UV vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle, Toggle selection for all elements. * ``SELECT`` Select, Select all elements. * ``DESELECT`` Deselect, Deselect all elements. * ``INVERT`` Invert, Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_border(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  pinned: typing.Union[bool, typing.Any] = False,
                  gesture_mode: typing.Optional[typing.Any] = 0,
                  xmin: typing.Optional[typing.Any] = 0,
                  xmax: typing.Optional[typing.Any] = 0,
                  ymin: typing.Optional[typing.Any] = 0,
                  ymax: typing.Optional[typing.Any] = 0,
                  extend: typing.Union[bool, typing.Any] = True):
    ''' Select UV vertices using border selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param pinned: Pinned, Border select pinned UVs only
    :type pinned: typing.Union[bool, typing.Any]
    :param gesture_mode: Gesture Mode
    :type gesture_mode: typing.Optional[typing.Any]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_lasso(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 path: typing.Optional[bpy.types.bpy_prop_collection[
                     'bpy.types.OperatorMousePath']] = None,
                 deselect: typing.Union[bool, typing.Any] = False,
                 extend: typing.Union[bool, typing.Any] = True):
    ''' Select UVs using lasso selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param path: Path
    :type path: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']]
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: typing.Union[bool, typing.Any]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Deselect UV vertices at the boundary of each selection region

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
                  extend: typing.Union[bool, typing.Any] = False):
    ''' Select all UV vertices linked to the active UV map

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_linked_pick(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       extend: typing.Union[bool, typing.Any] = False,
                       location: typing.Optional[typing.Any] = (0.0, 0.0)):
    ''' Select all UV vertices linked under the mouse

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: typing.Union[bool, typing.Any]
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: typing.Optional[typing.Any]
    '''

    pass


def select_loop(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                extend: typing.Union[bool, typing.Any] = False,
                location: typing.Optional[typing.Any] = (0.0, 0.0)):
    ''' Select a loop of connected UV vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: typing.Union[bool, typing.Any]
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: typing.Optional[typing.Any]
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Select more UV vertices connected to initial selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_pinned(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Select all pinned UV vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_split(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Select only entirely selected faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def smart_project(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  angle_limit: typing.Optional[typing.Any] = 66.0,
                  island_margin: typing.Optional[typing.Any] = 0.0,
                  user_area_weight: typing.Optional[typing.Any] = 0.0,
                  use_aspect: typing.Union[bool, typing.Any] = True,
                  stretch_to_bounds: typing.Union[bool, typing.Any] = True):
    ''' This script projection unwraps the selected faces of a mesh (it operates on all selected mesh objects, and can be used to unwrap selected faces, or all faces)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion
    :type angle_limit: typing.Optional[typing.Any]
    :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands
    :type island_margin: typing.Optional[typing.Any]
    :param user_area_weight: Area Weight, Weight projections vector by faces with larger areas
    :type user_area_weight: typing.Optional[typing.Any]
    :param use_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type use_aspect: typing.Union[bool, typing.Any]
    :param stretch_to_bounds: Stretch to UV Bounds, Stretch the final output to texture bounds
    :type stretch_to_bounds: typing.Union[bool, typing.Any]
    '''

    pass


def snap_cursor(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                target: typing.Optional[typing.Any] = 'PIXELS'):
    ''' Snap cursor to target type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param target: Target, Target to snap the selected UVs to
    :type target: typing.Optional[typing.Any]
    '''

    pass


def snap_selected(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  target: typing.Optional[typing.Any] = 'PIXELS'):
    ''' Snap selected UV vertices to target type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param target: Target, Target to snap the selected UVs to
    :type target: typing.Optional[typing.Any]
    '''

    pass


def sphere_project(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   direction: typing.Optional[typing.Any] = 'VIEW_ON_EQUATOR',
                   align: typing.Optional[typing.Any] = 'POLAR_ZX',
                   correct_aspect: typing.Union[bool, typing.Any] = True,
                   clip_to_bounds: typing.Union[bool, typing.Any] = False,
                   scale_to_bounds: typing.Union[bool, typing.Any] = False):
    ''' Project the UV vertices of the mesh over the curved surface of a sphere

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction, Direction of the sphere or cylinder * ``VIEW_ON_EQUATOR`` View on Equator, 3D view is on the equator. * ``VIEW_ON_POLES`` View on Poles, 3D view is on the poles. * ``ALIGN_TO_OBJECT`` Align to Object, Align according to object transform.
    :type direction: typing.Optional[typing.Any]
    :param align: Align, How to determine rotation around the pole * ``POLAR_ZX`` Polar ZX, Polar 0 is X. * ``POLAR_ZY`` Polar ZY, Polar 0 is Y.
    :type align: typing.Optional[typing.Any]
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: typing.Union[bool, typing.Any]
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: typing.Union[bool, typing.Any]
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: typing.Union[bool, typing.Any]
    '''

    pass


def stitch(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           use_limit: typing.Union[bool, typing.Any] = False,
           snap_islands: typing.Union[bool, typing.Any] = True,
           limit: typing.Optional[typing.Any] = 0.01,
           static_island: typing.Optional[typing.Any] = 0,
           midpoint_snap: typing.Union[bool, typing.Any] = False,
           clear_seams: typing.Union[bool, typing.Any] = True,
           mode: typing.Optional[typing.Any] = 'VERTEX',
           stored_mode: typing.Optional[typing.Any] = 'VERTEX',
           selection: typing.Optional[bpy.types.bpy_prop_collection[
               'bpy.types.SelectedUvElement']] = None):
    ''' Stitch selected UV vertices by proximity

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_limit: Use Limit, Stitch UVs within a specified limit distance
    :type use_limit: typing.Union[bool, typing.Any]
    :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too)
    :type snap_islands: typing.Union[bool, typing.Any]
    :param limit: Limit, Limit distance in normalized coordinates
    :type limit: typing.Optional[typing.Any]
    :param static_island: Static Island, Island that stays in place when stitching islands
    :type static_island: typing.Optional[typing.Any]
    :param midpoint_snap: Snap At Midpoint, UVs are stitched at midpoint instead of at static island
    :type midpoint_snap: typing.Union[bool, typing.Any]
    :param clear_seams: Clear Seams, Clear seams of stitched edges
    :type clear_seams: typing.Union[bool, typing.Any]
    :param mode: Operation Mode, Use vertex or edge stitching
    :type mode: typing.Optional[typing.Any]
    :param stored_mode: Stored Operation Mode, Use vertex or edge stitching
    :type stored_mode: typing.Optional[typing.Any]
    :param selection: Selection
    :type selection: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.SelectedUvElement']]
    '''

    pass


def tile_set(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             tile: typing.Optional[typing.Any] = (0, 0)):
    ''' Set UV image tile coordinates

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param tile: Tile, Tile coordinate
    :type tile: typing.Optional[typing.Any]
    '''

    pass


def unwrap(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           method: typing.Optional[typing.Any] = 'ANGLE_BASED',
           fill_holes: typing.Union[bool, typing.Any] = True,
           correct_aspect: typing.Union[bool, typing.Any] = True,
           use_subsurf_data: typing.Union[bool, typing.Any] = False,
           margin: typing.Optional[typing.Any] = 0.001):
    ''' Unwrap the mesh of the object being edited

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)
    :type method: typing.Optional[typing.Any]
    :param fill_holes: Fill Holes, Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
    :type fill_holes: typing.Union[bool, typing.Any]
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: typing.Union[bool, typing.Any]
    :param use_subsurf_data: Use Subsurf Modifier, Map UVs taking vertex position after Subdivision Surface modifier has been applied
    :type use_subsurf_data: typing.Union[bool, typing.Any]
    :param margin: Margin, Space between islands
    :type margin: typing.Optional[typing.Any]
    '''

    pass


def weld(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None):
    ''' Weld selected UV vertices together

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
