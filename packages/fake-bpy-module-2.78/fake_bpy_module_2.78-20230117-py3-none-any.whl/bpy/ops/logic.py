import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def actuator_add(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 type: typing.Union[str, int, typing.Any] = '',
                 name: typing.Union[str, typing.Any] = "",
                 object: typing.Union[str, typing.Any] = ""):
    ''' Add an actuator to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Type of actuator to add
    :type type: typing.Union[str, int, typing.Any]
    :param name: Name, Name of the Actuator to add
    :type name: typing.Union[str, typing.Any]
    :param object: Object, Name of the Object to add the Actuator to
    :type object: typing.Union[str, typing.Any]
    '''

    pass


def actuator_move(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  actuator: typing.Union[str, typing.Any] = "",
                  object: typing.Union[str, typing.Any] = "",
                  direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move Actuator

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param actuator: Actuator, Name of the actuator to edit
    :type actuator: typing.Union[str, typing.Any]
    :param object: Object, Name of the object the actuator belongs to
    :type object: typing.Union[str, typing.Any]
    :param direction: Direction, Move Up or Down
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def actuator_remove(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    actuator: typing.Union[str, typing.Any] = "",
                    object: typing.Union[str, typing.Any] = ""):
    ''' Remove an actuator from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param actuator: Actuator, Name of the actuator to edit
    :type actuator: typing.Union[str, typing.Any]
    :param object: Object, Name of the object the actuator belongs to
    :type object: typing.Union[str, typing.Any]
    '''

    pass


def controller_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   type: typing.Optional[typing.Any] = 'LOGIC_AND',
                   name: typing.Union[str, typing.Any] = "",
                   object: typing.Union[str, typing.Any] = ""):
    ''' Add a controller to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Type of controller to add * ``LOGIC_AND`` And, Logic And. * ``LOGIC_OR`` Or, Logic Or. * ``LOGIC_NAND`` Nand, Logic Nand. * ``LOGIC_NOR`` Nor, Logic Nor. * ``LOGIC_XOR`` Xor, Logic Xor. * ``LOGIC_XNOR`` Xnor, Logic Xnor. * ``EXPRESSION`` Expression. * ``PYTHON`` Python.
    :type type: typing.Optional[typing.Any]
    :param name: Name, Name of the Controller to add
    :type name: typing.Union[str, typing.Any]
    :param object: Object, Name of the Object to add the Controller to
    :type object: typing.Union[str, typing.Any]
    '''

    pass


def controller_move(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    controller: typing.Union[str, typing.Any] = "",
                    object: typing.Union[str, typing.Any] = "",
                    direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move Controller

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param controller: Controller, Name of the controller to edit
    :type controller: typing.Union[str, typing.Any]
    :param object: Object, Name of the object the controller belongs to
    :type object: typing.Union[str, typing.Any]
    :param direction: Direction, Move Up or Down
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def controller_remove(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      controller: typing.Union[str, typing.Any] = "",
                      object: typing.Union[str, typing.Any] = ""):
    ''' Remove a controller from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param controller: Controller, Name of the controller to edit
    :type controller: typing.Union[str, typing.Any]
    :param object: Object, Name of the object the controller belongs to
    :type object: typing.Union[str, typing.Any]
    '''

    pass


def links_cut(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              path: typing.Optional[bpy.types.bpy_prop_collection[
                  'bpy.types.OperatorMousePath']] = None,
              cursor: typing.Optional[typing.Any] = 9):
    ''' Remove logic brick connections

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param path: path
    :type path: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']]
    :param cursor: Cursor
    :type cursor: typing.Optional[typing.Any]
    '''

    pass


def properties(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Toggle the properties region visibility

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def sensor_add(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               type: typing.Union[str, int, typing.Any] = '',
               name: typing.Union[str, typing.Any] = "",
               object: typing.Union[str, typing.Any] = ""):
    ''' Add a sensor to the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Type of sensor to add
    :type type: typing.Union[str, int, typing.Any]
    :param name: Name, Name of the Sensor to add
    :type name: typing.Union[str, typing.Any]
    :param object: Object, Name of the Object to add the Sensor to
    :type object: typing.Union[str, typing.Any]
    '''

    pass


def sensor_move(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                sensor: typing.Union[str, typing.Any] = "",
                object: typing.Union[str, typing.Any] = "",
                direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move Sensor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param sensor: Sensor, Name of the sensor to edit
    :type sensor: typing.Union[str, typing.Any]
    :param object: Object, Name of the object the sensor belongs to
    :type object: typing.Union[str, typing.Any]
    :param direction: Direction, Move Up or Down
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def sensor_remove(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  sensor: typing.Union[str, typing.Any] = "",
                  object: typing.Union[str, typing.Any] = ""):
    ''' Remove a sensor from the active object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param sensor: Sensor, Name of the sensor to edit
    :type sensor: typing.Union[str, typing.Any]
    :param object: Object, Name of the object the sensor belongs to
    :type object: typing.Union[str, typing.Any]
    '''

    pass


def view_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Resize view so you can see all logic bricks

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
