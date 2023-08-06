import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def brush_stroke(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        stroke: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorStrokeElement']] = None,
        mode: typing.Optional[typing.Any] = 'NORMAL',
        ignore_background_click: typing.Union[bool, typing.Any] = False):
    ''' Sculpt a stroke into the geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param stroke: Stroke
    :type stroke: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorStrokeElement']]
    :param mode: Stroke Mode, Action taken when a paint stroke is made * ``NORMAL`` Regular, Apply brush normally. * ``INVERT`` Invert, Invert action of brush for duration of stroke. * ``SMOOTH`` Smooth, Switch brush to smooth mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    :param ignore_background_click: Ignore Background Click, Clicks on the background do not start the stroke
    :type ignore_background_click: typing.Union[bool, typing.Any]
    '''

    pass


def detail_flood_fill(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Flood fill the mesh with the selected detail setting

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def dirty_mask(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               dirty_only: typing.Union[bool, typing.Any] = False):
    ''' Generates a mask based on the geometry cavity and pointiness

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param dirty_only: Dirty Only, Don't calculate cleans for convex areas
    :type dirty_only: typing.Union[bool, typing.Any]
    '''

    pass


def dynamic_topology_toggle(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None):
    ''' Dynamic topology alters the mesh topology while sculpting

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def mask_expand(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                invert: typing.Union[bool, typing.Any] = True,
                use_cursor: typing.Union[bool, typing.Any] = True,
                update_pivot: typing.Union[bool, typing.Any] = True,
                smooth_iterations: typing.Optional[typing.Any] = 2,
                mask_speed: typing.Optional[typing.Any] = 5,
                use_normals: typing.Union[bool, typing.Any] = True,
                keep_previous_mask: typing.Union[bool, typing.Any] = False,
                edge_sensitivity: typing.Optional[typing.Any] = 300):
    ''' Expands a mask from the initial active vertex under the cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param invert: Invert, Invert the new mask
    :type invert: typing.Union[bool, typing.Any]
    :param use_cursor: Use Cursor, Expand the mask to the cursor position
    :type use_cursor: typing.Union[bool, typing.Any]
    :param update_pivot: Update Pivot Position, Set the pivot position to the mask border after creating the mask
    :type update_pivot: typing.Union[bool, typing.Any]
    :param smooth_iterations: Smooth iterations
    :type smooth_iterations: typing.Optional[typing.Any]
    :param mask_speed: Mask speed
    :type mask_speed: typing.Optional[typing.Any]
    :param use_normals: Use Normals, Generate the mask using the normals and curvature of the model
    :type use_normals: typing.Union[bool, typing.Any]
    :param keep_previous_mask: Keep Previous Mask, Generate the new mask on top of the current one
    :type keep_previous_mask: typing.Union[bool, typing.Any]
    :param edge_sensitivity: Edge Detection Sensitivity, Sensitivity for expanding the mask across sculpted sharp edges when using normals to generate the mask
    :type edge_sensitivity: typing.Optional[typing.Any]
    '''

    pass


def mask_filter(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                filter_type: typing.Optional[typing.Any] = 'SMOOTH',
                iterations: typing.Optional[typing.Any] = 1,
                auto_iteration_count: typing.Union[bool, typing.Any] = False):
    ''' Applies a filter to modify the current mask

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param filter_type: Type, Filter that is going to be applied to the mask * ``SMOOTH`` Smooth Mask, Smooth mask. * ``SHARPEN`` Sharpen Mask, Sharpen mask. * ``GROW`` Grow Mask, Grow mask. * ``SHRINK`` Shrink Mask, Shrink mask. * ``CONTRAST_INCREASE`` Increase contrast, Increase the contrast of the paint mask. * ``CONTRAST_DECREASE`` Decrease contrast, Decrease the contrast of the paint mask.
    :type filter_type: typing.Optional[typing.Any]
    :param iterations: Iterations, Number of times that the filter is going to be applied
    :type iterations: typing.Optional[typing.Any]
    :param auto_iteration_count: Auto Iteration Count, Use a automatic number of iterations based on the number of vertices of the sculpt
    :type auto_iteration_count: typing.Union[bool, typing.Any]
    '''

    pass


def mesh_filter(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                type: typing.Optional[typing.Any] = 'INFLATE',
                strength: typing.Optional[typing.Any] = 1.0,
                deform_axis: typing.Optional[typing.Any] = {'X', 'Y', 'Z'}):
    ''' Applies a filter to modify the current mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param type: Filter type, Operation that is going to be applied to the mesh * ``SMOOTH`` Smooth, Smooth mesh. * ``SCALE`` Scale, Scale mesh. * ``INFLATE`` Inflate, Inflate mesh. * ``SPHERE`` Sphere, Morph into sphere. * ``RANDOM`` Random, Randomize vertex positions. * ``RELAX`` Relax, Relax mesh.
    :type type: typing.Optional[typing.Any]
    :param strength: Strength, Filter Strength
    :type strength: typing.Optional[typing.Any]
    :param deform_axis: Deform axis, Apply the deformation in the selected axis * ``X`` X, Deform in the X axis. * ``Y`` Y, Deform in the Y axis. * ``Z`` Z, Deform in the Z axis.
    :type deform_axis: typing.Optional[typing.Any]
    '''

    pass


def optimize(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None):
    ''' Recalculate the sculpt BVH to improve performance

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def sample_detail_size(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       location: typing.Optional[typing.Any] = (0, 0),
                       mode: typing.Optional[typing.Any] = 'DYNTOPO'):
    ''' Sample the mesh detail on clicked point

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param location: Location, Screen Coordinates of sampling
    :type location: typing.Optional[typing.Any]
    :param mode: Detail Mode, Target sculpting workflow that is going to use the sampled size * ``DYNTOPO`` Dyntopo, Sample dyntopo detail. * ``VOXEL`` Voxel, Sample mesh voxel size.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def sculptmode_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Toggle sculpt mode in 3D view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_detail_size(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Set the mesh detail (either relative or constant one, depending on current dyntopo mode)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_persistent_base(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Reset the copy of the mesh that is being sculpted on

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def set_pivot_position(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       mode: typing.Optional[typing.Any] = 'UNMASKED'):
    ''' Sets the sculpt transform pivot position

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode * ``ORIGIN`` Origin, Sets the pivot to the origin of the sculpt. * ``UNMASKED`` Unmasked, Sets the pivot position to the average position of the unmasked vertices. * ``BORDER`` Mask border, Sets the pivot position to the center of the border of the mask. * ``ACTIVE`` Active vertex, Sets the pivot position to the active vertex position. * ``SURFACE`` Surface, Sets the pivot position to the surface under the cursor.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def symmetrize(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None):
    ''' Symmetrize the topology modifications

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def uv_sculpt_stroke(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     mode: typing.Optional[typing.Any] = 'NORMAL'):
    ''' Sculpt UVs using a brush

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Stroke Mode * ``NORMAL`` Regular, Apply brush normally. * ``INVERT`` Invert, Invert action of brush for duration of stroke. * ``RELAX`` Relax, Switch brush to relax mode for duration of stroke.
    :type mode: typing.Optional[typing.Any]
    '''

    pass
