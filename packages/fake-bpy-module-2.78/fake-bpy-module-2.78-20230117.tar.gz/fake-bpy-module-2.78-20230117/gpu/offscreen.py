import sys
import typing

GenericType = typing.TypeVar("GenericType")


class GPUOffscreen:
    ''' This object gives access to off screen buffers. bind(save=True) Bind the offscreen object. :param save: save OpenGL current states. :type save: bool draw_view3d(scene, view3d, region, modelview_matrix, projection_matrix) Draw the 3d viewport in the offscreen object. :param scene: Scene to draw. :type scene: `bpy.types.Scene` :param view3d: 3D View to get the drawing settings from. :type view3d: `bpy.types.SpaceView3D` :param region: Region of the 3D View. :type region: `bpy.types.Region` :param modelview_matrix: ModelView Matrix. :type modelview_matrix: `mathutils.Matrix` :param projection_matrix: Projection Matrix. :type projection_matrix: `mathutils.Matrix` free() Free the offscreen object The framebuffer, texture and render objects will no longer be accessible. unbind(restore=True) Unbind the offscreen object. :param restore: restore OpenGL previous states. :type restore: bool
    '''

    color_texture: int = None
    ''' Color texture.

    :type: int
    '''

    height: int = None
    ''' Texture height.

    :type: int
    '''

    width: int = None
    ''' Texture width.

    :type: int
    '''


def new(width: int, height: int, samples: int = 0) -> typing.Any:
    ''' Return a GPUOffScreen.

    :param width: Horizontal dimension of the buffer.
    :type width: int
    :param height: Vertical dimension of the buffer.
    :type height: int
    :param samples: OpenGL samples to use for MSAA or zero to disable.
    :type samples: int
    :rtype: typing.Any
    :return: Newly created off-screen buffer.
    '''

    pass
