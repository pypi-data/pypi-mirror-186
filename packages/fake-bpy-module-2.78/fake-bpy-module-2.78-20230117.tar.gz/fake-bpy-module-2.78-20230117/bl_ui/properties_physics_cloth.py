import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class CLOTH_MT_presets(bpy_types.Menu, bpy_types._GenericUI):
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


class PhysicButtonsPanel:
    bl_context = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_space_type = None
    ''' '''

    def poll(self, context):
        ''' 

        '''
        pass


class PHYSICS_PT_cloth(PhysicButtonsPanel, bpy_types.Panel,
                       bpy_types._GenericUI):
    COMPAT_ENGINES = None
    ''' '''

    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
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

    def path_resolve(self):
        ''' 

        '''
        pass

    def poll(self, context):
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


class PHYSICS_PT_cloth_cache(PhysicButtonsPanel, bpy_types.Panel,
                             bpy_types._GenericUI):
    COMPAT_ENGINES = None
    ''' '''

    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
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

    def path_resolve(self):
        ''' 

        '''
        pass

    def poll(self, context):
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


class PHYSICS_PT_cloth_collision(PhysicButtonsPanel, bpy_types.Panel,
                                 bpy_types._GenericUI):
    COMPAT_ENGINES = None
    ''' '''

    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
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

    def draw_header(self, context):
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

    def path_resolve(self):
        ''' 

        '''
        pass

    def poll(self, context):
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


class PHYSICS_PT_cloth_field_weights(PhysicButtonsPanel, bpy_types.Panel,
                                     bpy_types._GenericUI):
    COMPAT_ENGINES = None
    ''' '''

    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
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

    def path_resolve(self):
        ''' 

        '''
        pass

    def poll(self, context):
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


class PHYSICS_PT_cloth_sewing(PhysicButtonsPanel, bpy_types.Panel,
                              bpy_types._GenericUI):
    COMPAT_ENGINES = None
    ''' '''

    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
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

    def draw_header(self, context):
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

    def path_resolve(self):
        ''' 

        '''
        pass

    def poll(self, context):
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


class PHYSICS_PT_cloth_stiffness(PhysicButtonsPanel, bpy_types.Panel,
                                 bpy_types._GenericUI):
    COMPAT_ENGINES = None
    ''' '''

    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
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

    def draw_header(self, context):
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

    def path_resolve(self):
        ''' 

        '''
        pass

    def poll(self, context):
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


def cloth_panel_enabled(md):
    ''' 

    '''

    pass
