import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def brush_stroke(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        stroke: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        mode: typing.Optional[typing.Any] = 'NORMAL',
        ignore_background_click: typing.Union[bool, typing.Any] = False):
    ''' Sculpt a stroke into the geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param mode: Stroke Mode, Action taken when a paint stroke is made * ``NORMAL`` Normal, Apply brush normally. * ``INVERT`` Invert, Invert action of brush for duration of stroke. * ``SMOOTH`` Smooth, Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke
    :type ignore_background_click: typing.Union[bool, typing.Any]
    '''

    pass


def detail_flood_fill(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Flood fill the mesh with the selected detail setting

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def dynamic_topology_toggle(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None):
    ''' Dynamic topology alters the mesh topology while sculpting

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def optimize(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Recalculate the sculpt BVH to improve performance

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def sample_detail_size(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       location: typing.Optional[typing.Any] = (0, 0)):
    ''' Sample the mesh detail on clicked point

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param location: Location, Screen Coordinates of sampling
    :type location: typing.Optional[typing.Any]
    '''

    pass


def sculptmode_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Toggle sculpt mode in 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_detail_size(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Set the mesh detail (either relative or constant one, depending on current dyntopo mode)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_persistent_base(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Reset the copy of the mesh that is being sculpted on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def symmetrize(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Symmetrize the topology modifications

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def uv_sculpt_stroke(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     mode: typing.Optional[typing.Any] = 'NORMAL'):
    ''' Sculpt UVs using a brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Stroke Mode * ``NORMAL`` Normal, Apply brush normally. * ``INVERT`` Invert, Invert action of brush for duration of stroke. * ``RELAX`` Relax, Switch brush to relax mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    '''

    pass
