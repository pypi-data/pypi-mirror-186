import sys
import typing
import bpy.types

from . import offscreen

GenericType = typing.TypeVar("GenericType")


def export_shader(scene: 'bpy.types.Scene',
                  material: 'bpy.types.Material') -> typing.Any:
    ''' Extracts the GLSL shader producing the visual effect of material in scene for the purpose of reusing the shader in an external engine. This function is meant to be used in material exporter so that the GLSL shader can be exported entirely. The return value is a dictionary containing the shader source code and all associated data. The dictionary contains the following elements: - ``["fragment"]``: string fragment shader source code. - ``["vertex"]``: string vertex shader source code. - ``["uniforms"]``: sequence list of uniforms used in fragment shader, can be empty list. Each element of the sequence is a dictionary with the following elements: - ``["varname"]``: string name of the uniform in the fragment shader. Always of the form 'unf<number>'. - ``["datatype"]``: integer data type of the uniform variable. Can be one of the following: .. hlist:: :columns: 2 - :data:`gpu.GPU_DATA_1I` : use ``glUniform1i`` - :data:`gpu.GPU_DATA_1F` : use ``glUniform1fv`` - :data:`gpu.GPU_DATA_2F` : use ``glUniform2fv`` - :data:`gpu.GPU_DATA_3F` : use ``glUniform3fv`` - :data:`gpu.GPU_DATA_4F` : use ``glUniform4fv`` - :data:`gpu.GPU_DATA_9F` : use ``glUniformMatrix3fv`` - :data:`gpu.GPU_DATA_16F` : use ``glUniformMatrix4fv`` - ``["type"]``: integer type of uniform, determines the origin and method of calculation. See uniform-type_. Depending on the type, more elements will be be present. - ``["lamp"]``: `bpy.types.Object` Reference to the lamp object from which the uniforms value are extracted. Set for the following uniforms types: .. hlist:: :columns: 2 - :data:`gpu.GPU_DYNAMIC_LAMP_DYNVEC` - :data:`gpu.GPU_DYNAMIC_LAMP_DYNCO` - :data:`gpu.GPU_DYNAMIC_LAMP_DYNIMAT` - :data:`gpu.GPU_DYNAMIC_LAMP_DYNPERSMAT` - :data:`gpu.GPU_DYNAMIC_LAMP_DYNENERGY` - :data:`gpu.GPU_DYNAMIC_LAMP_DYNCOL` - :data:`gpu.GPU_DYNAMIC_SAMPLER_2DSHADOW` Notes: - The uniforms :data:`gpu.GPU_DYNAMIC_LAMP_DYNVEC`, :data:`gpu.GPU_DYNAMIC_LAMP_DYNCO`, :data:`gpu.GPU_DYNAMIC_LAMP_DYNIMAT` and :data:`gpu.GPU_DYNAMIC_LAMP_DYNPERSMAT` refer to the lamp object position and orientation, both of can be derived from the object world matrix: .. code-block:: python obmat = uniform["lamp"].matrix_world where obmat is the mat4_lamp_to_world_ matrix of the lamp as a 2 dimensional array, the lamp world location location is in ``obmat[3]``. - The uniform types :data:`gpu.GPU_DYNAMIC_LAMP_DYNENERGY` and :data:`gpu.GPU_DYNAMIC_LAMP_DYNCOL` refer to the lamp data bloc that you get from: .. code-block:: python la = uniform["lamp"].data from which you get ``lamp.energy`` and ``lamp.color`` - Lamp duplication is not supported: if you have duplicated lamps in your scene (i.e. lamp that are instantiated by dupligroup, etc), this element will only give you a reference to the orignal lamp and you will not know which instance of the lamp it is refering too. You can still handle that case in the exporter by distributing the uniforms amongst the duplicated lamps. - ``["image"]``: `bpy.types.Image` Reference to the image databloc. Set for uniform type :data:`gpu.GPU_DYNAMIC_SAMPLER_2DIMAGE`. You can get the image data from: .. code-block:: python # full path to image file uniform["image"].filepath # image size as a 2-dimensional array of int uniform["image"].size - ``["texnumber"]``: integer Channel number to which the texture is bound when drawing the object. Set for uniform types :data:`gpu.GPU_DYNAMIC_SAMPLER_2DBUFFER`, :data:`gpu.GPU_DYNAMIC_SAMPLER_2DIMAGE` and :data:`gpu.GPU_DYNAMIC_SAMPLER_2DSHADOW`. This is provided for information only: when reusing the shader outside blencer, you are free to assign the textures to the channel of your choice and to pass that number channel to the GPU in the uniform. - ``["texpixels"]``: byte array texture data for uniform type :data:`gpu.GPU_DYNAMIC_SAMPLER_2DBUFFER`. Although the corresponding uniform is a 2D sampler, the texture is always a 1D texture of n x 1 pixel. The texture size n is provided in ["texsize"] element. These texture are only used for computer generated texture (colorband, etc). The texture data is provided so that you can make a real image out of it in the exporter. - ``["texsize"]``: integer horizontal size of texture for uniform type :data:`gpu.GPU_DYNAMIC_SAMPLER_2DBUFFER`. The texture data is in ["texpixels"]. - ``["attributes"]``: sequence list of attributes used in vertex shader, can be empty. Blender doesn't use standard attributes except for vertex position and normal. All other vertex attributes must be passed using the generic ``glVertexAttrib`` functions. The attribute data can be found in the derived mesh custom data using RNA. Each element of the sequence is a dictionary containing the following elements: - ``["varname"]``: string name of the uniform in the vertex shader. Always of the form 'att<number>'. - ``["datatype"]``: integer data type of vertex attribute, can be one of the following: - :data:`gpu.GPU_DATA_2F`: use ``glVertexAttrib2fv`` - :data:`gpu.GPU_DATA_3F`: use ``glVertexAttrib3fv`` - :data:`gpu.GPU_DATA_4F`: use ``glVertexAttrib4fv`` - :data:`gpu.GPU_DATA_4UB`: use ``glVertexAttrib4ubv`` - ``["number"]``: integer Generic attribute number. This is provided for information only. Blender doesn't use ``glBindAttribLocation`` to place generic attributes at specific location, it lets the shader compiler place the attributes automatically and query the placement with ``glGetAttribLocation``. The result of this placement is returned in this element. When using this shader in a render engine, you should either use ``glBindAttribLocation`` to force the attribute at this location or use ``glGetAttribLocation`` to get the placement chosen by the compiler of your GPU. - ``["type"]``: integer type of the mesh custom data from which the vertex attribute is loaded. See attribute-type_. - ``["name"]``: string or integer custom data layer name, used for attribute type :data:`gpu.CD_MTFACE` and :data:`gpu.CD_MCOL`. Example:

    :param scene: the scene in which the material in rendered.
    :type scene: 'bpy.types.Scene'
    :param material: the material that you want to export the GLSL shader
    :type material: 'bpy.types.Material'
    :rtype: typing.Any
    :return: the shader source code and all associated data in a dictionary
    '''

    pass


