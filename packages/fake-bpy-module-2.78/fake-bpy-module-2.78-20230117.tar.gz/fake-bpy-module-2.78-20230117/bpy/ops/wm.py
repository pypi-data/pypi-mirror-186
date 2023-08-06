import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def addon_disable(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  module: typing.Union[str, typing.Any] = ""):
    ''' Disable an add-on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param module: Module, Module name of the add-on to disable
    :type module: typing.Union[str, typing.Any]
    '''

    pass


def addon_enable(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 module: typing.Union[str, typing.Any] = ""):
    ''' Enable an add-on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param module: Module, Module name of the add-on to enable
    :type module: typing.Union[str, typing.Any]
    '''

    pass


def addon_expand(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 module: typing.Union[str, typing.Any] = ""):
    ''' Display information and preferences for this add-on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param module: Module, Module name of the add-on to expand
    :type module: typing.Union[str, typing.Any]
    '''

    pass


def addon_install(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  overwrite: typing.Union[bool, typing.Any] = True,
                  target: typing.Optional[typing.Any] = 'DEFAULT',
                  filepath: typing.Union[str, typing.Any] = "",
                  filter_folder: typing.Union[bool, typing.Any] = True,
                  filter_python: typing.Union[bool, typing.Any] = True,
                  filter_glob: typing.Union[str, typing.Any] = "*.py;*.zip"):
    ''' Install an add-on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param overwrite: Overwrite, Remove existing add-ons with the same ID
    :type overwrite: typing.Union[bool, typing.Any]
    :param target: Target Path
    :type target: typing.Optional[typing.Any]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_python: Filter python
    :type filter_python: typing.Union[bool, typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    '''

    pass


