import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def childof_clear_inverse(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None,
                          *,
                          constraint: typing.Union[str, typing.Any] = "",
                          owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Clear inverse correction for ChildOf constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object, Edit a constraint on the active object. * ``BONE`` Bone, Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def childof_set_inverse(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        constraint: typing.Union[str, typing.Any] = "",
                        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Set inverse correction for ChildOf constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object, Edit a constraint on the active object. * ``BONE`` Bone, Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None):
    ''' Remove constraint from constraint stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def followpath_path_animate(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None,
                            *,
                            constraint: typing.Union[str, typing.Any] = "",
                            owner: typing.Optional[typing.Any] = 'OBJECT',
                            frame_start: typing.Optional[typing.Any] = 1,
                            length: typing.Optional[typing.Any] = 100):
    ''' Add default animation for path used by constraint if it isn't animated already

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object, Edit a constraint on the active object. * ``BONE`` Bone, Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    :param frame_start: Start Frame, First frame of path animation
    :type frame_start: typing.Optional[typing.Any]
    :param length: Length, Number of frames that path animation should take
    :type length: typing.Optional[typing.Any]
    '''

    pass


def limitdistance_reset(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        constraint: typing.Union[str, typing.Any] = "",
                        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Reset limiting distance for Limit Distance Constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object, Edit a constraint on the active object. * ``BONE`` Bone, Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def move_down(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              constraint: typing.Union[str, typing.Any] = "",
              owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Move constraint down in constraint stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object, Edit a constraint on the active object. * ``BONE`` Bone, Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def move_up(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: typing.Optional[bool] = None,
            *,
            constraint: typing.Union[str, typing.Any] = "",
            owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Move constraint up in constraint stack

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object, Edit a constraint on the active object. * ``BONE`` Bone, Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def objectsolver_clear_inverse(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        constraint: typing.Union[str, typing.Any] = "",
        owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Clear inverse correction for ObjectSolver constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object, Edit a constraint on the active object. * ``BONE`` Bone, Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def objectsolver_set_inverse(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: typing.Optional[bool] = None,
                             *,
                             constraint: typing.Union[str, typing.Any] = "",
                             owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Set inverse correction for ObjectSolver constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object, Edit a constraint on the active object. * ``BONE`` Bone, Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass


def stretchto_reset(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    constraint: typing.Union[str, typing.Any] = "",
                    owner: typing.Optional[typing.Any] = 'OBJECT'):
    ''' Reset original length of bone for Stretch To Constraint

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param constraint: Constraint, Name of the constraint to edit
    :type constraint: typing.Union[str, typing.Any]
    :param owner: Owner, The owner of this constraint * ``OBJECT`` Object, Edit a constraint on the active object. * ``BONE`` Bone, Edit a constraint on the active bone.
    :type owner: typing.Optional[typing.Any]
    '''

    pass
