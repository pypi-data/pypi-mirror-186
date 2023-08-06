import sys
import typing

GenericType = typing.TypeVar("GenericType")


def create_from_info(shader_info: typing.Any) -> typing.Any:
    ''' Create shader from a GPUShaderCreateInfo.

    :param shader_info: GPUShaderCreateInfo
    :type shader_info: typing.Any
    :rtype: typing.Any
    :return: Shader object corresponding to the given name.
    '''

    pass


def from_builtin(shader_name, config='DEFAULT'):
    ''' Shaders that are embedded in the blender internal code:

    '''

    pass


def unbind():
    ''' Unbind the bound shader object.

    '''

    pass