def addon_refresh(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Scan add-on directories for new modules :file: `startup/bl_operators/wm.py <https://developer.blender.org/diffusion/B/browse/master/release/scripts/ /startup/bl_operators/wm.py>`_:1912

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def addon_remove(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 module: typing.Union[str, typing.Any] = ""):
    ''' Delete the add-on from the file system

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param module: Module, Module name of the add-on to remove
    :type module: typing.Union[str, typing.Any]
    '''

    pass


def addon_userpref_show(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        module: typing.Union[str, typing.Any] = ""):
    ''' Show add-on user preferences

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param module: Module, Module name of the add-on to expand
    :type module: typing.Union[str, typing.Any]
    '''

    pass


def alembic_export(
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
        filter_btx: typing.Union[bool, typing.Any] = False,
        filter_collada: typing.Union[bool, typing.Any] = False,
        filter_alembic: typing.Union[bool, typing.Any] = True,
        filter_folder: typing.Union[bool, typing.Any] = True,
        filter_blenlib: typing.Union[bool, typing.Any] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
        start: typing.Optional[typing.Any] = 1,
        end: typing.Optional[typing.Any] = 1,
        xsamples: typing.Optional[typing.Any] = 1,
        gsamples: typing.Optional[typing.Any] = 1,
        sh_open: typing.Optional[typing.Any] = 0.0,
        sh_close: typing.Optional[typing.Any] = 1.0,
        selected: typing.Union[bool, typing.Any] = False,
        renderable_only: typing.Union[bool, typing.Any] = True,
        visible_layers_only: typing.Union[bool, typing.Any] = False,
        flatten: typing.Union[bool, typing.Any] = False,
        uvs: typing.Union[bool, typing.Any] = True,
        packuv: typing.Union[bool, typing.Any] = True,
        normals: typing.Union[bool, typing.Any] = True,
        vcolors: typing.Union[bool, typing.Any] = False,
        face_sets: typing.Union[bool, typing.Any] = False,
        subdiv_schema: typing.Union[bool, typing.Any] = False,
        apply_subdiv: typing.Union[bool, typing.Any] = False,
        compression_type: typing.Optional[typing.Any] = 'OGAWA',
        global_scale: typing.Optional[typing.Any] = 1.0):
    ''' Export current scene in an Alembic archive

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
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    :param start: Start Frame, Start Frame
    :type start: typing.Optional[typing.Any]
    :param end: End Frame, End Frame
    :type end: typing.Optional[typing.Any]
    :param xsamples: Transform Samples, Number of times per frame transformations are sampled
    :type xsamples: typing.Optional[typing.Any]
    :param gsamples: Geometry Samples, Number of times per frame object data are sampled
    :type gsamples: typing.Optional[typing.Any]
    :param sh_open: Shutter Open, Time at which the shutter is open
    :type sh_open: typing.Optional[typing.Any]
    :param sh_close: Shutter Close, Time at which the shutter is closed
    :type sh_close: typing.Optional[typing.Any]
    :param selected: Selected Objects Only, Export only selected objects
    :type selected: typing.Union[bool, typing.Any]
    :param renderable_only: Renderable Objects Only, Export only objects marked renderable in the outliner
    :type renderable_only: typing.Union[bool, typing.Any]
    :param visible_layers_only: Visible Layers Only, Export only objects in visible layers
    :type visible_layers_only: typing.Union[bool, typing.Any]
    :param flatten: Flatten Hierarchy, Do not preserve objects' parent/children relationship
    :type flatten: typing.Union[bool, typing.Any]
    :param uvs: UVs, Export UVs
    :type uvs: typing.Union[bool, typing.Any]
    :param packuv: Pack UV Islands, Export UVs with packed island
    :type packuv: typing.Union[bool, typing.Any]
    :param normals: Normals, Export normals
    :type normals: typing.Union[bool, typing.Any]
    :param vcolors: Vertex Colors, Export vertex colors
    :type vcolors: typing.Union[bool, typing.Any]
    :param face_sets: Face Sets, Export per face shading group assignments
    :type face_sets: typing.Union[bool, typing.Any]
    :param subdiv_schema: Use Subdivision Schema, Export meshes using Alembic's subdivision schema
    :type subdiv_schema: typing.Union[bool, typing.Any]
    :param apply_subdiv: Apply Subsurf, Export subdivision surfaces as meshes
    :type apply_subdiv: typing.Union[bool, typing.Any]
    :param compression_type: Compression
    :type compression_type: typing.Optional[typing.Any]
    :param global_scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type global_scale: typing.Optional[typing.Any]
    '''

    pass


def alembic_import(
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
        filter_btx: typing.Union[bool, typing.Any] = False,
        filter_collada: typing.Union[bool, typing.Any] = False,
        filter_alembic: typing.Union[bool, typing.Any] = True,
        filter_folder: typing.Union[bool, typing.Any] = True,
        filter_blenlib: typing.Union[bool, typing.Any] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
        scale: typing.Optional[typing.Any] = 1.0,
        set_frame_range: typing.Union[bool, typing.Any] = True,
        validate_meshes: typing.Union[bool, typing.Any] = False,
        is_sequence: typing.Union[bool, typing.Any] = False):
    ''' Load an Alembic archive

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
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    :param scale: Scale, Value by which to enlarge or shrink the objects with respect to the world's origin
    :type scale: typing.Optional[typing.Any]
    :param set_frame_range: Set Frame Range, If checked, update scene's start and end frame to match those of the Alembic archive
    :type set_frame_range: typing.Union[bool, typing.Any]
    :param validate_meshes: Validate Meshes, Check imported mesh objects for invalid data (slow)
    :type validate_meshes: typing.Union[bool, typing.Any]
    :param is_sequence: Is Sequence, Set to true if the cache is split into separate files
    :type is_sequence: typing.Union[bool, typing.Any]
    '''

    pass


def appconfig_activate(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       filepath: typing.Union[str, typing.Any] = ""):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    '''

    pass


def appconfig_default(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Undocumented :file: `startup/bl_operators/wm.py <https://developer.blender.org/diffusion/B/browse/master/release/scripts/ /startup/bl_operators/wm.py>`_:1362

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def append(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           filepath: typing.Union[str, typing.Any] = "",
           directory: typing.Union[str, typing.Any] = "",
           filename: typing.Union[str, typing.Any] = "",
           files: typing.Optional[bpy.types.bpy_prop_collection[
               'bpy.types.OperatorFileListElement']] = None,
           filter_blender: typing.Union[bool, typing.Any] = True,
           filter_backup: typing.Union[bool, typing.Any] = False,
           filter_image: typing.Union[bool, typing.Any] = False,
           filter_movie: typing.Union[bool, typing.Any] = False,
           filter_python: typing.Union[bool, typing.Any] = False,
           filter_font: typing.Union[bool, typing.Any] = False,
           filter_sound: typing.Union[bool, typing.Any] = False,
           filter_text: typing.Union[bool, typing.Any] = False,
           filter_btx: typing.Union[bool, typing.Any] = False,
           filter_collada: typing.Union[bool, typing.Any] = False,
           filter_alembic: typing.Union[bool, typing.Any] = False,
           filter_folder: typing.Union[bool, typing.Any] = True,
           filter_blenlib: typing.Union[bool, typing.Any] = True,
           filemode: typing.Optional[typing.Any] = 1,
           display_type: typing.Optional[typing.Any] = 'DEFAULT',
           sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
           link: typing.Union[bool, typing.Any] = False,
           autoselect: typing.Union[bool, typing.Any] = True,
           active_layer: typing.Union[bool, typing.Any] = True,
           instance_groups: typing.Union[bool, typing.Any] = False,
           set_fake: typing.Union[bool, typing.Any] = False,
           use_recursive: typing.Union[bool, typing.Any] = True):
    ''' Append from a Library .blend file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param filename: File Name, Name of the file
    :type filename: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
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
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    :param link: Link, Link the objects or datablocks rather than appending
    :type link: typing.Union[bool, typing.Any]
    :param autoselect: Select, Select new objects
    :type autoselect: typing.Union[bool, typing.Any]
    :param active_layer: Active Layer, Put new objects on the active layer
    :type active_layer: typing.Union[bool, typing.Any]
    :param instance_groups: Instance Groups, Create Dupli-Group instances for each group
    :type instance_groups: typing.Union[bool, typing.Any]
    :param set_fake: Fake User, Set Fake User for appended items (except Objects and Groups)
    :type set_fake: typing.Union[bool, typing.Any]
    :param use_recursive: Localize All, Localize all appended data, including those indirectly linked from other libraries
    :type use_recursive: typing.Union[bool, typing.Any]
    '''

    pass


def blenderplayer_start(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Launch the blender-player with the current blend-file :file: `startup/bl_operators/wm.py <https://developer.blender.org/diffusion/B/browse/master/release/scripts/ /startup/bl_operators/wm.py>`_:1462

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def call_menu(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              name: typing.Union[str, typing.Any] = ""):
    ''' Call (draw) a pre-defined menu

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the menu
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def call_menu_pie(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  name: typing.Union[str, typing.Any] = ""):
    ''' Call (draw) a pre-defined pie menu

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the pie menu
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def collada_export(
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
        filter_btx: typing.Union[bool, typing.Any] = False,
        filter_collada: typing.Union[bool, typing.Any] = True,
        filter_alembic: typing.Union[bool, typing.Any] = False,
        filter_folder: typing.Union[bool, typing.Any] = True,
        filter_blenlib: typing.Union[bool, typing.Any] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
        apply_modifiers: typing.Union[bool, typing.Any] = False,
        export_mesh_type: typing.Optional[typing.Any] = 0,
        export_mesh_type_selection: typing.Optional[typing.Any] = 'view',
        selected: typing.Union[bool, typing.Any] = False,
        include_children: typing.Union[bool, typing.Any] = False,
        include_armatures: typing.Union[bool, typing.Any] = False,
        include_shapekeys: typing.Union[bool, typing.Any] = True,
        deform_bones_only: typing.Union[bool, typing.Any] = False,
        active_uv_only: typing.Union[bool, typing.Any] = False,
        include_uv_textures: typing.Union[bool, typing.Any] = False,
        include_material_textures: typing.Union[bool, typing.Any] = False,
        use_texture_copies: typing.Union[bool, typing.Any] = True,
        triangulate: typing.Union[bool, typing.Any] = True,
        use_object_instantiation: typing.Union[bool, typing.Any] = True,
        use_blender_profile: typing.Union[bool, typing.Any] = True,
        sort_by_name: typing.Union[bool, typing.Any] = False,
        export_transformation_type: typing.Optional[typing.Any] = 0,
        export_transformation_type_selection: typing.Optional[typing.
                                                              Any] = 'matrix',
        open_sim: typing.Union[bool, typing.Any] = False):
    ''' Save a Collada file

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
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    :param apply_modifiers: Apply Modifiers, Apply modifiers to exported mesh (non destructive))
    :type apply_modifiers: typing.Union[bool, typing.Any]
    :param export_mesh_type: Resolution, Modifier resolution for export
    :type export_mesh_type: typing.Optional[typing.Any]
    :param export_mesh_type_selection: Resolution, Modifier resolution for export * ``view`` View, Apply modifier's view settings. * ``render`` Render, Apply modifier's render settings.
    :type export_mesh_type_selection: typing.Optional[typing.Any]
    :param selected: Selection Only, Export only selected elements
    :type selected: typing.Union[bool, typing.Any]
    :param include_children: Include Children, Export all children of selected objects (even if not selected)
    :type include_children: typing.Union[bool, typing.Any]
    :param include_armatures: Include Armatures, Export related armatures (even if not selected)
    :type include_armatures: typing.Union[bool, typing.Any]
    :param include_shapekeys: Include Shape Keys, Export all Shape Keys from Mesh Objects
    :type include_shapekeys: typing.Union[bool, typing.Any]
    :param deform_bones_only: Deform Bones only, Only export deforming bones with armatures
    :type deform_bones_only: typing.Union[bool, typing.Any]
    :param active_uv_only: Only Selected UV Map, Export only the selected UV Map
    :type active_uv_only: typing.Union[bool, typing.Any]
    :param include_uv_textures: Include UV Textures, Export textures assigned to the object UV Maps
    :type include_uv_textures: typing.Union[bool, typing.Any]
    :param include_material_textures: Include Material Textures, Export textures assigned to the object Materials
    :type include_material_textures: typing.Union[bool, typing.Any]
    :param use_texture_copies: Copy, Copy textures to same folder where the .dae file is exported
    :type use_texture_copies: typing.Union[bool, typing.Any]
    :param triangulate: Triangulate, Export Polygons (Quads & NGons) as Triangles
    :type triangulate: typing.Union[bool, typing.Any]
    :param use_object_instantiation: Use Object Instances, Instantiate multiple Objects from same Data
    :type use_object_instantiation: typing.Union[bool, typing.Any]
    :param use_blender_profile: Use Blender Profile, Export additional Blender specific information (for material, shaders, bones, etc.)
    :type use_blender_profile: typing.Union[bool, typing.Any]
    :param sort_by_name: Sort by Object name, Sort exported data by Object name
    :type sort_by_name: typing.Union[bool, typing.Any]
    :param export_transformation_type: Transform, Transformation type for translation, scale and rotation
    :type export_transformation_type: typing.Optional[typing.Any]
    :param export_transformation_type_selection: Transform, Transformation type for translation, scale and rotation * ``matrix`` Matrix, Use <matrix> to specify transformations. * ``transrotloc`` TransRotLoc, Use <translate>, <rotate>, <scale> to specify transformations. * ``both`` Both, Use <matrix> AND <translate>, <rotate>, <scale> to specify transformations.
    :type export_transformation_type_selection: typing.Optional[typing.Any]
    :param open_sim: Export to SL/OpenSim, Compatibility mode for SL, OpenSim and other compatible online worlds
    :type open_sim: typing.Union[bool, typing.Any]
    '''

    pass


def collada_import(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        filter_blender: typing.Union[bool, typing.Any] = False,
        filter_backup: typing.Union[bool, typing.Any] = False,
        filter_image: typing.Union[bool, typing.Any] = False,
        filter_movie: typing.Union[bool, typing.Any] = False,
        filter_python: typing.Union[bool, typing.Any] = False,
        filter_font: typing.Union[bool, typing.Any] = False,
        filter_sound: typing.Union[bool, typing.Any] = False,
        filter_text: typing.Union[bool, typing.Any] = False,
        filter_btx: typing.Union[bool, typing.Any] = False,
        filter_collada: typing.Union[bool, typing.Any] = True,
        filter_alembic: typing.Union[bool, typing.Any] = False,
        filter_folder: typing.Union[bool, typing.Any] = True,
        filter_blenlib: typing.Union[bool, typing.Any] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
        import_units: typing.Union[bool, typing.Any] = False,
        fix_orientation: typing.Union[bool, typing.Any] = False,
        find_chains: typing.Union[bool, typing.Any] = False,
        auto_connect: typing.Union[bool, typing.Any] = False,
        min_chain_length: typing.Optional[typing.Any] = 0):
    ''' Load a Collada file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    :param import_units: Import Units, If disabled match import to Blender's current Unit settings, otherwise use the settings from the Imported scene
    :type import_units: typing.Union[bool, typing.Any]
    :param fix_orientation: Fix Leaf Bones, Fix Orientation of Leaf Bones (Collada does only support Joints)
    :type fix_orientation: typing.Union[bool, typing.Any]
    :param find_chains: Find Bone Chains, Find best matching Bone Chains and ensure bones in chain are connected
    :type find_chains: typing.Union[bool, typing.Any]
    :param auto_connect: Auto Connect, Set use_connect for parent bones which have exactly one child bone
    :type auto_connect: typing.Union[bool, typing.Any]
    :param min_chain_length: Minimum Chain Length, When searching Bone Chains disregard chains of length below this value
    :type min_chain_length: typing.Optional[typing.Any]
    '''

    pass


def context_collection_boolean_set(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path_iter: typing.Union[str, typing.Any] = "",
        data_path_item: typing.Union[str, typing.Any] = "",
        type: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Set boolean values for a collection of items

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: typing.Union[str, typing.Any]
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: typing.Union[str, typing.Any]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def context_cycle_array(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        data_path: typing.Union[str, typing.Any] = "",
                        reverse: typing.Union[bool, typing.Any] = False):
    ''' Set a context array value (useful for cycling the active mesh edit mode)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param reverse: Reverse, Cycle backwards
    :type reverse: typing.Union[bool, typing.Any]
    '''

    pass


def context_cycle_enum(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       data_path: typing.Union[str, typing.Any] = "",
                       reverse: typing.Union[bool, typing.Any] = False,
                       wrap: typing.Union[bool, typing.Any] = False):
    ''' Toggle a context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param reverse: Reverse, Cycle backwards
    :type reverse: typing.Union[bool, typing.Any]
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: typing.Union[bool, typing.Any]
    '''

    pass


def context_cycle_int(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      data_path: typing.Union[str, typing.Any] = "",
                      reverse: typing.Union[bool, typing.Any] = False,
                      wrap: typing.Union[bool, typing.Any] = False):
    ''' Set a context value (useful for cycling active material, vertex keys, groups, etc.)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param reverse: Reverse, Cycle backwards
    :type reverse: typing.Union[bool, typing.Any]
    :param wrap: Wrap, Wrap back to the first/last values
    :type wrap: typing.Union[bool, typing.Any]
    '''

    pass


def context_menu_enum(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      data_path: typing.Union[str, typing.Any] = ""):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    '''

    pass


