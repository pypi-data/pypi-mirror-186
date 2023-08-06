import sys
import typing
from . import previews
from . import units

GenericType = typing.TypeVar("GenericType")


def blend_paths(absolute: typing.Optional[bool] = False,
                packed: typing.Optional[bool] = False,
                local: typing.Optional[bool] = False) -> typing.List[str]:
    ''' Returns a list of paths to external files referenced by the loaded .blend file.

    :param absolute: When true the paths returned are made absolute.
    :type absolute: typing.Optional[bool]
    :param packed: When true skip file paths for packed data.
    :type packed: typing.Optional[bool]
    :param local: When true skip linked library paths.
    :type local: typing.Optional[bool]
    :rtype: typing.List[str]
    :return: path list.
    '''

    pass


def escape_identifier(string: typing.Optional[str]) -> str:
    ''' Simple string escaping function used for animation paths.

    :param string: text
    :type string: typing.Optional[str]
    :rtype: str
    :return: The escaped string.
    '''

    pass


def keyconfig_set(filepath, report=None):
    ''' 

    '''

    pass


def load_scripts(reload_scripts: typing.Optional[bool] = False,
                 refresh_scripts: typing.Optional[bool] = False):
    ''' Load scripts and run each modules register function.

    :param reload_scripts: Causes all scripts to have their unregister method called before loading.
    :type reload_scripts: typing.Optional[bool]
    :param refresh_scripts: only load scripts which are not already loaded as modules.
    :type refresh_scripts: typing.Optional[bool]
    '''

    pass


def make_rna_paths(struct_name: typing.Optional[str],
                   prop_name: typing.Optional[str],
                   enum_name: typing.Optional[str]) -> typing.Tuple:
    ''' Create RNA "paths" from given names.

    :param struct_name: Name of a RNA struct (like e.g. "Scene").
    :type struct_name: typing.Optional[str]
    :param prop_name: Name of a RNA struct's property.
    :type prop_name: typing.Optional[str]
    :param enum_name: Name of a RNA enum identifier.
    :type enum_name: typing.Optional[str]
    :rtype: typing.Tuple
    :return: A triple of three "RNA paths" (most_complete_path, "struct.prop", "struct.prop:'enum'"). If no enum_name is given, the third element will always be void.
    '''

    pass


def manual_map():
    ''' 

    '''

    pass


def modules_from_path(
        path: typing.Optional[str],
        loaded_modules: typing.Optional[typing.Set]) -> typing.List:
    ''' Load all modules in a path and return them as a list.

    :param path: this path is scanned for scripts and packages.
    :type path: typing.Optional[str]
    :param loaded_modules: already loaded module names, files matching these names will be ignored.
    :type loaded_modules: typing.Optional[typing.Set]
    :rtype: typing.List
    :return: all loaded modules.
    '''

    pass


def preset_find(name, preset_path, display_name=False, ext='.py'):
    ''' 

    '''

    pass


def preset_paths(subdir: typing.Optional[str]) -> typing.List:
    ''' Returns a list of paths for a specific preset.

    :param subdir: preset subdirectory (must not be an absolute path).
    :type subdir: typing.Optional[str]
    :rtype: typing.List
    :return: script paths.
    '''

    pass


def refresh_script_paths():
    ''' Run this after creating new script paths to update sys.path

    '''

    pass


def register_class(cls):
    ''' Register a subclass of a blender type in (`bpy.types.Panel`, `bpy.types.UIList`, `bpy.types.Menu`, `bpy.types.Header`, `bpy.types.Operator`, `bpy.types.KeyingSetInfo`, `bpy.types.RenderEngine`). If the class has a *register* class method it will be called before registration.

    '''

    pass


def register_manual_map(manual_hook):
    ''' 

    '''

    pass


def register_module(module, verbose=False):
    ''' 

    '''

    pass


def resource_path(type: typing.Optional[str],
                  major: typing.Optional[int] = 'bpy.app.version[0]',
                  minor: typing.Optional[str] = 'bpy.app.version[1]') -> str:
    ''' Return the base path for storing system files.

    :param type: string in ['USER', 'LOCAL', 'SYSTEM'].
    :type type: typing.Optional[str]
    :param major: major version, defaults to current.
    :type major: typing.Optional[int]
    :param minor: minor version, defaults to current.
    :type minor: typing.Optional[str]
    :rtype: str
    :return: the resource path (not necessarily existing).
    '''

    pass


def script_path_pref():
    ''' returns the user preference or None

    '''

    pass


def script_path_user():
    ''' returns the env var and falls back to home dir or None

    '''

    pass


def script_paths(subdir: typing.Optional[str] = None,
                 user_pref: typing.Optional[bool] = True,
                 check_all: typing.Optional[bool] = False) -> typing.List:
    ''' Returns a list of valid script paths.

    :param subdir: Optional subdir.
    :type subdir: typing.Optional[str]
    :param user_pref: Include the user preference script path.
    :type user_pref: typing.Optional[bool]
    :param check_all: Include local, user and system paths rather just the paths blender uses.
    :type check_all: typing.Optional[bool]
    :rtype: typing.List
    :return: script paths.
    '''

    pass


def smpte_from_frame(frame: typing.Optional[int], fps=None,
                     fps_base=None) -> str:
    ''' Returns an SMPTE formatted string from the *frame*: ``HH:MM:SS:FF``. If *fps* and *fps_base* are not given the current scene is used.

    :param frame: frame number.
    :type frame: typing.Optional[int]
    :rtype: str
    :return: the frame string.
    '''

    pass


def smpte_from_seconds(time: typing.Union[int, float], fps=None) -> str:
    ''' Returns an SMPTE formatted string from the *time*: ``HH:MM:SS:FF``. If the *fps* is not given the current scene is used.

    :param time: time in seconds.
    :type time: typing.Union[int, float]
    :rtype: str
    :return: the frame string.
    '''

    pass


def time_from_frame(frame, fps, fps_base):
    ''' 

    '''

    pass


def time_to_frame(time, fps, fps_base):
    ''' 

    '''

    pass


def unregister_class(cls):
    ''' Unload the python class from blender. If the class has an *unregister* class method it will be called before unregistering.

    '''

    pass


def unregister_manual_map(manual_hook):
    ''' 

    '''

    pass


def unregister_module(module, verbose=False):
    ''' 

    '''

    pass


def user_resource(resource_type,
                  path='',
                  create: typing.Optional[bool] = False) -> str:
    ''' Return a user resource path (normally from the users home directory).

    :param type: Resource type in ['DATAFILES', 'CONFIG', 'SCRIPTS', 'AUTOSAVE'].
    :type type: typing.Optional[str]
    :param subdir: Optional subdirectory.
    :type subdir: typing.Optional[str]
    :param create: Treat the path as a directory and create it if its not existing.
    :type create: typing.Optional[bool]
    :rtype: str
    :return: a path.
    '''

    pass
