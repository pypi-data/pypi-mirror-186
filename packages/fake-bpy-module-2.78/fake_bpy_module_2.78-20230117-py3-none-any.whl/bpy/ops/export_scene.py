import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def autodesk_3ds(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 filepath: typing.Union[str, typing.Any] = "",
                 check_existing: typing.Union[bool, typing.Any] = True,
                 axis_forward: typing.Optional[typing.Any] = 'Y',
                 axis_up: typing.Optional[typing.Any] = 'Z',
                 filter_glob: typing.Union[str, typing.Any] = "*.3ds",
                 use_selection: typing.Union[bool, typing.Any] = False):
    ''' Export to 3DS file format (.3ds)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param use_selection: Selection Only, Export selected objects only
    :type use_selection: typing.Union[bool, typing.Any]
    '''

    pass


def fbx(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Union[bool, typing.Any] = True,
        axis_forward: typing.Optional[typing.Any] = '-Z',
        axis_up: typing.Optional[typing.Any] = 'Y',
        filter_glob: typing.Union[str, typing.Any] = "*.fbx",
        version: typing.Optional[typing.Any] = 'BIN7400',
        ui_tab: typing.Optional[typing.Any] = 'MAIN',
        use_selection: typing.Union[bool, typing.Any] = False,
        global_scale: typing.Optional[typing.Any] = 1.0,
        apply_unit_scale: typing.Union[bool, typing.Any] = True,
        bake_space_transform: typing.Union[bool, typing.Any] = False,
        object_types: typing.Optional[typing.Any] = {
            'ARMATURE', 'CAMERA', 'EMPTY', 'LAMP', 'MESH', 'OTHER'
        },
        use_mesh_modifiers: typing.Union[bool, typing.Any] = True,
        mesh_smooth_type: typing.Optional[typing.Any] = 'OFF',
        use_mesh_edges: typing.Union[bool, typing.Any] = False,
        use_tspace: typing.Union[bool, typing.Any] = False,
        use_custom_props: typing.Union[bool, typing.Any] = False,
        add_leaf_bones: typing.Union[bool, typing.Any] = True,
        primary_bone_axis: typing.Optional[typing.Any] = 'Y',
        secondary_bone_axis: typing.Optional[typing.Any] = 'X',
        use_armature_deform_only: typing.Union[bool, typing.Any] = False,
        armature_nodetype: typing.Optional[typing.Any] = 'NULL',
        bake_anim: typing.Union[bool, typing.Any] = True,
        bake_anim_use_all_bones: typing.Union[bool, typing.Any] = True,
        bake_anim_use_nla_strips: typing.Union[bool, typing.Any] = True,
        bake_anim_use_all_actions: typing.Union[bool, typing.Any] = True,
        bake_anim_force_startend_keying: typing.Union[bool, typing.Any] = True,
        bake_anim_step: typing.Optional[typing.Any] = 1.0,
        bake_anim_simplify_factor: typing.Optional[typing.Any] = 1.0,
        use_anim: typing.Union[bool, typing.Any] = True,
        use_anim_action_all: typing.Union[bool, typing.Any] = True,
        use_default_take: typing.Union[bool, typing.Any] = True,
        use_anim_optimize: typing.Union[bool, typing.Any] = True,
        anim_optimize_precision: typing.Optional[typing.Any] = 6.0,
        path_mode: typing.Optional[typing.Any] = 'AUTO',
        embed_textures: typing.Union[bool, typing.Any] = False,
        batch_mode: typing.Optional[typing.Any] = 'OFF',
        use_batch_own_dir: typing.Union[bool, typing.Any] = True,
        use_metadata: typing.Union[bool, typing.Any] = True):
    ''' Write a FBX file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param version: Version, Choose which version of the exporter to use * ``BIN7400`` FBX 7.4 binary, Modern 7.4 binary version. * ``ASCII6100`` FBX 6.1 ASCII, Legacy 6.1 ascii version - WARNING: Deprecated and no more maintained.
    :type version: typing.Optional[typing.Any]
    :param ui_tab: ui_tab, Export options categories * ``MAIN`` Main, Main basic settings. * ``GEOMETRY`` Geometries, Geometry-related settings. * ``ARMATURE`` Armatures, Armature-related settings. * ``ANIMATION`` Animation, Animation-related settings.
    :type ui_tab: typing.Optional[typing.Any]
    :param use_selection: Selected Objects, Export selected objects on visible layers
    :type use_selection: typing.Union[bool, typing.Any]
    :param global_scale: Scale, Scale all data (Some importers do not support scaled armatures!)
    :type global_scale: typing.Optional[typing.Any]
    :param apply_unit_scale: Apply Unit, Scale all data according to current Blender size, to match default FBX unit (centimeter, some importers do not handle UnitScaleFactor properly)
    :type apply_unit_scale: typing.Union[bool, typing.Any]
    :param bake_space_transform: !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)
    :type bake_space_transform: typing.Union[bool, typing.Any]
    :param object_types: Object Types, Which kind of object to export * ``EMPTY`` Empty. * ``CAMERA`` Camera. * ``LAMP`` Lamp. * ``ARMATURE`` Armature, WARNING: not supported in dupli/group instances. * ``MESH`` Mesh. * ``OTHER`` Other, Other geometry types, like curve, metaball, etc. (converted to meshes).
    :type object_types: typing.Optional[typing.Any]
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys
    :type use_mesh_modifiers: typing.Union[bool, typing.Any]
    :param mesh_smooth_type: Smoothing, Export smoothing information (prefer 'Normals Only' option if your target importer understand split normals) * ``OFF`` Normals Only, Export only normals instead of writing edge or face smoothing data. * ``FACE`` Face, Write face smoothing. * ``EDGE`` Edge, Write edge smoothing.
    :type mesh_smooth_type: typing.Optional[typing.Any]
    :param use_mesh_edges: Loose Edges, Export loose edges (as two-vertices polygons)
    :type use_mesh_edges: typing.Union[bool, typing.Any]
    :param use_tspace: Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)
    :type use_tspace: typing.Union[bool, typing.Any]
    :param use_custom_props: Custom Properties, Export custom properties
    :type use_custom_props: typing.Union[bool, typing.Any]
    :param add_leaf_bones: Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)
    :type add_leaf_bones: typing.Union[bool, typing.Any]
    :param primary_bone_axis: Primary Bone Axis
    :type primary_bone_axis: typing.Optional[typing.Any]
    :param secondary_bone_axis: Secondary Bone Axis
    :type secondary_bone_axis: typing.Optional[typing.Any]
    :param use_armature_deform_only: Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children)
    :type use_armature_deform_only: typing.Union[bool, typing.Any]
    :param armature_nodetype: Armature FBXNode Type, FBX type of node (object) used to represent Blender's armatures (use Null one unless you experience issues with other app, other choices may no import back perfectly in Blender...) * ``NULL`` Null, 'Null' FBX node, similar to Blender's Empty (default). * ``ROOT`` Root, 'Root' FBX node, supposed to be the root of chains of bones.... * ``LIMBNODE`` LimbNode, 'LimbNode' FBX node, a regular joint between two bones....
    :type armature_nodetype: typing.Optional[typing.Any]
    :param bake_anim: Baked Animation, Export baked keyframe animation
    :type bake_anim: typing.Union[bool, typing.Any]
    :param bake_anim_use_all_bones: Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)
    :type bake_anim_use_all_bones: typing.Union[bool, typing.Any]
    :param bake_anim_use_nla_strips: NLA Strips, Export each non-muted NLA strip as a separated FBX's AnimStack, if any, instead of global scene animation
    :type bake_anim_use_nla_strips: typing.Union[bool, typing.Any]
    :param bake_anim_use_all_actions: All Actions, Export each action as a separated FBX's AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)
    :type bake_anim_use_all_actions: typing.Union[bool, typing.Any]
    :param bake_anim_force_startend_keying: Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels
    :type bake_anim_force_startend_keying: typing.Union[bool, typing.Any]
    :param bake_anim_step: Sampling Rate, How often to evaluate animated values (in frames)
    :type bake_anim_step: typing.Optional[typing.Any]
    :param bake_anim_simplify_factor: Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified)
    :type bake_anim_simplify_factor: typing.Optional[typing.Any]
    :param use_anim: Animation, Export keyframe animation
    :type use_anim: typing.Union[bool, typing.Any]
    :param use_anim_action_all: All Actions, Export all actions for armatures or just the currently selected action
    :type use_anim_action_all: typing.Union[bool, typing.Any]
    :param use_default_take: Default Take, Export currently assigned object and armature animations into a default take from the scene start/end frames
    :type use_default_take: typing.Union[bool, typing.Any]
    :param use_anim_optimize: Optimize Keyframes, Remove double keyframes
    :type use_anim_optimize: typing.Union[bool, typing.Any]
    :param anim_optimize_precision: Precision, Tolerance for comparing double keyframes (higher for greater accuracy)
    :type anim_optimize_precision: typing.Optional[typing.Any]
    :param path_mode: Path Mode, Method used to reference paths * ``AUTO`` Auto, Use Relative paths with subdirectories only. * ``ABSOLUTE`` Absolute, Always write absolute paths. * ``RELATIVE`` Relative, Always write relative paths (where possible). * ``MATCH`` Match, Match Absolute/Relative setting with input path. * ``STRIP`` Strip Path, Filename only. * ``COPY`` Copy, Copy the file to the destination path (or subdirectory).
    :type path_mode: typing.Optional[typing.Any]
    :param embed_textures: Embed Textures, Embed textures in FBX binary file (only for "Copy" path mode!)
    :type embed_textures: typing.Union[bool, typing.Any]
    :param batch_mode: Batch Mode * ``OFF`` Off, Active scene to file. * ``SCENE`` Scene, Each scene as a file. * ``GROUP`` Group, Each group as a file.
    :type batch_mode: typing.Optional[typing.Any]
    :param use_batch_own_dir: Batch Own Dir, Create a dir for each exported file
    :type use_batch_own_dir: typing.Union[bool, typing.Any]
    :param use_metadata: Use Metadata
    :type use_metadata: typing.Union[bool, typing.Any]
    '''

    pass


