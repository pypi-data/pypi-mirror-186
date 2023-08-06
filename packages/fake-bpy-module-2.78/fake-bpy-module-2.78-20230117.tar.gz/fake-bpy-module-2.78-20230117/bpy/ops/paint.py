import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def add_simple_uvs(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: typing.Optional[bool] = None):
    ''' Add cube map uvs on mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def add_texture_paint_slot(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'DIFFUSE_COLOR',
        name: typing.Union[str, typing.Any] = "Untitled",
        width: typing.Optional[typing.Any] = 1024,
        height: typing.Optional[typing.Any] = 1024,
        color: typing.Optional[typing.Any] = (0.0, 0.0, 0.0, 1.0),
        alpha: typing.Union[bool, typing.Any] = True,
        generated_type: typing.Optional[typing.Any] = 'BLANK',
        float: typing.Union[bool, typing.Any] = False):
    ''' Add a texture paint slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Merge method to use
    :type type: typing.Optional[typing.Any]
    :param name: Name, Image datablock name
    :type name: typing.Union[str, typing.Any]
    :param width: Width, Image width
    :type width: typing.Optional[typing.Any]
    :param height: Height, Image height
    :type height: typing.Optional[typing.Any]
    :param color: Color, Default fill color
    :type color: typing.Optional[typing.Any]
    :param alpha: Alpha, Create an image with an alpha channel
    :type alpha: typing.Union[bool, typing.Any]
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing * ``BLANK`` Blank, Generate a blank image. * ``UV_GRID`` UV Grid, Generated grid to test UV mappings. * ``COLOR_GRID`` Color Grid, Generated improved UV grid to test UV mappings.
    :type generated_type: typing.Optional[typing.Any]
    :param float: 32 bit Float, Create image with 32 bit floating point bit depth
    :type float: typing.Union[bool, typing.Any]
    '''

    pass


def brush_colors_flip(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Toggle foreground and background brush colors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def brush_select(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 paint_mode: typing.Optional[typing.Any] = 'ACTIVE',
                 sculpt_tool: typing.Optional[typing.Any] = 'BLOB',
                 vertex_paint_tool: typing.Optional[typing.Any] = 'MIX',
                 weight_paint_tool: typing.Optional[typing.Any] = 'MIX',
                 texture_paint_tool: typing.Optional[typing.Any] = 'DRAW',
                 toggle: typing.Union[bool, typing.Any] = False,
                 create_missing: typing.Union[bool, typing.Any] = False):
    ''' Select a paint mode's brush by tool type

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param paint_mode: Paint Mode * ``ACTIVE`` Current, Set brush for active paint mode. * ``SCULPT`` Sculpt. * ``VERTEX_PAINT`` Vertex Paint. * ``WEIGHT_PAINT`` Weight Paint. * ``TEXTURE_PAINT`` Texture Paint.
    :type paint_mode: typing.Optional[typing.Any]
    :param sculpt_tool: Sculpt Tool
    :type sculpt_tool: typing.Optional[typing.Any]
    :param vertex_paint_tool: Vertex Paint Tool * ``MIX`` Mix, Use mix blending mode while painting. * ``ADD`` Add, Use add blending mode while painting. * ``SUB`` Subtract, Use subtract blending mode while painting. * ``MUL`` Multiply, Use multiply blending mode while painting. * ``BLUR`` Blur, Blur the color with surrounding values. * ``LIGHTEN`` Lighten, Use lighten blending mode while painting. * ``DARKEN`` Darken, Use darken blending mode while painting.
    :type vertex_paint_tool: typing.Optional[typing.Any]
    :param weight_paint_tool: Weight Paint Tool * ``MIX`` Mix, Use mix blending mode while painting. * ``ADD`` Add, Use add blending mode while painting. * ``SUB`` Subtract, Use subtract blending mode while painting. * ``MUL`` Multiply, Use multiply blending mode while painting. * ``BLUR`` Blur, Blur the color with surrounding values. * ``LIGHTEN`` Lighten, Use lighten blending mode while painting. * ``DARKEN`` Darken, Use darken blending mode while painting.
    :type weight_paint_tool: typing.Optional[typing.Any]
    :param texture_paint_tool: Texture Paint Tool
    :type texture_paint_tool: typing.Optional[typing.Any]
    :param toggle: Toggle, Toggle between two brushes rather than cycling
    :type toggle: typing.Union[bool, typing.Any]
    :param create_missing: Create Missing, If the requested brush type does not exist, create a new brush
    :type create_missing: typing.Union[bool, typing.Any]
    '''

    pass


def delete_texture_paint_slot(override_context: typing.
                              Union[typing.Dict, 'bpy.types.Context'] = None,
                              execution_context: typing.Union[str, int] = None,
                              undo: typing.Optional[bool] = None):
    ''' Delete selected texture paint slot

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def face_select_all(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection for all faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle, Toggle selection for all elements. * ``SELECT`` Select, Select all elements. * ``DESELECT`` Deselect, Deselect all elements. * ``INVERT`` Invert, Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def face_select_hide(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     unselected: typing.Union[bool, typing.Any] = False):
    ''' Hide selected faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: typing.Union[bool, typing.Any]
    '''

    pass


def face_select_linked(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None):
    ''' Select linked faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def face_select_linked_pick(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None,
                            *,
                            deselect: typing.Union[bool, typing.Any] = False):
    ''' Select linked faces under the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: typing.Union[bool, typing.Any]
    '''

    pass


def face_select_reveal(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       unselected: typing.Union[bool, typing.Any] = False):
    ''' Reveal hidden faces

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: typing.Union[bool, typing.Any]
    '''

    pass


def grab_clone(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               delta: typing.Optional[typing.Any] = (0.0, 0.0)):
    ''' Move the clone source image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param delta: Delta, Delta offset of clone image in 0.0..1.0 coordinates
    :type delta: typing.Optional[typing.Any]
    '''

    pass


def hide_show(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              action: typing.Optional[typing.Any] = 'HIDE',
              area: typing.Optional[typing.Any] = 'INSIDE',
              xmin: typing.Optional[typing.Any] = 0,
              xmax: typing.Optional[typing.Any] = 0,
              ymin: typing.Optional[typing.Any] = 0,
              ymax: typing.Optional[typing.Any] = 0):
    ''' Hide/show some vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action, Whether to hide or show vertices * ``HIDE`` Hide, Hide vertices. * ``SHOW`` Show, Show vertices.
    :type action: typing.Optional[typing.Any]
    :param area: Area, Which vertices to hide or show * ``OUTSIDE`` Outside, Hide or show vertices outside the selection. * ``INSIDE`` Inside, Hide or show vertices inside the selection. * ``ALL`` All, Hide or show all vertices. * ``MASKED`` Masked, Hide or show vertices that are masked (minimum mask value of 0.5).
    :type area: typing.Optional[typing.Any]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    '''

    pass


def image_from_view(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    filepath: typing.Union[str, typing.Any] = ""):
    ''' Make an image from the current 3D view for re-projection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Name of the file
    :type filepath: typing.Union[str, typing.Any]
    '''

    pass


def image_paint(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                stroke: typing.Optional[bpy.types.bpy_prop_collection[
                    'bpy.types.OperatorStrokeElement']] = None,
                mode: typing.Optional[typing.Any] = 'NORMAL'):
    ''' Paint a stroke into the image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param mode: Stroke Mode, Action taken when a paint stroke is made * ``NORMAL`` Normal, Apply brush normally. * ``INVERT`` Invert, Invert action of brush for duration of stroke. * ``SMOOTH`` Smooth, Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def mask_flood_fill(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    mode: typing.Optional[typing.Any] = 'VALUE',
                    value: typing.Optional[typing.Any] = 0.0):
    ''' Fill the whole mask with a given value, or invert its values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``VALUE`` Value, Set mask to the level specified by the 'value' property. * ``VALUE_INVERSE`` Value Inverted, Set mask to the level specified by the inverted 'value' property. * ``INVERT`` Invert, Invert the mask.
    :type mode: typing.Optional[typing.Any]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: typing.Optional[typing.Any]
    '''

    pass


def mask_lasso_gesture(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       path: typing.Optional[bpy.types.bpy_prop_collection[
                           'bpy.types.OperatorMousePath']] = None,
                       mode: typing.Optional[typing.Any] = 'VALUE',
                       value: typing.Optional[typing.Any] = 1.0):
    ''' Add mask within the lasso as you move the brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param path: path
    :type path: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']]
    :param mode: Mode * ``VALUE`` Value, Set mask to the level specified by the 'value' property. * ``VALUE_INVERSE`` Value Inverted, Set mask to the level specified by the inverted 'value' property. * ``INVERT`` Invert, Invert the mask.
    :type mode: typing.Optional[typing.Any]
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
    :type value: typing.Optional[typing.Any]
    '''

    pass


def project_image(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  image: typing.Union[str, int, typing.Any] = ''):
    ''' Project an edited render from the active camera back onto the object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param image: Image
    :type image: typing.Union[str, int, typing.Any]
    '''

    pass


def sample_color(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 location: typing.Optional[typing.Any] = (0, 0),
                 merged: typing.Union[bool, typing.Any] = False,
                 palette: typing.Union[bool, typing.Any] = False):
    ''' Use the mouse to sample a color in the image

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param location: Location
    :type location: typing.Optional[typing.Any]
    :param merged: Sample Merged, Sample the output display color
    :type merged: typing.Union[bool, typing.Any]
    :param palette: Add to Palette
    :type palette: typing.Union[bool, typing.Any]
    '''

    pass


def texture_paint_toggle(override_context: typing.
                         Union[typing.Dict, 'bpy.types.Context'] = None,
                         execution_context: typing.Union[str, int] = None,
                         undo: typing.Optional[bool] = None):
    ''' Toggle texture paint mode in 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vert_select_all(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection for all vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle, Toggle selection for all elements. * ``SELECT`` Select, Select all elements. * ``DESELECT`` Deselect, Deselect all elements. * ``INVERT`` Invert, Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def vert_select_ungrouped(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: typing.Optional[bool] = None,
                          *,
                          extend: typing.Union[bool, typing.Any] = False):
    ''' Select vertices without a group

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param extend: Extend, Extend the selection
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass


def vertex_color_brightness_contrast(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        brightness: typing.Optional[typing.Any] = 0.0,
        contrast: typing.Optional[typing.Any] = 0.0):
    ''' Adjust vertex color brightness/contrast

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param brightness: Brightness
    :type brightness: typing.Optional[typing.Any]
    :param contrast: Contrast
    :type contrast: typing.Optional[typing.Any]
    '''

    pass


def vertex_color_dirt(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      blur_strength: typing.Optional[typing.Any] = 1.0,
                      blur_iterations: typing.Optional[typing.Any] = 1,
                      clean_angle: typing.Optional[typing.Any] = 3.14159,
                      dirt_angle: typing.Optional[typing.Any] = 0.0,
                      dirt_only: typing.Union[bool, typing.Any] = False):
    ''' Undocumented

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param blur_strength: Blur Strength, Blur strength per iteration
    :type blur_strength: typing.Optional[typing.Any]
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
    :type blur_iterations: typing.Optional[typing.Any]
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
    :type clean_angle: typing.Optional[typing.Any]
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
    :type dirt_angle: typing.Optional[typing.Any]
    :param dirt_only: Dirt Only, Don't calculate cleans for convex areas
    :type dirt_only: typing.Union[bool, typing.Any]
    '''

    pass


def vertex_color_hsv(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     h: typing.Optional[typing.Any] = 0.5,
                     s: typing.Optional[typing.Any] = 1.0,
                     v: typing.Optional[typing.Any] = 1.0):
    ''' Adjust vertex color HSV values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param h: Hue
    :type h: typing.Optional[typing.Any]
    :param s: Saturation
    :type s: typing.Optional[typing.Any]
    :param v: Value
    :type v: typing.Optional[typing.Any]
    '''

    pass


def vertex_color_invert(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Invert RGB values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_color_levels(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        offset: typing.Optional[typing.Any] = 0.0,
                        gain: typing.Optional[typing.Any] = 1.0):
    ''' Adjust levels of vertex colors

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param offset: Offset, Value to add to colors
    :type offset: typing.Optional[typing.Any]
    :param gain: Gain, Value to multiply colors by
    :type gain: typing.Optional[typing.Any]
    '''

    pass


def vertex_color_set(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Fill the active vertex color layer with the current paint color

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_color_smooth(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Smooth colors across vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def vertex_paint(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 stroke: typing.Optional[bpy.types.bpy_prop_collection[
                     'bpy.types.OperatorStrokeElement']] = None,
                 mode: typing.Optional[typing.Any] = 'NORMAL'):
    ''' Paint a stroke in the active vertex color layer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param mode: Stroke Mode, Action taken when a paint stroke is made * ``NORMAL`` Normal, Apply brush normally. * ``INVERT`` Invert, Invert action of brush for duration of stroke. * ``SMOOTH`` Smooth, Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def vertex_paint_toggle(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Toggle the vertex paint mode in 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def weight_from_bones(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      type: typing.Optional[typing.Any] = 'AUTOMATIC'):
    ''' Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type, Method to use for assigning weights * ``AUTOMATIC`` Automatic, Automatic weights from bones. * ``ENVELOPES`` From Envelopes, Weights from envelopes with user defined radius.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def weight_gradient(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None,
                    *,
                    type: typing.Optional[typing.Any] = 'LINEAR',
                    xstart: typing.Optional[typing.Any] = 0,
                    xend: typing.Optional[typing.Any] = 0,
                    ystart: typing.Optional[typing.Any] = 0,
                    yend: typing.Optional[typing.Any] = 0,
                    cursor: typing.Optional[typing.Any] = 1002):
    ''' Draw a line to apply a weight gradient to selected vertices

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    :param xstart: X Start
    :type xstart: typing.Optional[typing.Any]
    :param xend: X End
    :type xend: typing.Optional[typing.Any]
    :param ystart: Y Start
    :type ystart: typing.Optional[typing.Any]
    :param yend: Y End
    :type yend: typing.Optional[typing.Any]
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: typing.Optional[typing.Any]
    '''

    pass


def weight_paint(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 stroke: typing.Optional[bpy.types.bpy_prop_collection[
                     'bpy.types.OperatorStrokeElement']] = None,
                 mode: typing.Optional[typing.Any] = 'NORMAL'):
    ''' Paint a stroke in the current vertex group's weights

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param mode: Stroke Mode, Action taken when a paint stroke is made * ``NORMAL`` Normal, Apply brush normally. * ``INVERT`` Invert, Invert action of brush for duration of stroke. * ``SMOOTH`` Smooth, Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def weight_paint_toggle(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Toggle weight paint mode in 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def weight_sample(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Use the mouse to sample a weight in the 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def weight_sample_group(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        group: typing.Union[str, int, typing.Any] = 'DEFAULT'):
    ''' Select one of the vertex groups available under current mouse position

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param group: Keying Set, The Keying Set to use
    :type group: typing.Union[str, int, typing.Any]
    '''

    pass


def weight_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Fill the active vertex group with the current paint weight

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
