import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class ConstraintButtonsPanel:
    bl_context = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_space_type = None
    ''' '''

    def ACTION(self, context, layout, con):
        ''' 

        '''
        pass

    def CAMERA_SOLVER(self, context, layout, con):
        ''' 

        '''
        pass

    def CHILD_OF(self, context, layout, con):
        ''' 

        '''
        pass

    def CLAMP_TO(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_LOCATION(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_ROTATION(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_SCALE(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_TRANSFORMS(self, context, layout, con):
        ''' 

        '''
        pass

    def DAMPED_TRACK(self, context, layout, con):
        ''' 

        '''
        pass

    def FLOOR(self, context, layout, con):
        ''' 

        '''
        pass

    def FOLLOW_PATH(self, context, layout, con):
        ''' 

        '''
        pass

    def FOLLOW_TRACK(self, context, layout, con):
        ''' 

        '''
        pass

    def IK(self, context, layout, con):
        ''' 

        '''
        pass

    def IK_COPY_POSE(self, context, layout, con):
        ''' 

        '''
        pass

    def IK_DISTANCE(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_DISTANCE(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_LOCATION(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_ROTATION(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_SCALE(self, context, layout, con):
        ''' 

        '''
        pass

    def LOCKED_TRACK(self, context, layout, con):
        ''' 

        '''
        pass

    def MAINTAIN_VOLUME(self, context, layout, con):
        ''' 

        '''
        pass

    def OBJECT_SOLVER(self, context, layout, con):
        ''' 

        '''
        pass

    def PIVOT(self, context, layout, con):
        ''' 

        '''
        pass

    def RIGID_BODY_JOINT(self, context, layout, con):
        ''' 

        '''
        pass

    def SCRIPT(self, context, layout, con):
        ''' 

        '''
        pass

    def SHRINKWRAP(self, context, layout, con):
        ''' 

        '''
        pass

    def SPLINE_IK(self, context, layout, con):
        ''' 

        '''
        pass

    def STRETCH_TO(self, context, layout, con):
        ''' 

        '''
        pass

    def TRACK_TO(self, context, layout, con):
        ''' 

        '''
        pass

    def TRANSFORM(self, context, layout, con):
        ''' 

        '''
        pass

    def TRANSFORM_CACHE(self, context, layout, con):
        ''' 

        '''
        pass

    def draw_constraint(self, context, con):
        ''' 

        '''
        pass

    def ik_template(self, layout, con):
        ''' 

        '''
        pass

    def space_template(self, layout, con, target, owner):
        ''' 

        '''
        pass

    def target_template(self, layout, con, subtargets):
        ''' 

        '''
        pass


class BONE_PT_constraints(ConstraintButtonsPanel, bpy_types.Panel,
                          bpy_types._GenericUI):
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

    def ACTION(self, context, layout, con):
        ''' 

        '''
        pass

    def CAMERA_SOLVER(self, context, layout, con):
        ''' 

        '''
        pass

    def CHILD_OF(self, context, layout, con):
        ''' 

        '''
        pass

    def CLAMP_TO(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_LOCATION(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_ROTATION(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_SCALE(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_TRANSFORMS(self, context, layout, con):
        ''' 

        '''
        pass

    def DAMPED_TRACK(self, context, layout, con):
        ''' 

        '''
        pass

    def FLOOR(self, context, layout, con):
        ''' 

        '''
        pass

    def FOLLOW_PATH(self, context, layout, con):
        ''' 

        '''
        pass

    def FOLLOW_TRACK(self, context, layout, con):
        ''' 

        '''
        pass

    def IK(self, context, layout, con):
        ''' 

        '''
        pass

    def IK_COPY_POSE(self, context, layout, con):
        ''' 

        '''
        pass

    def IK_DISTANCE(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_DISTANCE(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_LOCATION(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_ROTATION(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_SCALE(self, context, layout, con):
        ''' 

        '''
        pass

    def LOCKED_TRACK(self, context, layout, con):
        ''' 

        '''
        pass

    def MAINTAIN_VOLUME(self, context, layout, con):
        ''' 

        '''
        pass

    def OBJECT_SOLVER(self, context, layout, con):
        ''' 

        '''
        pass

    def PIVOT(self, context, layout, con):
        ''' 

        '''
        pass

    def RIGID_BODY_JOINT(self, context, layout, con):
        ''' 

        '''
        pass

    def SCRIPT(self, context, layout, con):
        ''' 

        '''
        pass

    def SHRINKWRAP(self, context, layout, con):
        ''' 

        '''
        pass

    def SPLINE_IK(self, context, layout, con):
        ''' 

        '''
        pass

    def STRETCH_TO(self, context, layout, con):
        ''' 

        '''
        pass

    def TRACK_TO(self, context, layout, con):
        ''' 

        '''
        pass

    def TRANSFORM(self, context, layout, con):
        ''' 

        '''
        pass

    def TRANSFORM_CACHE(self, context, layout, con):
        ''' 

        '''
        pass

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

    def draw_constraint(self, context, con):
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

    def ik_template(self, layout, con):
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

    def space_template(self, layout, con, target, owner):
        ''' 

        '''
        pass

    def target_template(self, layout, con, subtargets):
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


class OBJECT_PT_constraints(ConstraintButtonsPanel, bpy_types.Panel,
                            bpy_types._GenericUI):
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

    def ACTION(self, context, layout, con):
        ''' 

        '''
        pass

    def CAMERA_SOLVER(self, context, layout, con):
        ''' 

        '''
        pass

    def CHILD_OF(self, context, layout, con):
        ''' 

        '''
        pass

    def CLAMP_TO(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_LOCATION(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_ROTATION(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_SCALE(self, context, layout, con):
        ''' 

        '''
        pass

    def COPY_TRANSFORMS(self, context, layout, con):
        ''' 

        '''
        pass

    def DAMPED_TRACK(self, context, layout, con):
        ''' 

        '''
        pass

    def FLOOR(self, context, layout, con):
        ''' 

        '''
        pass

    def FOLLOW_PATH(self, context, layout, con):
        ''' 

        '''
        pass

    def FOLLOW_TRACK(self, context, layout, con):
        ''' 

        '''
        pass

    def IK(self, context, layout, con):
        ''' 

        '''
        pass

    def IK_COPY_POSE(self, context, layout, con):
        ''' 

        '''
        pass

    def IK_DISTANCE(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_DISTANCE(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_LOCATION(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_ROTATION(self, context, layout, con):
        ''' 

        '''
        pass

    def LIMIT_SCALE(self, context, layout, con):
        ''' 

        '''
        pass

    def LOCKED_TRACK(self, context, layout, con):
        ''' 

        '''
        pass

    def MAINTAIN_VOLUME(self, context, layout, con):
        ''' 

        '''
        pass

    def OBJECT_SOLVER(self, context, layout, con):
        ''' 

        '''
        pass

    def PIVOT(self, context, layout, con):
        ''' 

        '''
        pass

    def RIGID_BODY_JOINT(self, context, layout, con):
        ''' 

        '''
        pass

    def SCRIPT(self, context, layout, con):
        ''' 

        '''
        pass

    def SHRINKWRAP(self, context, layout, con):
        ''' 

        '''
        pass

    def SPLINE_IK(self, context, layout, con):
        ''' 

        '''
        pass

    def STRETCH_TO(self, context, layout, con):
        ''' 

        '''
        pass

    def TRACK_TO(self, context, layout, con):
        ''' 

        '''
        pass

    def TRANSFORM(self, context, layout, con):
        ''' 

        '''
        pass

    def TRANSFORM_CACHE(self, context, layout, con):
        ''' 

        '''
        pass

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

    def draw_constraint(self, context, con):
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

    def ik_template(self, layout, con):
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

    def space_template(self, layout, con, target, owner):
        ''' 

        '''
        pass

    def target_template(self, layout, con, subtargets):
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