CD_MCOL = None
''' Vertex attribute is color layer. Data type is vector 4 unsigned byte (RGBA). There can be more than one attribute of that type, they are differenciated by name. In blender you can retrieve the attribute data with:
'''

CD_MTFACE = None
''' Vertex attribute is a UV Map. Data type is vector of 2 float. There can be more than one attribute of that type, they are differenciated by name. In blender, you can retrieve the attribute data with:
'''

CD_ORCO = None
''' Vertex attribute is original coordinates. Data type is vector 3 float. There can be only 1 attribute of that type per shader. In blender you can retrieve the attribute data with:
'''

CD_TANGENT = None
''' Vertex attribute is the tangent vector. Data type is vector 4 float. There can be only 1 attribute of that type per shader. There is currently no way to retrieve this attribute data via the RNA API but a standalone C function to compute the tangent layer from the other layers can be obtained from blender.org.
'''

GPU_DATA_16F = None
''' matrix 4x4 in column-major order
'''

GPU_DATA_1F = None
''' one float
'''

GPU_DATA_1I = None
''' one integer
'''

GPU_DATA_2F = None
''' two floats
'''

GPU_DATA_3F = None
''' three floats
'''

GPU_DATA_4F = None
''' four floats
'''

GPU_DATA_4UB = None
''' four unsigned byte
'''

GPU_DATA_9F = None
''' matrix 3x3 in column-major order
'''

GPU_DYNAMIC_AMBIENT_COLOR: typing.Any = None
''' See `bpy.types.World.ambient_color`.
'''

GPU_DYNAMIC_HORIZON_COLOR: typing.Any = None
''' See `bpy.types.World.horizon_color`.
'''

GPU_DYNAMIC_LAMP_ATT1: float = None
''' See `bpy.types.PointLamp.linear_attenuation`, `bpy.types.SpotLamp.linear_attenuation`.
'''

GPU_DYNAMIC_LAMP_ATT2: float = None
''' See `bpy.types.PointLamp.quadratic_attenuation`, `bpy.types.SpotLamp.quadratic_attenuation`.
'''

GPU_DYNAMIC_LAMP_DISTANCE: float = None
''' See `bpy.types.Lamp.distance`.
'''

GPU_DYNAMIC_LAMP_DYNCO: typing.Any = None
''' Represents the position of the light in camera space. Computed as: mat4_world_to_cam_ * vec3_lamp_pos
'''

GPU_DYNAMIC_LAMP_DYNCOL: typing.Any = None
''' See `bpy.types.Lamp.color`.
'''

