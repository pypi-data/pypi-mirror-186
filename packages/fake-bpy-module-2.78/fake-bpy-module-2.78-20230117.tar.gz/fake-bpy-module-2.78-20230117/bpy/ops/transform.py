import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def bend(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         value: typing.Optional[typing.Any] = (0.0),
         mirror: typing.Union[bool, typing.Any] = False,
         proportional: typing.Optional[typing.Any] = 'DISABLED',
         proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
         proportional_size: typing.Optional[typing.Any] = 1.0,
         snap: typing.Union[bool, typing.Any] = False,
         snap_target: typing.Optional[typing.Any] = 'CLOSEST',
         snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
         snap_align: typing.Union[bool, typing.Any] = False,
         snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
         gpencil_strokes: typing.Union[bool, typing.Any] = False,
         release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Bend selected items between the 3D cursor and the mouse

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Angle
    :type value: typing.Optional[typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def create_orientation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       name: typing.Union[str, typing.Any] = "",
                       use_view: typing.Union[bool, typing.Any] = False,
                       use: typing.Union[bool, typing.Any] = False,
                       overwrite: typing.Union[bool, typing.Any] = False):
    ''' Create transformation orientation from selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the new custom orientation
    :type name: typing.Union[str, typing.Any]
    :param use_view: Use View, Use the current view instead of the active object to create the new orientation
    :type use_view: typing.Union[bool, typing.Any]
    :param use: Use after creation, Select orientation after its creation
    :type use: typing.Union[bool, typing.Any]
    :param overwrite: Overwrite previous, Overwrite previously created orientation with same name
    :type overwrite: typing.Union[bool, typing.Any]
    '''

    pass


def delete_orientation(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None):
    ''' Delete transformation orientation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def edge_bevelweight(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     value: typing.Optional[typing.Any] = 0.0,
                     snap: typing.Union[bool, typing.Any] = False,
                     snap_target: typing.Optional[typing.Any] = 'CLOSEST',
                     snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
                     snap_align: typing.Union[bool, typing.Any] = False,
                     snap_normal: typing.Optional[typing.Any] = (0.0, 0.0,
                                                                 0.0),
                     release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Change the bevel weight of edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Factor
    :type value: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def edge_crease(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                value: typing.Optional[typing.Any] = 0.0,
                snap: typing.Union[bool, typing.Any] = False,
                snap_target: typing.Optional[typing.Any] = 'CLOSEST',
                snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
                snap_align: typing.Union[bool, typing.Any] = False,
                snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
                release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Change the crease of edges

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Factor
    :type value: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def edge_slide(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               value: typing.Optional[typing.Any] = 0.0,
               single_side: typing.Union[bool, typing.Any] = False,
               use_even: typing.Union[bool, typing.Any] = False,
               flipped: typing.Union[bool, typing.Any] = False,
               use_clamp: typing.Union[bool, typing.Any] = True,
               mirror: typing.Union[bool, typing.Any] = False,
               snap: typing.Union[bool, typing.Any] = False,
               snap_target: typing.Optional[typing.Any] = 'CLOSEST',
               snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
               snap_align: typing.Union[bool, typing.Any] = False,
               snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
               correct_uv: typing.Union[bool, typing.Any] = False,
               release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Slide an edge loop along a mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Factor
    :type value: typing.Optional[typing.Any]
    :param single_side: Single Side
    :type single_side: typing.Union[bool, typing.Any]
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :type use_even: typing.Union[bool, typing.Any]
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :type flipped: typing.Union[bool, typing.Any]
    :param use_clamp: Clamp, Clamp within the edge extents
    :type use_clamp: typing.Union[bool, typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :type correct_uv: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def mirror(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint_axis: typing.Union[typing.List[bool], typing.Any] = (False,
                                                                        False,
                                                                        False),
        constraint_orientation: typing.Union[str, int, typing.Any] = 'GLOBAL',
        proportional: typing.Optional[typing.Any] = 'DISABLED',
        proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        gpencil_strokes: typing.Union[bool, typing.Any] = False,
        release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Mirror selected items around one or more axes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.Union[typing.List[bool], typing.Any]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def push_pull(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        value: typing.Optional[typing.Any] = 0.0,
        mirror: typing.Union[bool, typing.Any] = False,
        proportional: typing.Optional[typing.Any] = 'DISABLED',
        proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        snap: typing.Union[bool, typing.Any] = False,
        snap_target: typing.Optional[typing.Any] = 'CLOSEST',
        snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        snap_align: typing.Union[bool, typing.Any] = False,
        snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Push/Pull selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Distance
    :type value: typing.Optional[typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def resize(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        value: typing.Optional[typing.Any] = (1.0, 1.0, 1.0),
        constraint_axis: typing.Union[typing.List[bool], typing.Any] = (False,
                                                                        False,
                                                                        False),
        constraint_orientation: typing.Union[str, int, typing.Any] = 'GLOBAL',
        mirror: typing.Union[bool, typing.Any] = False,
        proportional: typing.Optional[typing.Any] = 'DISABLED',
        proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        snap: typing.Union[bool, typing.Any] = False,
        snap_target: typing.Optional[typing.Any] = 'CLOSEST',
        snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        snap_align: typing.Union[bool, typing.Any] = False,
        snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        gpencil_strokes: typing.Union[bool, typing.Any] = False,
        texture_space: typing.Union[bool, typing.Any] = False,
        remove_on_cancel: typing.Union[bool, typing.Any] = False,
        release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Scale (resize) selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Vector
    :type value: typing.Optional[typing.Any]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.Union[typing.List[bool], typing.Any]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int, typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: typing.Union[bool, typing.Any]
    :param texture_space: Edit Texture Space, Edit Object data texture space
    :type texture_space: typing.Union[bool, typing.Any]
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def rotate(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        value: typing.Optional[typing.Any] = 0.0,
        axis: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        constraint_axis: typing.Union[typing.List[bool], typing.Any] = (False,
                                                                        False,
                                                                        False),
        constraint_orientation: typing.Union[str, int, typing.Any] = 'GLOBAL',
        mirror: typing.Union[bool, typing.Any] = False,
        proportional: typing.Optional[typing.Any] = 'DISABLED',
        proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        snap: typing.Union[bool, typing.Any] = False,
        snap_target: typing.Optional[typing.Any] = 'CLOSEST',
        snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        snap_align: typing.Union[bool, typing.Any] = False,
        snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        gpencil_strokes: typing.Union[bool, typing.Any] = False,
        release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Rotate selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Angle
    :type value: typing.Optional[typing.Any]
    :param axis: Axis, The axis around which the transformation occurs
    :type axis: typing.Optional[typing.Any]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.Union[typing.List[bool], typing.Any]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int, typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def select_orientation(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        orientation: typing.Union[str, int, typing.Any] = 'GLOBAL'):
    ''' Select transformation orientation

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param orientation: Orientation, Transformation orientation
    :type orientation: typing.Union[str, int, typing.Any]
    '''

    pass


def seq_slide(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              value: typing.Optional[typing.Any] = (0.0, 0.0),
              snap: typing.Union[bool, typing.Any] = False,
              snap_target: typing.Optional[typing.Any] = 'CLOSEST',
              snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
              snap_align: typing.Union[bool, typing.Any] = False,
              snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
              release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Slide a sequence strip in time

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Vector
    :type value: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def shear(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: typing.Optional[bool] = None,
          *,
          value: typing.Optional[typing.Any] = 0.0,
          mirror: typing.Union[bool, typing.Any] = False,
          proportional: typing.Optional[typing.Any] = 'DISABLED',
          proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
          proportional_size: typing.Optional[typing.Any] = 1.0,
          snap: typing.Union[bool, typing.Any] = False,
          snap_target: typing.Optional[typing.Any] = 'CLOSEST',
          snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
          snap_align: typing.Union[bool, typing.Any] = False,
          snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
          gpencil_strokes: typing.Union[bool, typing.Any] = False,
          release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Shear selected items along the horizontal screen axis

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Offset
    :type value: typing.Optional[typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def shrink_fatten(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        value: typing.Optional[typing.Any] = 0.0,
        use_even_offset: typing.Union[bool, typing.Any] = True,
        mirror: typing.Union[bool, typing.Any] = False,
        proportional: typing.Optional[typing.Any] = 'DISABLED',
        proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        snap: typing.Union[bool, typing.Any] = False,
        snap_target: typing.Optional[typing.Any] = 'CLOSEST',
        snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        snap_align: typing.Union[bool, typing.Any] = False,
        snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Shrink/fatten selected vertices along normals

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Offset
    :type value: typing.Optional[typing.Any]
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: typing.Union[bool, typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def skin_resize(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        value: typing.Optional[typing.Any] = (1.0, 1.0, 1.0),
        constraint_axis: typing.Union[typing.List[bool], typing.Any] = (False,
                                                                        False,
                                                                        False),
        constraint_orientation: typing.Union[str, int, typing.Any] = 'GLOBAL',
        mirror: typing.Union[bool, typing.Any] = False,
        proportional: typing.Optional[typing.Any] = 'DISABLED',
        proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        snap: typing.Union[bool, typing.Any] = False,
        snap_target: typing.Optional[typing.Any] = 'CLOSEST',
        snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        snap_align: typing.Union[bool, typing.Any] = False,
        snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Scale selected vertices' skin radii

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Vector
    :type value: typing.Optional[typing.Any]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.Union[typing.List[bool], typing.Any]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int, typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def tilt(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         value: typing.Optional[typing.Any] = 0.0,
         mirror: typing.Union[bool, typing.Any] = False,
         proportional: typing.Optional[typing.Any] = 'DISABLED',
         proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
         proportional_size: typing.Optional[typing.Any] = 1.0,
         snap: typing.Union[bool, typing.Any] = False,
         snap_target: typing.Optional[typing.Any] = 'CLOSEST',
         snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
         snap_align: typing.Union[bool, typing.Any] = False,
         snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
         release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Tilt selected control vertices of 3D curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Angle
    :type value: typing.Optional[typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def tosphere(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             value: typing.Optional[typing.Any] = 0.0,
             mirror: typing.Union[bool, typing.Any] = False,
             proportional: typing.Optional[typing.Any] = 'DISABLED',
             proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
             proportional_size: typing.Optional[typing.Any] = 1.0,
             snap: typing.Union[bool, typing.Any] = False,
             snap_target: typing.Optional[typing.Any] = 'CLOSEST',
             snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
             snap_align: typing.Union[bool, typing.Any] = False,
             snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
             gpencil_strokes: typing.Union[bool, typing.Any] = False,
             release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Move selected vertices outward in a spherical shape around mesh center

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Factor
    :type value: typing.Optional[typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def trackball(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        value: typing.Optional[typing.Any] = (0.0, 0.0),
        mirror: typing.Union[bool, typing.Any] = False,
        proportional: typing.Optional[typing.Any] = 'DISABLED',
        proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        snap: typing.Union[bool, typing.Any] = False,
        snap_target: typing.Optional[typing.Any] = 'CLOSEST',
        snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        snap_align: typing.Union[bool, typing.Any] = False,
        snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        gpencil_strokes: typing.Union[bool, typing.Any] = False,
        release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Trackball style rotation of selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Angle
    :type value: typing.Optional[typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def transform(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'TRANSLATION',
        value: typing.Optional[typing.Any] = (0.0, 0.0, 0.0, 0.0),
        axis: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        constraint_axis: typing.Union[typing.List[bool], typing.Any] = (False,
                                                                        False,
                                                                        False),
        constraint_orientation: typing.Union[str, int, typing.Any] = 'GLOBAL',
        mirror: typing.Union[bool, typing.Any] = False,
        proportional: typing.Optional[typing.Any] = 'DISABLED',
        proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        snap: typing.Union[bool, typing.Any] = False,
        snap_target: typing.Optional[typing.Any] = 'CLOSEST',
        snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        snap_align: typing.Union[bool, typing.Any] = False,
        snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        gpencil_strokes: typing.Union[bool, typing.Any] = False,
        release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Transform selected items by mode type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param value: Values
    :type value: typing.Optional[typing.Any]
    :param axis: Axis, The axis around which the transformation occurs
    :type axis: typing.Optional[typing.Any]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.Union[typing.List[bool], typing.Any]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int, typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def translate(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        value: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        constraint_axis: typing.Union[typing.List[bool], typing.Any] = (False,
                                                                        False,
                                                                        False),
        constraint_orientation: typing.Union[str, int, typing.Any] = 'GLOBAL',
        mirror: typing.Union[bool, typing.Any] = False,
        proportional: typing.Optional[typing.Any] = 'DISABLED',
        proportional_edit_falloff: typing.Optional[typing.Any] = 'SMOOTH',
        proportional_size: typing.Optional[typing.Any] = 1.0,
        snap: typing.Union[bool, typing.Any] = False,
        snap_target: typing.Optional[typing.Any] = 'CLOSEST',
        snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        snap_align: typing.Union[bool, typing.Any] = False,
        snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
        gpencil_strokes: typing.Union[bool, typing.Any] = False,
        texture_space: typing.Union[bool, typing.Any] = False,
        remove_on_cancel: typing.Union[bool, typing.Any] = False,
        release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Translate (move) selected items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Vector
    :type value: typing.Optional[typing.Any]
    :param constraint_axis: Constraint Axis
    :type constraint_axis: typing.Union[typing.List[bool], typing.Any]
    :param constraint_orientation: Orientation, Transformation orientation
    :type constraint_orientation: typing.Union[str, int, typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param proportional: Proportional Editing * ``DISABLED`` Disable, Proportional Editing disabled. * ``ENABLED`` Enable, Proportional Editing enabled. * ``PROJECTED`` Projected (2D), Proportional Editing using screen space locations. * ``CONNECTED`` Connected, Proportional Editing using connected geometry only.
    :type proportional: typing.Optional[typing.Any]
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode * ``SMOOTH`` Smooth, Smooth falloff. * ``SPHERE`` Sphere, Spherical falloff. * ``ROOT`` Root, Root falloff. * ``INVERSE_SQUARE`` Inverse Square, Inverse Square falloff. * ``SHARP`` Sharp, Sharp falloff. * ``LINEAR`` Linear, Linear falloff. * ``CONSTANT`` Constant, Constant falloff. * ``RANDOM`` Random, Random falloff.
    :type proportional_edit_falloff: typing.Optional[typing.Any]
    :param proportional_size: Proportional Size
    :type proportional_size: typing.Optional[typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
    :type gpencil_strokes: typing.Union[bool, typing.Any]
    :param texture_space: Edit Texture Space, Edit Object data texture space
    :type texture_space: typing.Union[bool, typing.Any]
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
    :type remove_on_cancel: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def vert_slide(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               value: typing.Optional[typing.Any] = 0.0,
               use_even: typing.Union[bool, typing.Any] = False,
               flipped: typing.Union[bool, typing.Any] = False,
               use_clamp: typing.Union[bool, typing.Any] = True,
               mirror: typing.Union[bool, typing.Any] = False,
               snap: typing.Union[bool, typing.Any] = False,
               snap_target: typing.Optional[typing.Any] = 'CLOSEST',
               snap_point: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
               snap_align: typing.Union[bool, typing.Any] = False,
               snap_normal: typing.Optional[typing.Any] = (0.0, 0.0, 0.0),
               correct_uv: typing.Union[bool, typing.Any] = False,
               release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Slide a vertex along a mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param value: Factor
    :type value: typing.Optional[typing.Any]
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
    :type use_even: typing.Union[bool, typing.Any]
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
    :type flipped: typing.Union[bool, typing.Any]
    :param use_clamp: Clamp, Clamp within the edge extents
    :type use_clamp: typing.Union[bool, typing.Any]
    :param mirror: Mirror Editing
    :type mirror: typing.Union[bool, typing.Any]
    :param snap: Use Snapping Options
    :type snap: typing.Union[bool, typing.Any]
    :param snap_target: Target * ``CLOSEST`` Closest, Snap closest point onto target. * ``CENTER`` Center, Snap center onto target. * ``MEDIAN`` Median, Snap median onto target. * ``ACTIVE`` Active, Snap active onto target.
    :type snap_target: typing.Optional[typing.Any]
    :param snap_point: Point
    :type snap_point: typing.Optional[typing.Any]
    :param snap_align: Align with Point Normal
    :type snap_align: typing.Union[bool, typing.Any]
    :param snap_normal: Normal
    :type snap_normal: typing.Optional[typing.Any]
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
    :type correct_uv: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def vertex_random(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  offset: typing.Optional[typing.Any] = 0.1,
                  uniform: typing.Optional[typing.Any] = 0.0,
                  normal: typing.Optional[typing.Any] = 0.0,
                  seed: typing.Optional[typing.Any] = 0):
    ''' Randomize vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param offset: Amount, Distance to offset
    :type offset: typing.Optional[typing.Any]
    :param uniform: Uniform, Increase for uniform offset distance
    :type uniform: typing.Optional[typing.Any]
    :param normal: normal, Align offset direction to normals
    :type normal: typing.Optional[typing.Any]
    :param seed: Random Seed, Seed for the random number generator
    :type seed: typing.Optional[typing.Any]
    '''

    pass


def vertex_warp(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        warp_angle: typing.Optional[typing.Any] = 6.28319,
        offset_angle: typing.Optional[typing.Any] = 0.0,
        min: typing.Optional[typing.Any] = -1,
        max: typing.Optional[typing.Any] = 1.0,
        viewmat: typing.Optional[typing.Any] = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                0.0, 0.0, 0.0, 0.0),
        center: typing.Optional[typing.Any] = (0.0, 0.0, 0.0)):
    ''' Warp vertices around the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param warp_angle: Warp Angle, Amount to warp about the cursor
    :type warp_angle: typing.Optional[typing.Any]
    :param offset_angle: Offset Angle, Angle to use as the basis for warping
    :type offset_angle: typing.Optional[typing.Any]
    :param min: Min
    :type min: typing.Optional[typing.Any]
    :param max: Max
    :type max: typing.Optional[typing.Any]
    :param viewmat: Matrix
    :type viewmat: typing.Optional[typing.Any]
    :param center: Center
    :type center: typing.Optional[typing.Any]
    '''

    pass
