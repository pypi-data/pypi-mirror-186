import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def action_sanitize(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: typing.Optional[bool] = None):
    ''' Make action suitable for use as a Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def apply_pose(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               pose_index: typing.Optional[typing.Any] = -1):
    ''' Apply specified Pose Library pose to the rig

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: typing.Optional[typing.Any]
    '''

    pass


def apply_pose_asset(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     blend_factor: typing.Optional[typing.Any] = 1.0,
                     flipped: typing.Union[bool, typing.Any] = False):
    ''' Apply the given Pose Action to the rig

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses
    :type blend_factor: typing.Optional[typing.Any]
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: typing.Union[bool, typing.Any]
    '''

    pass


def apply_pose_asset_for_keymap(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Apply the given Pose Action to the rig :file: `addons/pose_library/operators.py\:447 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$447>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def blend_pose_asset(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     blend_factor: typing.Optional[typing.Any] = 0.0,
                     flipped: typing.Union[bool, typing.Any] = False,
                     release_confirm: typing.Union[bool, typing.Any] = False):
    ''' Blend the given Pose Action to the rig

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param blend_factor: Blend Factor, Amount that the pose is applied on top of the existing poses
    :type blend_factor: typing.Optional[typing.Any]
    :param flipped: Apply Flipped, When enabled, applies the pose flipped over the X-axis
    :type flipped: typing.Union[bool, typing.Any]
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
    :type release_confirm: typing.Union[bool, typing.Any]
    '''

    pass


def blend_pose_asset_for_keymap(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Blend the given Pose Action to the rig :file: `addons/pose_library/operators.py\:419 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$419>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def browse_interactive(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: typing.Optional[bool] = None,
                       *,
                       pose_index: typing.Optional[typing.Any] = -1):
    ''' Interactively browse poses in 3D-View

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param pose_index: Pose, Index of the pose to apply (-2 for no change to pose, -1 for poselib active pose)
    :type pose_index: typing.Optional[typing.Any]
    '''

    pass


def convert_old_poselib(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None):
    ''' Create a pose asset for each pose marker in the current action :file: `addons/pose_library/operators.py\:469 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$469>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def copy_as_asset(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None):
    ''' Create a new pose asset on the clipboard, to be pasted into an Asset Browser :file: `addons/pose_library/operators.py\:226 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$226>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def create_pose_asset(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        pose_name: typing.Union[str, typing.Any] = "",
        activate_new_action: typing.Union[bool, typing.Any] = True):
    ''' Create a new Action that contains the pose of the selected bones, and mark it as Asset. The asset will be stored in the current blend file

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param pose_name: Pose Name
    :type pose_name: typing.Union[str, typing.Any]
    :param activate_new_action: Activate New Action
    :type activate_new_action: typing.Union[bool, typing.Any]
    '''

    pass


def new(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Add New Pose Library to active Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def paste_asset(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Paste the Asset that was previously copied using Copy As Asset :file: `addons/pose_library/operators.py\:301 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$301>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def pose_add(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             frame: typing.Optional[typing.Any] = 1,
             name: typing.Union[str, typing.Any] = "Pose"):
    ''' Add the current Pose to the active Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param frame: Frame, Frame to store pose on
    :type frame: typing.Optional[typing.Any]
    :param name: Pose Name, Name of newly added Pose
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def pose_asset_select_bones(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None,
                            *,
                            select: typing.Union[bool, typing.Any] = True,
                            flipped: typing.Union[bool, typing.Any] = False):
    ''' Select those bones that are used in this pose

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Union[bool, typing.Any]
    :param flipped: Flipped
    :type flipped: typing.Union[bool, typing.Any]
    '''

    pass


def pose_move(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              pose: typing.Union[str, int, typing.Any] = '',
              direction: typing.Optional[typing.Any] = 'UP'):
    ''' Move the pose up or down in the active Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param pose: Pose, The pose to move
    :type pose: typing.Union[str, int, typing.Any]
    :param direction: Direction, Direction to move the chosen pose towards
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def pose_remove(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                pose: typing.Union[str, int, typing.Any] = ''):
    ''' Remove nth pose from the active Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param pose: Pose, The pose to remove
    :type pose: typing.Union[str, int, typing.Any]
    '''

    pass


def pose_rename(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                name: typing.Union[str, typing.Any] = "RenamedPose",
                pose: typing.Union[str, int, typing.Any] = ''):
    ''' Rename specified pose from the active Pose Library

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: New Pose Name, New name for pose
    :type name: typing.Union[str, typing.Any]
    :param pose: Pose, The pose to rename
    :type pose: typing.Union[str, int, typing.Any]
    '''

    pass


def restore_previous_action(override_context: typing.
                            Union[typing.Dict, 'bpy.types.Context'] = None,
                            execution_context: typing.Union[str, int] = None,
                            undo: typing.Optional[bool] = None):
    ''' Switch back to the previous Action, after creating a pose asset :file: `addons/pose_library/operators.py\:179 <https://developer.blender.org/diffusion/BA/addons/pose_library/operators.py$179>`_

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def unlink(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None):
    ''' Remove Pose Library from active Object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass
