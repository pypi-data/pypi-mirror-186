import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class UnifiedPaintPanel:
    def paint_settings(self, context):
        ''' 

        '''
        pass

    def prop_unified_color(self, parent, context, brush, prop_name, text):
        ''' 

        '''
        pass

    def prop_unified_color_picker(self, parent, context, brush, prop_name,
                                  value_slider):
        ''' 

        '''
        pass

    def prop_unified_size(self, parent, context, brush, prop_name, icon, text,
                          slider):
        ''' 

        '''
        pass

    def prop_unified_strength(self, parent, context, brush, prop_name, icon,
                              text, slider):
        ''' 

        '''
        pass

    def prop_unified_weight(self, parent, context, brush, prop_name, icon,
                            text, slider):
        ''' 

        '''
        pass

    def unified_paint_settings(self, parent, context):
        ''' 

        '''
        pass


class VIEW3D_MT_tools_projectpaint_clone(bpy_types.Menu, bpy_types._GenericUI):
    bl_label = None
    ''' '''

    bl_rna = None
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


def brush_mask_texture_settings(layout, brush):
    ''' 

    '''

    pass


def brush_texpaint_common(panel, context, layout, brush, settings, projpaint):
    ''' 

    '''

    pass


def brush_texture_settings(layout, brush, sculpt):
    ''' 

    '''

    pass