def context_modal_mouse(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        data_path_iter: typing.Union[str, typing.Any] = "",
                        data_path_item: typing.Union[str, typing.Any] = "",
                        header_text: typing.Union[str, typing.Any] = "",
                        input_scale: typing.Optional[typing.Any] = 0.01,
                        invert: typing.Union[bool, typing.Any] = False,
                        initial_x: typing.Optional[typing.Any] = 0):
    ''' Adjust arbitrary values with mouse input

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path_iter: data_path_iter, The data path relative to the context, must point to an iterable
    :type data_path_iter: typing.Union[str, typing.Any]
    :param data_path_item: data_path_item, The data path from each iterable to the value (int or float)
    :type data_path_item: typing.Union[str, typing.Any]
    :param header_text: Header Text, Text to display in header during scale
    :type header_text: typing.Union[str, typing.Any]
    :param input_scale: input_scale, Scale the mouse movement by this value before applying the delta
    :type input_scale: typing.Optional[typing.Any]
    :param invert: invert, Invert the mouse input
    :type invert: typing.Union[bool, typing.Any]
    :param initial_x: initial_x
    :type initial_x: typing.Optional[typing.Any]
    '''

    pass


def context_pie_enum(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     data_path: typing.Union[str, typing.Any] = ""):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    '''

    pass


def context_scale_float(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        data_path: typing.Union[str, typing.Any] = "",
                        value: typing.Optional[typing.Any] = 1.0):
    ''' Scale a float context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Optional[typing.Any]
    '''

    pass


def context_scale_int(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      data_path: typing.Union[str, typing.Any] = "",
                      value: typing.Optional[typing.Any] = 1.0,
                      always_step: typing.Union[bool, typing.Any] = True):
    ''' Scale an int context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Optional[typing.Any]
    :param always_step: Always Step, Always adjust the value by a minimum of 1 when 'value' is not 1.0
    :type always_step: typing.Union[bool, typing.Any]
    '''

    pass


def context_set_boolean(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        data_path: typing.Union[str, typing.Any] = "",
                        value: typing.Union[bool, typing.Any] = True):
    ''' Set a context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assignment value
    :type value: typing.Union[bool, typing.Any]
    '''

    pass


def context_set_enum(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     data_path: typing.Union[str, typing.Any] = "",
                     value: typing.Union[str, typing.Any] = ""):
    ''' Set a context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assignment value (as a string)
    :type value: typing.Union[str, typing.Any]
    '''

    pass


def context_set_float(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      data_path: typing.Union[str, typing.Any] = "",
                      value: typing.Optional[typing.Any] = 0.0,
                      relative: typing.Union[bool, typing.Any] = False):
    ''' Set a context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assignment value
    :type value: typing.Optional[typing.Any]
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: typing.Union[bool, typing.Any]
    '''

    pass


def context_set_id(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   data_path: typing.Union[str, typing.Any] = "",
                   value: typing.Union[str, typing.Any] = ""):
    ''' Set a context value to an ID data-block

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Union[str, typing.Any]
    '''

    pass


def context_set_int(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    data_path: typing.Union[str, typing.Any] = "",
                    value: typing.Optional[typing.Any] = 0,
                    relative: typing.Union[bool, typing.Any] = False):
    ''' Set a context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Optional[typing.Any]
    :param relative: Relative, Apply relative to the current value (delta)
    :type relative: typing.Union[bool, typing.Any]
    '''

    pass


def context_set_string(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       data_path: typing.Union[str, typing.Any] = "",
                       value: typing.Union[str, typing.Any] = ""):
    ''' Set a context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assign value
    :type value: typing.Union[str, typing.Any]
    '''

    pass


def context_set_value(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      data_path: typing.Union[str, typing.Any] = "",
                      value: typing.Union[str, typing.Any] = ""):
    ''' Set a context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value: Value, Assignment value (as a string)
    :type value: typing.Union[str, typing.Any]
    '''

    pass


def context_toggle(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   data_path: typing.Union[str, typing.Any] = ""):
    ''' Toggle a context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    '''

    pass


def context_toggle_enum(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        data_path: typing.Union[str, typing.Any] = "",
                        value_1: typing.Union[str, typing.Any] = "",
                        value_2: typing.Union[str, typing.Any] = ""):
    ''' Toggle a context value

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Context Attributes, RNA context string
    :type data_path: typing.Union[str, typing.Any]
    :param value_1: Value, Toggle enum
    :type value_1: typing.Union[str, typing.Any]
    :param value_2: Value, Toggle enum
    :type value_2: typing.Union[str, typing.Any]
    '''

    pass


def copy_prev_settings(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None):
    ''' Copy settings from previous version :file: `startup/bl_operators/wm.py <https://developer.blender.org/diffusion/B/browse/master/release/scripts/ /startup/bl_operators/wm.py>`_:1428

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def debug_menu(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               debug_value: typing.Optional[typing.Any] = 0):
    ''' Open a popup to set the debug level

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param debug_value: Debug Value
    :type debug_value: typing.Optional[typing.Any]
    '''

    pass


