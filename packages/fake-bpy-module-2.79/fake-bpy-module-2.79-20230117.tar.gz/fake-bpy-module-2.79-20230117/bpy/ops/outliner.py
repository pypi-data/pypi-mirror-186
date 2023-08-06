import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def action_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               action: typing.Union[str, int, typing.Any] = ''):
    ''' Change the active action used

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action
    :type action: typing.Union[str, int, typing.Any]
    '''

    pass


def animdata_operation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       type: typing.Optional[typing.Any] = 'CLEAR_ANIMDATA'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Animation Operation * ``CLEAR_ANIMDATA`` Clear Animation Data, Remove this animation data container. * ``SET_ACT`` Set Action. * ``CLEAR_ACT`` Unlink Action. * ``REFRESH_DRIVERS`` Refresh Drivers. * ``CLEAR_DRIVERS`` Clear Drivers.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def constraint_operation(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None,
                         *,
                         type: typing.Optional[typing.Any] = 'ENABLE'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Constraint Operation
    :type type: typing.Optional[typing.Any]
    '''

    pass


def data_operation(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   type: typing.Optional[typing.Any] = 'SELECT'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Data Operation
    :type type: typing.Optional[typing.Any]
    '''

    pass


def drivers_add_selected(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Add drivers to selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def drivers_delete_selected(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None):
    ''' Delete drivers assigned to selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def expanded_toggle(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Expand/Collapse all items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def group_link(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               object: typing.Union[str, typing.Any] = "Object"):
    ''' Link Object to Group in Outliner

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param object: Object, Target Object
    :type object: typing.Union[str, typing.Any]
    '''

    pass


def group_operation(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    type: typing.Optional[typing.Any] = 'UNLINK'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Group Operation * ``UNLINK`` Unlink Group. * ``LOCAL`` Make Local Group. * ``LINK`` Link Group Objects to Scene. * ``DELETE`` Delete Group. * ``REMAP`` Remap Users, Make all users of selected data-blocks to use instead current (clicked) one. * ``INSTANCE`` Instance Groups in Scene. * ``TOGVIS`` Toggle Visible Group. * ``TOGSEL`` Toggle Selectable. * ``TOGREN`` Toggle Renderable. * ``RENAME`` Rename.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def id_delete(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Delete the ID under cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def id_operation(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 type: typing.Optional[typing.Any] = 'UNLINK'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: ID data Operation * ``UNLINK`` Unlink. * ``LOCAL`` Make Local. * ``SINGLE`` Make Single User. * ``DELETE`` Delete, WARNING: no undo. * ``REMAP`` Remap Users, Make all users of selected data-blocks to use instead current (clicked) one. * ``ADD_FAKE`` Add Fake User, Ensure data-block gets saved even if it isn't in use (e.g. for motion and material libraries). * ``CLEAR_FAKE`` Clear Fake User. * ``RENAME`` Rename. * ``SELECT_LINKED`` Select Linked.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def id_remap(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             id_type: typing.Optional[typing.Any] = 'OBJECT',
             old_id: typing.Union[str, int, typing.Any] = '',
             new_id: typing.Union[str, int, typing.Any] = ''):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param id_type: ID Type
    :type id_type: typing.Optional[typing.Any]
    :param old_id: Old ID, Old ID to replace
    :type old_id: typing.Union[str, int, typing.Any]
    :param new_id: New ID, New ID to remap all selected IDs' users to
    :type new_id: typing.Union[str, int, typing.Any]
    '''

    pass


def item_activate(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  extend: typing.Union[bool, typing.Any] = True,
                  recursive: typing.Union[bool, typing.Any] = False):
    ''' Handle mouse clicks to activate/select items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection for activation
    :type extend: typing.Union[bool, typing.Any]
    :param recursive: Recursive, Select Objects and their children
    :type recursive: typing.Union[bool, typing.Any]
    '''

    pass


def item_openclose(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   all: typing.Union[bool, typing.Any] = True):
    ''' Toggle whether item under cursor is enabled or closed

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param all: All, Close or open all items
    :type all: typing.Union[bool, typing.Any]
    '''

    pass


def item_rename(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Rename item under cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def keyingset_add_selected(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: typing.Optional[bool] = None):
    ''' Add selected items (blue-gray rows) to active Keying Set

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def keyingset_remove_selected(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: typing.Optional[bool] = None):
    ''' Remove selected items (blue-gray rows) from active Keying Set

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def lib_operation(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  type: typing.Optional[typing.Any] = 'RENAME'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Library Operation * ``RENAME`` Rename. * ``DELETE`` Delete, Delete this library and all its item from Blender - WARNING: no undo. * ``RELOCATE`` Relocate, Select a new path for this library, and reload all its data. * ``RELOAD`` Reload, Reload all data from this library.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def lib_relocate(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Relocate the library under cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def material_drop(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  object: typing.Union[str, typing.Any] = "Object",
                  material: typing.Union[str, typing.Any] = "Material"):
    ''' Drag material to object in Outliner

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param object: Object, Target Object
    :type object: typing.Union[str, typing.Any]
    :param material: Material, Target Material
    :type material: typing.Union[str, typing.Any]
    '''

    pass


def modifier_operation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       type: typing.Optional[typing.Any] = 'TOGVIS'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Modifier Operation
    :type type: typing.Optional[typing.Any]
    '''

    pass


def object_operation(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     type: typing.Optional[typing.Any] = 'SELECT'):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Object Operation * ``SELECT`` Select. * ``DESELECT`` Deselect. * ``SELECT_HIERARCHY`` Select Hierarchy. * ``DELETE`` Delete. * ``DELETE_HIERARCHY`` Delete Hierarchy. * ``REMAP`` Remap Users, Make all users of selected data-blocks to use instead a new chosen one. * ``TOGVIS`` Toggle Visible. * ``TOGSEL`` Toggle Selectable. * ``TOGREN`` Toggle Renderable. * ``RENAME`` Rename.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def operation(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Context menu for item operations

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def orphans_purge(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Clear all orphaned data-blocks without any users from the file (cannot be undone, saves to current .blend file)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def parent_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 dragged_obj: typing.Union[str, typing.Any] = "Object",
                 type: typing.Optional[typing.Any] = 'CLEAR'):
    ''' Drag to clear parent in Outliner

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param dragged_obj: Child, Child Object
    :type dragged_obj: typing.Union[str, typing.Any]
    :param type: Type * ``CLEAR`` Clear Parent, Completely clear the parenting relationship, including involved modifiers if any. * ``CLEAR_KEEP_TRANSFORM`` Clear and Keep Transformation, As 'Clear Parent', but keep the current visual transformations of the object. * ``CLEAR_INVERSE`` Clear Parent Inverse, Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def parent_drop(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                child: typing.Union[str, typing.Any] = "Object",
                parent: typing.Union[str, typing.Any] = "Object",
                type: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Drag to parent in Outliner

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param child: Child, Child Object
    :type child: typing.Union[str, typing.Any]
    :param parent: Parent, Parent Object
    :type parent: typing.Union[str, typing.Any]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def renderability_toggle(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Toggle the renderability of selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def scene_drop(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               object: typing.Union[str, typing.Any] = "Object",
               scene: typing.Union[str, typing.Any] = "Scene"):
    ''' Drag object to scene in Outliner

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param object: Object, Target Object
    :type object: typing.Union[str, typing.Any]
    :param scene: Scene, Target Scene
    :type scene: typing.Union[str, typing.Any]
    '''

    pass


def scene_operation(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    type: typing.Union[str, int, typing.Any] = 'DELETE'):
    ''' Context menu for scene operations

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Scene Operation
    :type type: typing.Union[str, int, typing.Any]
    '''

    pass


def scroll_page(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                up: typing.Union[bool, typing.Any] = False):
    ''' Scroll page up or down

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param up: Up, Scroll up one page
    :type up: typing.Union[bool, typing.Any]
    '''

    pass


def select_border(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  gesture_mode: typing.Optional[typing.Any] = 0,
                  xmin: typing.Optional[typing.Any] = 0,
                  xmax: typing.Optional[typing.Any] = 0,
                  ymin: typing.Optional[typing.Any] = 0,
                  ymax: typing.Optional[typing.Any] = 0):
    ''' Use box selection to select tree elements

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
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
    '''

    pass


def selectability_toggle(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Toggle the selectability

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def selected_toggle(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Toggle the Outliner selection of items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def show_active(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Open up the tree and adjust the view so that the active Object is shown centered

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def show_hierarchy(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Open all object entries and close all others

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def show_one_level(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   open: typing.Union[bool, typing.Any] = True):
    ''' Expand/collapse all entries by one level

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param open: Open, Expand all entries one level deep
    :type open: typing.Union[bool, typing.Any]
    '''

    pass


def visibility_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Toggle the visibility of selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