def obj(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Union[bool, typing.Any] = True,
        axis_forward: typing.Optional[typing.Any] = '-Z',
        axis_up: typing.Optional[typing.Any] = 'Y',
        filter_glob: typing.Union[str, typing.Any] = "*.obj;*.mtl",
        use_selection: typing.Union[bool, typing.Any] = False,
        use_animation: typing.Union[bool, typing.Any] = False,
        use_mesh_modifiers: typing.Union[bool, typing.Any] = True,
        use_edges: typing.Union[bool, typing.Any] = True,
        use_smooth_groups: typing.Union[bool, typing.Any] = False,
        use_smooth_groups_bitflags: typing.Union[bool, typing.Any] = False,
        use_normals: typing.Union[bool, typing.Any] = True,
        use_uvs: typing.Union[bool, typing.Any] = True,
        use_materials: typing.Union[bool, typing.Any] = True,
        use_triangles: typing.Union[bool, typing.Any] = False,
        use_nurbs: typing.Union[bool, typing.Any] = False,
        use_vertex_groups: typing.Union[bool, typing.Any] = False,
        use_blen_objects: typing.Union[bool, typing.Any] = True,
        group_by_object: typing.Union[bool, typing.Any] = False,
        group_by_material: typing.Union[bool, typing.Any] = False,
        keep_vertex_order: typing.Union[bool, typing.Any] = False,
        global_scale: typing.Optional[typing.Any] = 1.0,
        path_mode: typing.Optional[typing.Any] = 'AUTO'):
    ''' Save a Wavefront OBJ File

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param use_selection: Selection Only, Export selected objects only
    :type use_selection: typing.Union[bool, typing.Any]
    :param use_animation: Animation, Write out an OBJ for each frame
    :type use_animation: typing.Union[bool, typing.Any]
    :param use_mesh_modifiers: Apply Modifiers, Apply modifiers (preview resolution)
    :type use_mesh_modifiers: typing.Union[bool, typing.Any]
    :param use_edges: Include Edges
    :type use_edges: typing.Union[bool, typing.Any]
    :param use_smooth_groups: Smooth Groups, Write sharp edges as smooth groups
    :type use_smooth_groups: typing.Union[bool, typing.Any]
    :param use_smooth_groups_bitflags: Bitflag Smooth Groups, Same as 'Smooth Groups', but generate smooth groups IDs as bitflags (produces at most 32 different smooth groups, usually much less)
    :type use_smooth_groups_bitflags: typing.Union[bool, typing.Any]
    :param use_normals: Write Normals, Export one normal per vertex and per face, to represent flat faces and sharp edges
    :type use_normals: typing.Union[bool, typing.Any]
    :param use_uvs: Include UVs, Write out the active UV coordinates
    :type use_uvs: typing.Union[bool, typing.Any]
    :param use_materials: Write Materials, Write out the MTL file
    :type use_materials: typing.Union[bool, typing.Any]
    :param use_triangles: Triangulate Faces, Convert all faces to triangles
    :type use_triangles: typing.Union[bool, typing.Any]
    :param use_nurbs: Write Nurbs, Write nurbs curves as OBJ nurbs rather than converting to geometry
    :type use_nurbs: typing.Union[bool, typing.Any]
    :param use_vertex_groups: Polygroups
    :type use_vertex_groups: typing.Union[bool, typing.Any]
    :param use_blen_objects: Objects as OBJ Objects
    :type use_blen_objects: typing.Union[bool, typing.Any]
    :param group_by_object: Objects as OBJ Groups
    :type group_by_object: typing.Union[bool, typing.Any]
    :param group_by_material: Material Groups
    :type group_by_material: typing.Union[bool, typing.Any]
    :param keep_vertex_order: Keep Vertex Order
    :type keep_vertex_order: typing.Union[bool, typing.Any]
    :param global_scale: Scale
    :type global_scale: typing.Optional[typing.Any]
    :param path_mode: Path Mode, Method used to reference paths * ``AUTO`` Auto, Use Relative paths with subdirectories only. * ``ABSOLUTE`` Absolute, Always write absolute paths. * ``RELATIVE`` Relative, Always write relative paths (where possible). * ``MATCH`` Match, Match Absolute/Relative setting with input path. * ``STRIP`` Strip Path, Filename only. * ``COPY`` Copy, Copy the file to the destination path (or subdirectory).
    :type path_mode: typing.Optional[typing.Any]
    '''

    pass


def x3d(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Union[bool, typing.Any] = True,
        axis_forward: typing.Optional[typing.Any] = 'Z',
        axis_up: typing.Optional[typing.Any] = 'Y',
        filter_glob: typing.Union[str, typing.Any] = "*.x3d",
        use_selection: typing.Union[bool, typing.Any] = False,
        use_mesh_modifiers: typing.Union[bool, typing.Any] = True,
        use_triangulate: typing.Union[bool, typing.Any] = False,
        use_normals: typing.Union[bool, typing.Any] = False,
        use_compress: typing.Union[bool, typing.Any] = False,
        use_hierarchy: typing.Union[bool, typing.Any] = True,
        name_decorations: typing.Union[bool, typing.Any] = True,
        use_h3d: typing.Union[bool, typing.Any] = False,
        global_scale: typing.Optional[typing.Any] = 1.0,
        path_mode: typing.Optional[typing.Any] = 'AUTO'):
    ''' Export selection to Extensible 3D file (.x3d)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Union[bool, typing.Any]
    :param axis_forward: Forward
    :type axis_forward: typing.Optional[typing.Any]
    :param axis_up: Up
    :type axis_up: typing.Optional[typing.Any]
    :param filter_glob: filter_glob
    :type filter_glob: typing.Union[str, typing.Any]
    :param use_selection: Selection Only, Export selected objects only
    :type use_selection: typing.Union[bool, typing.Any]
    :param use_mesh_modifiers: Apply Modifiers, Use transformed mesh data from each object
    :type use_mesh_modifiers: typing.Union[bool, typing.Any]
    :param use_triangulate: Triangulate, Write quads into 'IndexedTriangleSet'
    :type use_triangulate: typing.Union[bool, typing.Any]
    :param use_normals: Normals, Write normals with geometry
    :type use_normals: typing.Union[bool, typing.Any]
    :param use_compress: Compress, Compress the exported file
    :type use_compress: typing.Union[bool, typing.Any]
    :param use_hierarchy: Hierarchy, Export parent child relationships
    :type use_hierarchy: typing.Union[bool, typing.Any]
    :param name_decorations: Name decorations, Add prefixes to the names of exported nodes to indicate their type
    :type name_decorations: typing.Union[bool, typing.Any]
    :param use_h3d: H3D Extensions, Export shaders for H3D
    :type use_h3d: typing.Union[bool, typing.Any]
    :param global_scale: Scale
    :type global_scale: typing.Optional[typing.Any]
    :param path_mode: Path Mode, Method used to reference paths * ``AUTO`` Auto, Use Relative paths with subdirectories only. * ``ABSOLUTE`` Absolute, Always write absolute paths. * ``RELATIVE`` Relative, Always write relative paths (where possible). * ``MATCH`` Match, Match Absolute/Relative setting with input path. * ``STRIP`` Strip Path, Filename only. * ``COPY`` Copy, Copy the file to the destination path (or subdirectory).
    :type path_mode: typing.Optional[typing.Any]
    '''

    pass