def dependency_relations(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Print dependency graph relations to the console

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def doc_view(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             doc_id: typing.Union[str, typing.Any] = ""):
    ''' Load online reference docs

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param doc_id: Doc ID
    :type doc_id: typing.Union[str, typing.Any]
    '''

    pass


def doc_view_manual(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    doc_id: typing.Union[str, typing.Any] = ""):
    ''' Load online manual

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param doc_id: Doc ID
    :type doc_id: typing.Union[str, typing.Any]
    '''

    pass


def doc_view_manual_ui_context(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' View a context based online manual in a web browser

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def interaction_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_active: typing.Union[bool, typing.Any] = False):
    ''' Add or remove an Application Interaction Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_active: remove_active
    :type remove_active: typing.Union[bool, typing.Any]
    '''

    pass


def interface_theme_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_active: typing.Union[bool, typing.Any] = False):
    ''' Add or remove a theme preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_active: remove_active
    :type remove_active: typing.Union[bool, typing.Any]
    '''

    pass


def keyconfig_activate(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       filepath: typing.Union[str, typing.Any] = ""):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    '''

    pass


def keyconfig_export(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     filepath: typing.Union[str, typing.Any] = "keymap.py",
                     filter_folder: typing.Union[bool, typing.Any] = True,
                     filter_text: typing.Union[bool, typing.Any] = True,
                     filter_python: typing.Union[bool, typing.Any] = True):
    ''' Export key configuration to a python script

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_text: Filter text
    :type filter_text: typing.Union[bool, typing.Any]
    :param filter_python: Filter python
    :type filter_python: typing.Union[bool, typing.Any]
    '''

    pass


def keyconfig_import(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     filepath: typing.Union[str, typing.Any] = "keymap.py",
                     filter_folder: typing.Union[bool, typing.Any] = True,
                     filter_text: typing.Union[bool, typing.Any] = True,
                     filter_python: typing.Union[bool, typing.Any] = True,
                     keep_original: typing.Union[bool, typing.Any] = True):
    ''' Import key configuration from a python script

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_text: Filter text
    :type filter_text: typing.Union[bool, typing.Any]
    :param filter_python: Filter python
    :type filter_python: typing.Union[bool, typing.Any]
    :param keep_original: Keep original, Keep original file after copying to configuration folder
    :type keep_original: typing.Union[bool, typing.Any]
    '''

    pass


def keyconfig_preset_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "",
        remove_active: typing.Union[bool, typing.Any] = False):
    ''' Add or remove a Key-config Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_active: remove_active
    :type remove_active: typing.Union[bool, typing.Any]
    '''

    pass


def keyconfig_remove(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Remove key config :file: `startup/bl_operators/wm.py <https://developer.blender.org/diffusion/B/browse/master/release/scripts/ /startup/bl_operators/wm.py>`_:1740

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def keyconfig_test(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Test key-config for conflicts :file: `startup/bl_operators/wm.py <https://developer.blender.org/diffusion/B/browse/master/release/scripts/ /startup/bl_operators/wm.py>`_:1510

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def keyitem_add(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Add key map item :file: `startup/bl_operators/wm.py <https://developer.blender.org/diffusion/B/browse/master/release/scripts/ /startup/bl_operators/wm.py>`_:1691

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def keyitem_remove(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   item_id: typing.Optional[typing.Any] = 0):
    ''' Remove key map item

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param item_id: Item Identifier, Identifier of the item to remove
    :type item_id: typing.Optional[typing.Any]
    '''

    pass


def keyitem_restore(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    item_id: typing.Optional[typing.Any] = 0):
    ''' Restore key map item

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param item_id: Item Identifier, Identifier of the item to remove
    :type item_id: typing.Optional[typing.Any]
    '''

    pass


def keymap_restore(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   all: typing.Union[bool, typing.Any] = False):
    ''' Restore key map(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param all: All Keymaps, Restore all keymaps to default
    :type all: typing.Union[bool, typing.Any]
    '''

    pass


def lib_reload(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               library: typing.Union[str, typing.Any] = "",
               filepath: typing.Union[str, typing.Any] = "",
               directory: typing.Union[str, typing.Any] = "",
               filename: typing.Union[str, typing.Any] = "",
               filter_blender: typing.Union[bool, typing.Any] = True,
               filter_backup: typing.Union[bool, typing.Any] = False,
               filter_image: typing.Union[bool, typing.Any] = False,
               filter_movie: typing.Union[bool, typing.Any] = False,
               filter_python: typing.Union[bool, typing.Any] = False,
               filter_font: typing.Union[bool, typing.Any] = False,
               filter_sound: typing.Union[bool, typing.Any] = False,
               filter_text: typing.Union[bool, typing.Any] = False,
               filter_btx: typing.Union[bool, typing.Any] = False,
               filter_collada: typing.Union[bool, typing.Any] = False,
               filter_alembic: typing.Union[bool, typing.Any] = False,
               filter_folder: typing.Union[bool, typing.Any] = True,
               filter_blenlib: typing.Union[bool, typing.Any] = False,
               filemode: typing.Optional[typing.Any] = 8,
               relative_path: typing.Union[bool, typing.Any] = True,
               display_type: typing.Optional[typing.Any] = 'DEFAULT',
               sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA'):
    ''' Reload the given library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param library: Library, Library to reload
    :type library: typing.Union[str, typing.Any]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param filename: File Name, Name of the file
    :type filename: typing.Union[str, typing.Any]
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
    '''

    pass


def lib_relocate(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 library: typing.Union[str, typing.Any] = "",
                 filepath: typing.Union[str, typing.Any] = "",
                 directory: typing.Union[str, typing.Any] = "",
                 filename: typing.Union[str, typing.Any] = "",
                 files: typing.Optional[bpy.types.bpy_prop_collection[
                     'bpy.types.OperatorFileListElement']] = None,
                 filter_blender: typing.Union[bool, typing.Any] = True,
                 filter_backup: typing.Union[bool, typing.Any] = False,
                 filter_image: typing.Union[bool, typing.Any] = False,
                 filter_movie: typing.Union[bool, typing.Any] = False,
                 filter_python: typing.Union[bool, typing.Any] = False,
                 filter_font: typing.Union[bool, typing.Any] = False,
                 filter_sound: typing.Union[bool, typing.Any] = False,
                 filter_text: typing.Union[bool, typing.Any] = False,
                 filter_btx: typing.Union[bool, typing.Any] = False,
                 filter_collada: typing.Union[bool, typing.Any] = False,
                 filter_alembic: typing.Union[bool, typing.Any] = False,
                 filter_folder: typing.Union[bool, typing.Any] = True,
                 filter_blenlib: typing.Union[bool, typing.Any] = False,
                 filemode: typing.Optional[typing.Any] = 8,
                 relative_path: typing.Union[bool, typing.Any] = True,
                 display_type: typing.Optional[typing.Any] = 'DEFAULT',
                 sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA'):
    ''' Relocate the given library to one or several others

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param library: Library, Library to relocate
    :type library: typing.Union[str, typing.Any]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param filename: File Name, Name of the file
    :type filename: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
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
    '''

    pass


def link(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         filepath: typing.Union[str, typing.Any] = "",
         directory: typing.Union[str, typing.Any] = "",
         filename: typing.Union[str, typing.Any] = "",
         files: typing.Optional[bpy.types.bpy_prop_collection[
             'bpy.types.OperatorFileListElement']] = None,
         filter_blender: typing.Union[bool, typing.Any] = True,
         filter_backup: typing.Union[bool, typing.Any] = False,
         filter_image: typing.Union[bool, typing.Any] = False,
         filter_movie: typing.Union[bool, typing.Any] = False,
         filter_python: typing.Union[bool, typing.Any] = False,
         filter_font: typing.Union[bool, typing.Any] = False,
         filter_sound: typing.Union[bool, typing.Any] = False,
         filter_text: typing.Union[bool, typing.Any] = False,
         filter_btx: typing.Union[bool, typing.Any] = False,
         filter_collada: typing.Union[bool, typing.Any] = False,
         filter_alembic: typing.Union[bool, typing.Any] = False,
         filter_folder: typing.Union[bool, typing.Any] = True,
         filter_blenlib: typing.Union[bool, typing.Any] = True,
         filemode: typing.Optional[typing.Any] = 1,
         relative_path: typing.Union[bool, typing.Any] = True,
         display_type: typing.Optional[typing.Any] = 'DEFAULT',
         sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
         link: typing.Union[bool, typing.Any] = True,
         autoselect: typing.Union[bool, typing.Any] = True,
         active_layer: typing.Union[bool, typing.Any] = True,
         instance_groups: typing.Union[bool, typing.Any] = True):
    ''' Link from a Library .blend file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param directory: Directory, Directory of the file
    :type directory: typing.Union[str, typing.Any]
    :param filename: File Name, Name of the file
    :type filename: typing.Union[str, typing.Any]
    :param files: Files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
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
    :param link: Link, Link the objects or datablocks rather than appending
    :type link: typing.Union[bool, typing.Any]
    :param autoselect: Select, Select new objects
    :type autoselect: typing.Union[bool, typing.Any]
    :param active_layer: Active Layer, Put new objects on the active layer
    :type active_layer: typing.Union[bool, typing.Any]
    :param instance_groups: Instance Groups, Create Dupli-Group instances for each group
    :type instance_groups: typing.Union[bool, typing.Any]
    '''

    pass


def memory_statistics(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Print memory statistics to the console

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def open_mainfile(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  filepath: typing.Union[str, typing.Any] = "",
                  filter_blender: typing.Union[bool, typing.Any] = True,
                  filter_backup: typing.Union[bool, typing.Any] = False,
                  filter_image: typing.Union[bool, typing.Any] = False,
                  filter_movie: typing.Union[bool, typing.Any] = False,
                  filter_python: typing.Union[bool, typing.Any] = False,
                  filter_font: typing.Union[bool, typing.Any] = False,
                  filter_sound: typing.Union[bool, typing.Any] = False,
                  filter_text: typing.Union[bool, typing.Any] = False,
                  filter_btx: typing.Union[bool, typing.Any] = False,
                  filter_collada: typing.Union[bool, typing.Any] = False,
                  filter_alembic: typing.Union[bool, typing.Any] = False,
                  filter_folder: typing.Union[bool, typing.Any] = True,
                  filter_blenlib: typing.Union[bool, typing.Any] = False,
                  filemode: typing.Optional[typing.Any] = 8,
                  display_type: typing.Optional[typing.Any] = 'DEFAULT',
                  sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
                  load_ui: typing.Union[bool, typing.Any] = True,
                  use_scripts: typing.Union[bool, typing.Any] = True):
    ''' Open a Blender file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    :param load_ui: Load UI, Load user interface setup in the .blend file
    :type load_ui: typing.Union[bool, typing.Any]
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: typing.Union[bool, typing.Any]
    '''

    pass


def operator_cheat_sheet(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Undocumented :file: `startup/bl_operators/wm.py <https://developer.blender.org/diffusion/B/browse/master/release/scripts/ /startup/bl_operators/wm.py>`_:1751

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def operator_defaults(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Set the active operator to its default values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def operator_pie_enum(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      data_path: typing.Union[str, typing.Any] = "",
                      prop_string: typing.Union[str, typing.Any] = ""):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Operator, Operator name (in python as string)
    :type data_path: typing.Union[str, typing.Any]
    :param prop_string: Property, Property name (as a string)
    :type prop_string: typing.Union[str, typing.Any]
    '''

    pass


def operator_preset_add(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        name: typing.Union[str, typing.Any] = "",
                        remove_active: typing.Union[bool, typing.Any] = False,
                        operator: typing.Union[str, typing.Any] = ""):
    ''' Add or remove an Operator Preset

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of the preset, used to make the path name
    :type name: typing.Union[str, typing.Any]
    :param remove_active: remove_active
    :type remove_active: typing.Union[bool, typing.Any]
    :param operator: Operator
    :type operator: typing.Union[str, typing.Any]
    '''

    pass


def path_open(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              filepath: typing.Union[str, typing.Any] = ""):
    ''' Open a path in a file browser

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    '''

    pass


def previews_batch_clear(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        directory: typing.Union[str, typing.Any] = "",
        filter_blender: typing.Union[bool, typing.Any] = True,
        filter_folder: typing.Union[bool, typing.Any] = True,
        use_scenes: typing.Union[bool, typing.Any] = True,
        use_groups: typing.Union[bool, typing.Any] = True,
        use_objects: typing.Union[bool, typing.Any] = True,
        use_intern_data: typing.Union[bool, typing.Any] = True,
        use_trusted: typing.Union[bool, typing.Any] = False,
        use_backups: typing.Union[bool, typing.Any] = True):
    ''' Clear selected .blend file's previews

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param files: files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param directory: directory
    :type directory: typing.Union[str, typing.Any]
    :param filter_blender: filter_blender
    :type filter_blender: typing.Union[bool, typing.Any]
    :param filter_folder: filter_folder
    :type filter_folder: typing.Union[bool, typing.Any]
    :param use_scenes: Scenes, Clear scenes' previews
    :type use_scenes: typing.Union[bool, typing.Any]
    :param use_groups: Groups, Clear groups' previews
    :type use_groups: typing.Union[bool, typing.Any]
    :param use_objects: Objects, Clear objects' previews
    :type use_objects: typing.Union[bool, typing.Any]
    :param use_intern_data: Mat/Tex/..., Clear 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: typing.Union[bool, typing.Any]
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: typing.Union[bool, typing.Any]
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with cleared previews
    :type use_backups: typing.Union[bool, typing.Any]
    '''

    pass


def previews_batch_generate(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        files: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorFileListElement']] = None,
        directory: typing.Union[str, typing.Any] = "",
        filter_blender: typing.Union[bool, typing.Any] = True,
        filter_folder: typing.Union[bool, typing.Any] = True,
        use_scenes: typing.Union[bool, typing.Any] = True,
        use_groups: typing.Union[bool, typing.Any] = True,
        use_objects: typing.Union[bool, typing.Any] = True,
        use_intern_data: typing.Union[bool, typing.Any] = True,
        use_trusted: typing.Union[bool, typing.Any] = False,
        use_backups: typing.Union[bool, typing.Any] = True):
    ''' Generate selected .blend file's previews

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param files: files
    :type files: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorFileListElement']]
    :param directory: directory
    :type directory: typing.Union[str, typing.Any]
    :param filter_blender: filter_blender
    :type filter_blender: typing.Union[bool, typing.Any]
    :param filter_folder: filter_folder
    :type filter_folder: typing.Union[bool, typing.Any]
    :param use_scenes: Scenes, Generate scenes' previews
    :type use_scenes: typing.Union[bool, typing.Any]
    :param use_groups: Groups, Generate groups' previews
    :type use_groups: typing.Union[bool, typing.Any]
    :param use_objects: Objects, Generate objects' previews
    :type use_objects: typing.Union[bool, typing.Any]
    :param use_intern_data: Mat/Tex/..., Generate 'internal' previews (materials, textures, images, etc.)
    :type use_intern_data: typing.Union[bool, typing.Any]
    :param use_trusted: Trusted Blend Files, Enable python evaluation for selected files
    :type use_trusted: typing.Union[bool, typing.Any]
    :param use_backups: Save Backups, Keep a backup (.blend1) version of the files when saving with generated previews
    :type use_backups: typing.Union[bool, typing.Any]
    '''

    pass


def previews_clear(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   id_type: typing.Optional[typing.Any] = {
                       'GROUP', 'IMAGE', 'LAMP', 'MATERIAL', 'OBJECT', 'SCENE',
                       'TEXTURE', 'WORLD'
                   }):
    ''' Clear datablock previews (only for some types like objects, materials, textures, etc.)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param id_type: DataBlock Type, Which datablock previews to clear
    :type id_type: typing.Optional[typing.Any]
    '''

    pass


def previews_ensure(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Ensure datablock previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def properties_add(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None,
                   *,
                   data_path: typing.Union[str, typing.Any] = ""):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Property Edit, Property data_path edit
    :type data_path: typing.Union[str, typing.Any]
    '''

    pass


def properties_context_change(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: typing.Optional[bool] = None,
                              *,
                              context: typing.Union[str, typing.Any] = ""):
    ''' Jump to a different tab inside the properties editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param context: Context
    :type context: typing.Union[str, typing.Any]
    '''

    pass


def properties_edit(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    data_path: typing.Union[str, typing.Any] = "",
                    property: typing.Union[str, typing.Any] = "",
                    value: typing.Union[str, typing.Any] = "",
                    min: typing.Optional[typing.Any] = -10000,
                    max: typing.Optional[typing.Any] = 10000.0,
                    use_soft_limits: typing.Union[bool, typing.Any] = False,
                    soft_min: typing.Optional[typing.Any] = -10000,
                    soft_max: typing.Optional[typing.Any] = 10000.0,
                    description: typing.Union[str, typing.Any] = ""):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Property Edit, Property data_path edit
    :type data_path: typing.Union[str, typing.Any]
    :param property: Property Name, Property name edit
    :type property: typing.Union[str, typing.Any]
    :param value: Property Value, Property value edit
    :type value: typing.Union[str, typing.Any]
    :param min: Min
    :type min: typing.Optional[typing.Any]
    :param max: Max
    :type max: typing.Optional[typing.Any]
    :param use_soft_limits: Use Soft Limits
    :type use_soft_limits: typing.Union[bool, typing.Any]
    :param soft_min: Min
    :type soft_min: typing.Optional[typing.Any]
    :param soft_max: Max
    :type soft_max: typing.Optional[typing.Any]
    :param description: Tooltip
    :type description: typing.Union[str, typing.Any]
    '''

    pass


def properties_remove(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      data_path: typing.Union[str, typing.Any] = "",
                      property: typing.Union[str, typing.Any] = ""):
    ''' Internal use (edit a property data_path)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path: Property Edit, Property data_path edit
    :type data_path: typing.Union[str, typing.Any]
    :param property: Property Name, Property name edit
    :type property: typing.Union[str, typing.Any]
    '''

    pass


def quit_blender(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Quit Blender

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def radial_control(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        data_path_primary: typing.Union[str, typing.Any] = "",
        data_path_secondary: typing.Union[str, typing.Any] = "",
        use_secondary: typing.Union[str, typing.Any] = "",
        rotation_path: typing.Union[str, typing.Any] = "",
        color_path: typing.Union[str, typing.Any] = "",
        fill_color_path: typing.Union[str, typing.Any] = "",
        fill_color_override_path: typing.Union[str, typing.Any] = "",
        fill_color_override_test_path: typing.Union[str, typing.Any] = "",
        zoom_path: typing.Union[str, typing.Any] = "",
        image_id: typing.Union[str, typing.Any] = "",
        secondary_tex: typing.Union[bool, typing.Any] = False):
    ''' Set some size property (like e.g. brush size) with mouse wheel

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param data_path_primary: Primary Data Path, Primary path of property to be set by the radial control
    :type data_path_primary: typing.Union[str, typing.Any]
    :param data_path_secondary: Secondary Data Path, Secondary path of property to be set by the radial control
    :type data_path_secondary: typing.Union[str, typing.Any]
    :param use_secondary: Use Secondary, Path of property to select between the primary and secondary data paths
    :type use_secondary: typing.Union[str, typing.Any]
    :param rotation_path: Rotation Path, Path of property used to rotate the texture display
    :type rotation_path: typing.Union[str, typing.Any]
    :param color_path: Color Path, Path of property used to set the color of the control
    :type color_path: typing.Union[str, typing.Any]
    :param fill_color_path: Fill Color Path, Path of property used to set the fill color of the control
    :type fill_color_path: typing.Union[str, typing.Any]
    :param fill_color_override_path: Fill Color Override Path
    :type fill_color_override_path: typing.Union[str, typing.Any]
    :param fill_color_override_test_path: Fill Color Override Test
    :type fill_color_override_test_path: typing.Union[str, typing.Any]
    :param zoom_path: Zoom Path, Path of property used to set the zoom level for the control
    :type zoom_path: typing.Union[str, typing.Any]
    :param image_id: Image ID, Path of ID that is used to generate an image for the control
    :type image_id: typing.Union[str, typing.Any]
    :param secondary_tex: Secondary Texture, Tweak brush secondary/mask texture
    :type secondary_tex: typing.Union[bool, typing.Any]
    '''

    pass


def read_factory_settings(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None):
    ''' Load default file and user preferences

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def read_history(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Reloads history and bookmarks

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def read_homefile(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  filepath: typing.Union[str, typing.Any] = "",
                  load_ui: typing.Union[bool, typing.Any] = True):
    ''' Open the default file (doesn't save the current file)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to an alternative start-up file
    :type filepath: typing.Union[str, typing.Any]
    :param load_ui: Load UI, Load user interface setup from the .blend file
    :type load_ui: typing.Union[bool, typing.Any]
    '''

    pass


def recover_auto_save(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        filter_blender: typing.Union[bool, typing.Any] = True,
        filter_backup: typing.Union[bool, typing.Any] = False,
        filter_image: typing.Union[bool, typing.Any] = False,
        filter_movie: typing.Union[bool, typing.Any] = False,
        filter_python: typing.Union[bool, typing.Any] = False,
        filter_font: typing.Union[bool, typing.Any] = False,
        filter_sound: typing.Union[bool, typing.Any] = False,
        filter_text: typing.Union[bool, typing.Any] = False,
        filter_btx: typing.Union[bool, typing.Any] = False,
        filter_collada: typing.Union[bool, typing.Any] = False,
        filter_alembic: typing.Union[bool, typing.Any] = False,
        filter_folder: typing.Union[bool, typing.Any] = False,
        filter_blenlib: typing.Union[bool, typing.Any] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'LIST_LONG',
        sort_method: typing.Optional[typing.Any] = 'FILE_SORT_TIME'):
    ''' Open an automatically saved file to recover it

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
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
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    '''

    pass


def recover_last_session(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Open the last closed file ("quit.blend")

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def redraw_timer(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 type: typing.Optional[typing.Any] = 'DRAW',
                 iterations: typing.Optional[typing.Any] = 10,
                 time_limit: typing.Optional[typing.Any] = 0.0):
    ''' Simple redraw timer to test the speed of updating the interface

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type * ``DRAW`` Draw Region, Draw Region. * ``DRAW_SWAP`` Draw Region + Swap, Draw Region and Swap. * ``DRAW_WIN`` Draw Window, Draw Window. * ``DRAW_WIN_SWAP`` Draw Window + Swap, Draw Window and Swap. * ``ANIM_STEP`` Anim Step, Animation Steps. * ``ANIM_PLAY`` Anim Play, Animation Playback. * ``UNDO`` Undo/Redo, Undo/Redo.
    :type type: typing.Optional[typing.Any]
    :param iterations: Iterations, Number of times to redraw
    :type iterations: typing.Optional[typing.Any]
    :param time_limit: Time Limit, Seconds to run the test for (override iterations)
    :type time_limit: typing.Optional[typing.Any]
    '''

    pass


def revert_mainfile(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    use_scripts: typing.Union[bool, typing.Any] = True):
    ''' Reload the saved file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param use_scripts: Trusted Source, Allow .blend file to execute scripts automatically, default available from system preferences
    :type use_scripts: typing.Union[bool, typing.Any]
    '''

    pass


def save_as_mainfile(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Union[bool, typing.Any] = True,
        filter_blender: typing.Union[bool, typing.Any] = True,
        filter_backup: typing.Union[bool, typing.Any] = False,
        filter_image: typing.Union[bool, typing.Any] = False,
        filter_movie: typing.Union[bool, typing.Any] = False,
        filter_python: typing.Union[bool, typing.Any] = False,
        filter_font: typing.Union[bool, typing.Any] = False,
        filter_sound: typing.Union[bool, typing.Any] = False,
        filter_text: typing.Union[bool, typing.Any] = False,
        filter_btx: typing.Union[bool, typing.Any] = False,
        filter_collada: typing.Union[bool, typing.Any] = False,
        filter_alembic: typing.Union[bool, typing.Any] = False,
        filter_folder: typing.Union[bool, typing.Any] = True,
        filter_blenlib: typing.Union[bool, typing.Any] = False,
        filemode: typing.Optional[typing.Any] = 8,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
        compress: typing.Union[bool, typing.Any] = False,
        relative_remap: typing.Union[bool, typing.Any] = True,
        copy: typing.Union[bool, typing.Any] = False,
        use_mesh_compat: typing.Union[bool, typing.Any] = False):
    ''' Save the current file in the desired location

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
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    :param compress: Compress, Write compressed .blend file
    :type compress: typing.Union[bool, typing.Any]
    :param relative_remap: Remap Relative, Remap relative paths when saving in a different directory
    :type relative_remap: typing.Union[bool, typing.Any]
    :param copy: Save Copy, Save a copy of the actual working state but does not make saved file active
    :type copy: typing.Union[bool, typing.Any]
    :param use_mesh_compat: Legacy Mesh Format, Save using legacy mesh format (no ngons) - WARNING: only saves tris and quads, other ngons will be lost (no implicit triangulation)
    :type use_mesh_compat: typing.Union[bool, typing.Any]
    '''

    pass


def save_homefile(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Make the current file the default .blend file, includes preferences

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def save_mainfile(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  filepath: typing.Union[str, typing.Any] = "",
                  check_existing: typing.Union[bool, typing.Any] = True,
                  filter_blender: typing.Union[bool, typing.Any] = True,
                  filter_backup: typing.Union[bool, typing.Any] = False,
                  filter_image: typing.Union[bool, typing.Any] = False,
                  filter_movie: typing.Union[bool, typing.Any] = False,
                  filter_python: typing.Union[bool, typing.Any] = False,
                  filter_font: typing.Union[bool, typing.Any] = False,
                  filter_sound: typing.Union[bool, typing.Any] = False,
                  filter_text: typing.Union[bool, typing.Any] = False,
                  filter_btx: typing.Union[bool, typing.Any] = False,
                  filter_collada: typing.Union[bool, typing.Any] = False,
                  filter_alembic: typing.Union[bool, typing.Any] = False,
                  filter_folder: typing.Union[bool, typing.Any] = True,
                  filter_blenlib: typing.Union[bool, typing.Any] = False,
                  filemode: typing.Optional[typing.Any] = 8,
                  display_type: typing.Optional[typing.Any] = 'DEFAULT',
                  sort_method: typing.Optional[typing.Any] = 'FILE_SORT_ALPHA',
                  compress: typing.Union[bool, typing.Any] = False,
                  relative_remap: typing.Union[bool, typing.Any] = False):
    ''' Save the current Blender file

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
    :param display_type: Display Type * ``DEFAULT`` Default, Automatically determine display type for files. * ``LIST_SHORT`` Short List, Display files as short list. * ``LIST_LONG`` Long List, Display files as a detailed list. * ``THUMBNAIL`` Thumbnails, Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode * ``FILE_SORT_ALPHA`` Sort alphabetically, Sort the file list alphabetically. * ``FILE_SORT_EXTENSION`` Sort by extension, Sort the file list by extension/type. * ``FILE_SORT_TIME`` Sort by time, Sort files by modification time. * ``FILE_SORT_SIZE`` Sort by size, Sort files by size.
    :type sort_method: typing.Optional[typing.Any]
    :param compress: Compress, Write compressed .blend file
    :type compress: typing.Union[bool, typing.Any]
    :param relative_remap: Remap Relative, Remap relative paths when saving in a different directory
    :type relative_remap: typing.Union[bool, typing.Any]
    '''

    pass


def save_userpref(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Save user preferences separately, overrides startup file preferences

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def search_menu(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Pop-up a search menu over all available operators in current context

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_stereo_3d(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        display_mode: typing.Optional[typing.Any] = 'ANAGLYPH',
        anaglyph_type: typing.Optional[typing.Any] = 'RED_CYAN',
        interlace_type: typing.Optional[typing.Any] = 'ROW_INTERLEAVED',
        use_interlace_swap: typing.Union[bool, typing.Any] = False,
        use_sidebyside_crosseyed: typing.Union[bool, typing.Any] = False):
    ''' Toggle 3D stereo support for current window (or change the display mode)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param display_mode: Display Mode * ``ANAGLYPH`` Anaglyph, Render views for left and right eyes as two differently filtered colors in a single image (anaglyph glasses are required). * ``INTERLACE`` Interlace, Render views for left and right eyes interlaced in a single image (3D-ready monitor is required). * ``TIMESEQUENTIAL`` Time Sequential, Render alternate eyes (also known as page flip, quad buffer support in the graphic card is required). * ``SIDEBYSIDE`` Side-by-Side, Render views for left and right eyes side-by-side. * ``TOPBOTTOM`` Top-Bottom, Render views for left and right eyes one above another.
    :type display_mode: typing.Optional[typing.Any]
    :param anaglyph_type: Anaglyph Type
    :type anaglyph_type: typing.Optional[typing.Any]
    :param interlace_type: Interlace Type
    :type interlace_type: typing.Optional[typing.Any]
    :param use_interlace_swap: Swap Left/Right, Swap left and right stereo channels
    :type use_interlace_swap: typing.Union[bool, typing.Any]
    :param use_sidebyside_crosseyed: Cross-Eyed, Right eye should see left image and vice-versa
    :type use_sidebyside_crosseyed: typing.Union[bool, typing.Any]
    '''

    pass


def splash(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None):
    ''' Open the splash screen with release info

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def sysinfo(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: typing.Optional[bool] = None,
            *,
            filepath: typing.Union[str, typing.Any] = ""):
    ''' Generate system information, saved into a text file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    '''

    pass


def theme_install(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  overwrite: typing.Union[bool, typing.Any] = True,
                  filepath: typing.Union[str, typing.Any] = "",
                  filter_folder: typing.Union[bool, typing.Any] = True,
                  filter_glob: typing.Union[str, typing.Any] = "*.xml"):
    ''' Load and apply a Blender XML theme file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param overwrite: Overwrite, Remove existing theme file if exists
    :type overwrite: typing.Union[bool, typing.Any]
    :param filepath: filepath
    :type filepath: typing.Union[str, typing.Any]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Union[bool, typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    '''

    pass


def url_open(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             url: typing.Union[str, typing.Any] = ""):
    ''' Open a website in the web-browser

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param url: URL, URL to open
    :type url: typing.Union[str, typing.Any]
    '''

    pass


def userpref_autoexec_path_add(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Add path to exclude from autoexecution

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def userpref_autoexec_path_remove(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        index: typing.Optional[typing.Any] = 0):
    ''' Remove path to exclude from autoexecution

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param index: Index
    :type index: typing.Optional[typing.Any]
    '''

    pass


def window_close(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None):
    ''' Close the current Blender window

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def window_duplicate(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Duplicate the current Blender window

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def window_fullscreen_toggle(override_context: typing.
                             Union[typing.Dict, 'bpy.types.Context'] = None,
                             execution_context: typing.Union[str, int] = None,
                             undo: typing.Optional[bool] = None):
    ''' Toggle the current window fullscreen

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
