import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def envmap_clear(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Discard the environment map and free it from memory

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def envmap_clear_all(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Discard all environment maps in the .blend file and free them from memory

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def envmap_save(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                layout: typing.Optional[typing.Any] = (0.0, 0.0, 1.0, 0.0, 2.0,
                                                       0.0, 0.0, 1.0, 1.0, 1.0,
                                                       2.0, 1.0),
                filepath: typing.Union[str, typing.Any] = "",
                check_existing: typing.Union[bool, typing.Any] = True,
                filter_blender: typing.Union[bool, typing.Any] = False,
                filter_backup: typing.Union[bool, typing.Any] = False,
                filter_image: typing.Union[bool, typing.Any] = True,
                filter_movie: typing.Union[bool, typing.Any] = True,
                filter_python: typing.Union[bool, typing.Any] = False,
                filter_font: typing.Union[bool, typing.Any] = False,
                filter_sound: typing.Union[bool, typing.Any] = False,
                filter_text: typing.Union[bool, typing.Any] = False,
                filter_btx: typing.Union[bool, typing.Any] = False,
                filter_collada: typing.Union[bool, typing.Any] = False,
                filter_alembic: typing.Union[bool, typing.Any] = False,
                filter_folder: typing.Union[bool, typing.Any] = True,
                filter_blenlib: typing.Union[bool, typing.Any] = False,
                filemode: typing.Optional[typing.Any] = 9,
                show_multiview: typing.Union[bool, typing.Any] = False,
                use_multiview: typing.Union[bool, typing.Any] = False,
                display_type: typing.Optional[typing.Any] = 'DEFAULT',
                sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA'):
    ''' Save the current generated Environment map to an image file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param layout: File layout, Flat array describing the X,Y position of each cube face in the output image, where 1 is the size of a face - order is [+Z -Z +Y -X -Y +X] (use -1 to skip a face)
    :type layout: typing.Optional[typing.Any]
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
    :param show_multiview: Enable Multi-View
    :type show_multiview: typing.Union[bool, typing.Any]
    :param use_multiview: Use Multi-View
    :type use_multiview: typing.Union[bool, typing.Any]
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    '''

    pass


def new(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a new texture

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def slot_copy(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None):
    ''' Copy the material texture settings and nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def slot_move(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              type: typing.Optional[typing.Any] = 'UP'):
    ''' Move texture slots up and down

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def slot_paste(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Copy the texture settings and nodes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