GPU_DYNAMIC_LAMP_DYNENERGY: float = None
''' See `bpy.types.Lamp.energy`.
'''

GPU_DYNAMIC_LAMP_DYNIMAT: typing.Any = None
''' Matrix that converts vector in camera space to lamp space. Computed as: mat4_world_to_lamp_ * mat4_cam_to_world_
'''

GPU_DYNAMIC_LAMP_DYNPERSMAT: typing.Any = None
''' Matrix that converts a vector in camera space to shadow buffer depth space. Computed as: mat4_perspective_to_depth_ * mat4_lamp_to_perspective_ * mat4_world_to_lamp_ * mat4_cam_to_world_. ``mat4_perspective_to_depth`` is a fixed matrix defined as follow:: 0.5 0.0 0.0 0.5 0.0 0.5 0.0 0.5 0.0 0.0 0.5 0.5 0.0 0.0 0.0 1.0
'''

GPU_DYNAMIC_LAMP_DYNVEC: typing.Any = None
''' Represents the direction of light in camera space. Computed as: mat4_world_to_cam_ * (-vec3_lamp_Z_axis)
'''

GPU_DYNAMIC_LAMP_SPOTBLEND: float = None
''' See `bpy.types.SpotLamp.spot_blend`.
'''

GPU_DYNAMIC_LAMP_SPOTSCALE: typing.Any = None
''' Represents the SpotLamp local scale.
'''

GPU_DYNAMIC_LAMP_SPOTSIZE: float = None
''' See `bpy.types.SpotLamp.spot_size`.
'''

GPU_DYNAMIC_MAT_ALPHA: float = None
''' See `bpy.types.Material.alpha`.
'''

GPU_DYNAMIC_MAT_AMB: float = None
''' See `bpy.types.Material.ambient`.
'''

GPU_DYNAMIC_MAT_DIFFRGB: typing.Any = None
''' See `bpy.types.Material.diffuse_color`.
'''

GPU_DYNAMIC_MAT_EMIT: float = None
''' See `bpy.types.Material.emit`.
'''

GPU_DYNAMIC_MAT_HARD: float = None
''' See `bpy.types.Material.specular_hardness`.
'''

GPU_DYNAMIC_MAT_REF: float = None
''' See `bpy.types.Material.diffuse_intensity`.
'''

GPU_DYNAMIC_MAT_SPEC: float = None
''' See `bpy.types.Material.specular_intensity`.
'''

GPU_DYNAMIC_MAT_SPECRGB: typing.Any = None
''' See `bpy.types.Material.specular_color`.
'''

GPU_DYNAMIC_MIST_COLOR = None

GPU_DYNAMIC_MIST_DISTANCE: float = None
''' See `bpy.types.WorldMistSettings.intensity`.
'''

GPU_DYNAMIC_MIST_ENABLE: float = None
''' See `bpy.types.WorldMistSettings.use_mist`.
'''

GPU_DYNAMIC_MIST_INTENSITY: float = None

GPU_DYNAMIC_MIST_START: float = None
''' See `bpy.types.WorldMistSettings.start`. See `bpy.types.WorldMistSettings.depth`.
'''

GPU_DYNAMIC_MIST_TYPE: float = None
''' See `bpy.types.WorldMistSettings.falloff`.
'''

GPU_DYNAMIC_OBJECT_AUTOBUMPSCALE: float = None
''' Multiplier for bump-map scaling.
'''

GPU_DYNAMIC_OBJECT_COLOR: typing.Any = None
''' An RGB color + alpha defined at object level. Each values between 0.0 and 1.0. See `bpy.types.Object.color`.
'''

GPU_DYNAMIC_OBJECT_IMAT: typing.Any = None
''' The uniform is a 4x4 GL matrix that converts world coodinates to object coordinates (see mat4_world_to_object_).
'''

GPU_DYNAMIC_OBJECT_MAT: typing.Any = None
''' A matrix that converts object coordinates to world coordinates (see mat4_object_to_world_).
'''

GPU_DYNAMIC_OBJECT_VIEWIMAT: typing.Any = None
''' The uniform is a 4x4 GL matrix that converts coordinates in camera space to world coordinates (see mat4_cam_to_world_).
'''

GPU_DYNAMIC_OBJECT_VIEWMAT: typing.Any = None
''' A matrix that converts world coordinates to camera coordinates (see mat4_world_to_cam_).
'''

GPU_DYNAMIC_SAMPLER_2DBUFFER: typing.Any = None
''' Represents an internal texture used for certain effect (color band, etc).
'''

GPU_DYNAMIC_SAMPLER_2DIMAGE: typing.Any = None
''' Represents a texture loaded from an image file.
'''

GPU_DYNAMIC_SAMPLER_2DSHADOW: typing.Any = None
''' Represents a texture loaded from a shadow buffer file.
'''
