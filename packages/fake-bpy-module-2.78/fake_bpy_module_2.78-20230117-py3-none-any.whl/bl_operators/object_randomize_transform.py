import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class RandomizeLocRotSize(bpy_types.Operator):
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

    loc = None
    ''' '''

    order = None
    ''' '''

    random_seed = None
    ''' '''

    rot = None
    ''' '''

    scale = None
    ''' '''

    scale_even = None
    ''' '''

    use_delta = None
    ''' '''

    use_loc = None
    ''' '''

    use_rot = None
    ''' '''

    use_scale = None
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


def randomize_selected(context, seed, delta, loc, rot, scale, scale_even,
                       scale_min):
    ''' 

    '''

    pass
