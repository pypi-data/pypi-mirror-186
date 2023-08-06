import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def active_frame_delete(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Delete the active frame for the active Grease Pencil Layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def active_frames_delete_all(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: typing.Optional[bool] = None):
    ''' Delete the active frame(s) of all editable Grease Pencil layers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def brush_add(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Add new Grease Pencil drawing brush for the active Grease Pencil datablock

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def brush_change(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 brush: typing.Union[str, int, typing.Any] = 'DEFAULT'):
    ''' Change active Grease Pencil drawing brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param brush: Grease Pencil Brush
    :type brush: typing.Union[str, int, typing.Any]
    '''

    pass


def brush_copy(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Copy current Grease Pencil drawing brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def brush_move(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               type: typing.Optional[typing.Any] = 'UP'):
    ''' Move the active Grease Pencil drawing brush up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def brush_paint(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                stroke: typing.Optional[bpy.types.bpy_prop_collection[
                    'bpy.types.OperatorStrokeElement']] = None,
                wait_for_input: typing.Union[bool, typing.Any] = True):
    ''' Apply tweaks to strokes by painting over the strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param wait_for_input: Wait for Input, Enter a mini 'sculpt-mode' if enabled, otherwise, exit after drawing a single stroke
    :type wait_for_input: typing.Union[bool, typing.Any]
    '''

    pass


def brush_presets_create(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Create a set of predefined Grease Pencil drawing brushes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def brush_remove(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Remove active Grease Pencil drawing brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def brush_select(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 index: typing.Optional[typing.Any] = 0):
    ''' Select a Grease Pencil drawing brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param index: Index, Index of Drawing Brush
    :type index: typing.Optional[typing.Any]
    '''

    pass


def convert(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: typing.Optional[bool] = None,
            *,
            type: typing.Optional[typing.Any] = 'PATH',
            use_normalize_weights: typing.Union[bool, typing.Any] = True,
            radius_multiplier: typing.Optional[typing.Any] = 1.0,
            use_link_strokes: typing.Union[bool, typing.Any] = True,
            timing_mode: typing.Optional[typing.Any] = 'FULL',
            frame_range: typing.Optional[typing.Any] = 100,
            start_frame: typing.Optional[typing.Any] = 1,
            use_realtime: typing.Union[bool, typing.Any] = False,
            end_frame: typing.Optional[typing.Any] = 250,
            gap_duration: typing.Optional[typing.Any] = 0.0,
            gap_randomness: typing.Optional[typing.Any] = 0.0,
            seed: typing.Optional[typing.Any] = 0,
            use_timing_data: typing.Union[bool, typing.Any] = False):
    ''' Convert the active Grease Pencil layer to a new Curve Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Which type of curve to convert to * ``PATH`` Path, Animation path. * ``CURVE`` Bezier Curve, Smooth Bezier curve. * ``POLY`` Polygon Curve, Bezier curve with straight-line segments (vector handles).
    :type type: typing.Optional[typing.Any]
    :param use_normalize_weights: Normalize Weight, Normalize weight (set from stroke width)
    :type use_normalize_weights: typing.Union[bool, typing.Any]
    :param radius_multiplier: Radius Fac, Multiplier for the points' radii (set from stroke width)
    :type radius_multiplier: typing.Optional[typing.Any]
    :param use_link_strokes: Link Strokes, Whether to link strokes with zero-radius sections of curves
    :type use_link_strokes: typing.Union[bool, typing.Any]
    :param timing_mode: Timing Mode, How to use timing data stored in strokes * ``NONE`` No Timing, Ignore timing. * ``LINEAR`` Linear, Simple linear timing. * ``FULL`` Original, Use the original timing, gaps included. * ``CUSTOMGAP`` Custom Gaps, Use the original timing, but with custom gap lengths (in frames).
    :type timing_mode: typing.Optional[typing.Any]
    :param frame_range: Frame Range, The duration of evaluation of the path control curve
    :type frame_range: typing.Optional[typing.Any]
    :param start_frame: Start Frame, The start frame of the path control curve
    :type start_frame: typing.Optional[typing.Any]
    :param use_realtime: Realtime, Whether the path control curve reproduces the drawing in realtime, starting from Start Frame
    :type use_realtime: typing.Union[bool, typing.Any]
    :param end_frame: End Frame, The end frame of the path control curve (if Realtime is not set)
    :type end_frame: typing.Optional[typing.Any]
    :param gap_duration: Gap Duration, Custom Gap mode: (Average) length of gaps, in frames (Note: Realtime value, will be scaled if Realtime is not set)
    :type gap_duration: typing.Optional[typing.Any]
    :param gap_randomness: Gap Randomness, Custom Gap mode: Number of frames that gap lengths can vary
    :type gap_randomness: typing.Optional[typing.Any]
    :param seed: Random Seed, Custom Gap mode: Random generator seed
    :type seed: typing.Optional[typing.Any]
    :param use_timing_data: Has Valid Timing, Whether the converted Grease Pencil layer has valid timing data (internal use)
    :type use_timing_data: typing.Union[bool, typing.Any]
    '''

    pass


def copy(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None):
    ''' Copy selected Grease Pencil points and strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def data_add(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Add new Grease Pencil datablock

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def data_unlink(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Unlink active Grease Pencil datablock

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           type: typing.Optional[typing.Any] = 'POINTS'):
    ''' Delete selected Grease Pencil strokes, vertices, or frames

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Method used for deleting Grease Pencil data * ``POINTS`` Points, Delete selected points and split strokes into segments. * ``STROKES`` Strokes, Delete selected strokes. * ``FRAME`` Frame, Delete active frame.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def dissolve(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Delete selected points without splitting strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def draw(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         mode: typing.Optional[typing.Any] = 'DRAW',
         stroke: typing.Optional[bpy.types.bpy_prop_collection[
             'bpy.types.OperatorStrokeElement']] = None,
         wait_for_input: typing.Union[bool, typing.Any] = True):
    ''' Make annotations on the active data

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Way to interpret mouse movements * ``DRAW`` Draw Freehand, Draw freehand stroke(s). * ``DRAW_STRAIGHT`` Draw Straight Lines, Draw straight line segment(s). * ``DRAW_POLY`` Draw Poly Line, Click to place endpoints of straight line segments (connected). * ``ERASER`` Eraser, Erase Grease Pencil strokes.
    :type mode: typing.Optional[typing.Any]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param wait_for_input: Wait for Input, Wait for first click instead of painting immediately
    :type wait_for_input: typing.Union[bool, typing.Any]
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Duplicate the selected Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def duplicate_move(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   GPENCIL_OT_duplicate: typing.Optional['duplicate'] = None,
                   TRANSFORM_OT_translate: typing.
                   Optional['bpy.ops.transform.translate'] = None):
    ''' Make copies of the selected Grease Pencil strokes and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param GPENCIL_OT_duplicate: Duplicate Strokes, Duplicate the selected Grease Pencil strokes
    :type GPENCIL_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def editmode_toggle(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Enter/Exit edit mode for Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def hide(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Union[bool, typing.Any] = False):
    ''' Hide selected/unselected Grease Pencil layers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected layers
    :type unselected: typing.Union[bool, typing.Any]
    '''

    pass


def layer_add(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Add new Grease Pencil layer for the active Grease Pencil datablock

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_change(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 layer: typing.Union[str, int, typing.Any] = 'DEFAULT'):
    ''' Change active Grease Pencil layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param layer: Grease Pencil Layer
    :type layer: typing.Union[str, int, typing.Any]
    '''

    pass


def layer_duplicate(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Make a copy of the active Grease Pencil layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_isolate(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  affect_visibility: typing.Union[bool, typing.Any] = False):
    ''' Toggle whether the active layer is the only one that can be edited and/or visible

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility
    :type affect_visibility: typing.Union[bool, typing.Any]
    '''

    pass


def layer_merge(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Merge the current layer with the layer below

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_move(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               type: typing.Optional[typing.Any] = 'UP'):
    ''' Move the active Grease Pencil layer up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def layer_remove(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Remove active Grease Pencil layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def lock_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Lock all Grease Pencil layers to prevent them from being accidentally modified

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def move_to_layer(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  layer: typing.Union[str, int, typing.Any] = 'DEFAULT'):
    ''' Move selected strokes to another layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param layer: Grease Pencil Layer
    :type layer: typing.Union[str, int, typing.Any]
    '''

    pass


def palette_add(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Add new Grease Pencil palette for the active Grease Pencil datablock

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def palette_change(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   palette: typing.Union[str, int, typing.Any] = 'DEFAULT'):
    ''' Change active Grease Pencil palette

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param palette: Grease Pencil Palette
    :type palette: typing.Union[str, int, typing.Any]
    '''

    pass


def palette_lock_layer(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None):
    ''' Lock and hide any color not used in any layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def palette_remove(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Remove active Grease Pencil palette

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def palettecolor_add(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Add new Grease Pencil palette color for the active Grease Pencil datablock

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def palettecolor_copy(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Copy current Grease Pencil palette color

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def palettecolor_hide(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      unselected: typing.Union[bool, typing.Any] = False):
    ''' Hide selected/unselected Grease Pencil colors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected colors
    :type unselected: typing.Union[bool, typing.Any]
    '''

    pass


def palettecolor_isolate(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        affect_visibility: typing.Union[bool, typing.Any] = False):
    ''' Toggle whether the active color is the only one that is editable and/or visible

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility
    :type affect_visibility: typing.Union[bool, typing.Any]
    '''

    pass


def palettecolor_lock_all(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None):
    ''' Lock all Grease Pencil colors to prevent them from being accidentally modified

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def palettecolor_move(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move the active Grease Pencil palette color up/down in the list

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def palettecolor_remove(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Remove active Grease Pencil palette color

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def palettecolor_reveal(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Unhide all hidden Grease Pencil palette colors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def palettecolor_select(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Select all Grease Pencil strokes using current color

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def palettecolor_unlock_all(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None):
    ''' Unlock all Grease Pencil colors so that they can be edited

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def paste(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: typing.Optional[bool] = None,
          *,
          type: typing.Optional[typing.Any] = 'COPY'):
    ''' Paste previously copied strokes or copy and merge in active layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def reproject(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Reproject the selected strokes from the current viewpoint to get all points on the same plane again (e.g. to fix problems from accidental 3D cursor movement, or viewport changes)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def reveal(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None):
    ''' Show all Grease Pencil layers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           extend: typing.Union[bool, typing.Any] = False,
           deselect: typing.Union[bool, typing.Any] = False,
           toggle: typing.Union[bool, typing.Any] = False,
           entire_strokes: typing.Union[bool, typing.Any] = False,
           location: typing.Optional[typing.Any] = (0, 0)):
    ''' Select Grease Pencil strokes and/or stroke points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    :param deselect: Deselect, Remove from selection
    :type deselect: typing.Union[bool, typing.Any]
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: typing.Union[bool, typing.Any]
    :param entire_strokes: Entire Strokes, Select entire strokes instead of just the nearest stroke vertex
    :type entire_strokes: typing.Union[bool, typing.Any]
    :param location: Location, Mouse location
    :type location: typing.Optional[typing.Any]
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection of all Grease Pencil strokes currently visible

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
                  gesture_mode: typing.Optional[typing.Any] = 0,
                  xmin: typing.Optional[typing.Any] = 0,
                  xmax: typing.Optional[typing.Any] = 0,
                  ymin: typing.Optional[typing.Any] = 0,
                  ymax: typing.Optional[typing.Any] = 0,
                  extend: typing.Union[bool, typing.Any] = True):
    ''' Select Grease Pencil strokes within a rectangular region

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
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_circle(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  x: typing.Optional[typing.Any] = 0,
                  y: typing.Optional[typing.Any] = 0,
                  radius: typing.Optional[typing.Any] = 1,
                  gesture_mode: typing.Optional[typing.Any] = 0):
    ''' Select Grease Pencil strokes using brush selection

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


def select_first(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 only_selected_strokes: typing.Union[bool, typing.Any] = False,
                 extend: typing.Union[bool, typing.Any] = False):
    ''' Select first point in Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param only_selected_strokes: Selected Strokes Only, Only select the first point of strokes that already have points selected
    :type only_selected_strokes: typing.Union[bool, typing.Any]
    :param extend: Extend, Extend selection instead of deselecting all other selected points
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_grouped(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   type: typing.Optional[typing.Any] = 'LAYER'):
    ''' Select all strokes with similar characteristics

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type * ``LAYER`` Layer, Shared layers. * ``COLOR`` Color, Shared colors.
    :type type: typing.Optional[typing.Any]
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
    ''' Select Grease Pencil strokes using lasso selection

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


def select_last(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                only_selected_strokes: typing.Union[bool, typing.Any] = False,
                extend: typing.Union[bool, typing.Any] = False):
    ''' Select last point in Grease Pencil strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param only_selected_strokes: Selected Strokes Only, Only select the last point of strokes that already have points selected
    :type only_selected_strokes: typing.Union[bool, typing.Any]
    :param extend: Extend, Extend selection instead of deselecting all other selected points
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Shrink sets of selected Grease Pencil points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Select all points in same strokes as already selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Grow sets of selected Grease Pencil points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def selection_opacity_toggle(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: typing.Optional[bool] = None):
    ''' Hide/Unhide selected points for Grease Pencil strokes setting alpha factor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def snap_cursor_to_selected(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None):
    ''' Snap cursor to center of selected points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def snap_to_cursor(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   use_offset: typing.Union[bool, typing.Any] = True):
    ''' Snap selected points/strokes to the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_offset: With Offset, Offset the entire stroke instead of selected points only
    :type use_offset: typing.Union[bool, typing.Any]
    '''

    pass


def snap_to_grid(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Snap selected points to the nearest grid points

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def stroke_apply_thickness(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: typing.Optional[bool] = None):
    ''' Apply the thickness change of the layer to its strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def stroke_arrange(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   direction: typing.Optional[typing.Any] = 'UP'):
    ''' Arrange selected strokes up/down in the drawing order of the active layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param direction: Direction
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def stroke_change_color(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Move selected strokes to active color

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def stroke_cyclical_set(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        type: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Close or open the selected stroke adding an edge from last to first point

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def stroke_flip(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Change direction of the points of the selected strokes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def stroke_join(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                type: typing.Optional[typing.Any] = 'JOIN',
                leave_gaps: typing.Union[bool, typing.Any] = False):
    ''' Join selected strokes (optionally as new stroke)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param leave_gaps: Leave Gaps, Leave gaps between joined strokes instead of linking them
    :type leave_gaps: typing.Union[bool, typing.Any]
    '''

    pass


def stroke_lock_color(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Lock any color not used in any selected stroke

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def unlock_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Unlock all Grease Pencil layers so that they can be edited

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
