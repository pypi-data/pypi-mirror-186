import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def convert_to_particle_system(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a new or update an existing hair particle system on the surface object

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def sculptmode_toggle(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Enter/Exit sculpt mode for curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def snap_curves_to_surface(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        attach_mode: typing.Optional[typing.Any] = 'NEAREST'):
    ''' Move curves so that the first point is exactly on the surface mesh

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param attach_mode: Attach Mode, How to find the point on the surface to attach to * ``NEAREST`` Nearest -- Find the closest point on the surface for the root point of every curve and move the root there. * ``DEFORM`` Deform -- Re-attach curves to a deformed surface using the existing attachment information. This only works when the topology of the surface mesh has not changed.
    :type attach_mode: typing.Optional[typing.Any]
    '''

    pass
