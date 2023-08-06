import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class AddPresetBase:
    bl_options = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass


class ExecutePreset(bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_rna = None
    ''' '''

    filepath = None
    ''' '''

    id_data = None
    ''' '''

    menu_idname = None
    ''' '''

    order = None
    ''' '''

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class WM_MT_operator_presets(bpy_types.Menu, bpy_types._GenericUI):
    bl_label = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    preset_operator = None
    ''' '''

    preset_subdir = None
    ''' '''

    def append(self, draw_func):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def draw(self, context):
        ''' 

        '''
        pass

    def draw_collapsible(self, context, layout):
        ''' 

        '''
        pass

    def draw_preset(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_menu(self, searchpaths, operator, props_default, filter_ext):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def prepend(self, draw_func):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def remove(self, draw_func):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetCamera(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    use_focal_length = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetCloth(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetFluid(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetHairDynamics(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetInteraction(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetInterfaceTheme(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetKeyconfig(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    remove_active = None
    ''' '''

    def add(self, context, filepath):
        ''' 

        '''
        pass

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def post_cb(self, context):
        ''' 

        '''
        pass

    def pre_cb(self, context):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetNodeColor(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetOperator(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    operator = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def operator_path(self, operator):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetRender(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetSSS(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetSafeAreas(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetSunSky(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetTrackingCamera(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    use_focal_length = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetTrackingSettings(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetTrackingTrackColor(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class AddPresetUnitsLength(AddPresetBase, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    name = None
    ''' '''

    order = None
    ''' '''

    preset_defines = None
    ''' '''

    preset_menu = None
    ''' '''

    preset_subdir = None
    ''' '''

    preset_values = None
    ''' '''

    remove_active = None
    ''' '''

    def as_filename(self, name):
        ''' 

        '''
        pass

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def check(self, context):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass
