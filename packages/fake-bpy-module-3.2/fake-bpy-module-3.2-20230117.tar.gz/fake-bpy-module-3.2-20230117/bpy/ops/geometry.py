import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def attribute_add(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: typing.Optional[bool] = None,
                  *,
                  name: typing.Union[str, typing.Any] = "Attribute",
                  domain: typing.Optional[typing.Any] = 'POINT',
                  data_type: typing.Optional[typing.Any] = 'FLOAT'):
    ''' Add attribute to geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of new attribute
    :type name: typing.Union[str, typing.Any]
    :param domain: Domain, Type of element that attribute is stored on * ``POINT`` Point -- Attribute on point. * ``EDGE`` Edge -- Attribute on mesh edge. * ``FACE`` Face -- Attribute on mesh faces. * ``CORNER`` Face Corner -- Attribute on mesh face corner. * ``CURVE`` Spline -- Attribute on spline. * ``INSTANCE`` Instance -- Attribute on instance.
    :type domain: typing.Optional[typing.Any]
    :param data_type: Data Type, Type of data stored in attribute * ``FLOAT`` Float -- Floating-point value. * ``INT`` Integer -- 32-bit integer. * ``FLOAT_VECTOR`` Vector -- 3D vector with floating-point values. * ``FLOAT_COLOR`` Color -- RGBA color with 32-bit floating-point values. * ``BYTE_COLOR`` Byte Color -- RGBA color with 8-bit positive integer values. * ``STRING`` String -- Text string. * ``BOOLEAN`` Boolean -- True or false. * ``FLOAT2`` 2D Vector -- 2D vector with floating-point values. * ``INT8`` 8-Bit Integer -- Smaller integer with a range from -128 to 127.
    :type data_type: typing.Optional[typing.Any]
    '''

    pass


def attribute_convert(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None,
                      *,
                      mode: typing.Optional[typing.Any] = 'GENERIC',
                      domain: typing.Optional[typing.Any] = 'POINT',
                      data_type: typing.Optional[typing.Any] = 'FLOAT'):
    ''' Change how the attribute is stored

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param domain: Domain, Which geometry element to move the attribute to * ``POINT`` Point -- Attribute on point. * ``EDGE`` Edge -- Attribute on mesh edge. * ``FACE`` Face -- Attribute on mesh faces. * ``CORNER`` Face Corner -- Attribute on mesh face corner. * ``CURVE`` Spline -- Attribute on spline. * ``INSTANCE`` Instance -- Attribute on instance.
    :type domain: typing.Optional[typing.Any]
    :param data_type: Data Type * ``FLOAT`` Float -- Floating-point value. * ``INT`` Integer -- 32-bit integer. * ``FLOAT_VECTOR`` Vector -- 3D vector with floating-point values. * ``FLOAT_COLOR`` Color -- RGBA color with 32-bit floating-point values. * ``BYTE_COLOR`` Byte Color -- RGBA color with 8-bit positive integer values. * ``STRING`` String -- Text string. * ``BOOLEAN`` Boolean -- True or false. * ``FLOAT2`` 2D Vector -- 2D vector with floating-point values. * ``INT8`` 8-Bit Integer -- Smaller integer with a range from -128 to 127.
    :type data_type: typing.Optional[typing.Any]
    '''

    pass


def attribute_remove(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None):
    ''' Remove attribute from geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def color_attribute_add(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: typing.Optional[bool] = None,
                        *,
                        name: typing.Union[str, typing.Any] = "Color",
                        domain: typing.Optional[typing.Any] = 'POINT',
                        data_type: typing.Optional[typing.Any] = 'COLOR',
                        color: typing.Optional[typing.Any] = (0.0, 0.0, 0.0,
                                                              1.0)):
    ''' Add color attribute to geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of new color attribute
    :type name: typing.Union[str, typing.Any]
    :param domain: Domain, Type of element that attribute is stored on
    :type domain: typing.Optional[typing.Any]
    :param data_type: Data Type, Type of data stored in attribute
    :type data_type: typing.Optional[typing.Any]
    :param color: Color, Default fill color
    :type color: typing.Optional[typing.Any]
    '''

    pass


def color_attribute_remove(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: typing.Optional[bool] = None):
    ''' Remove color attribute from geometry

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def color_attribute_render_set(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        name: typing.Union[str, typing.Any] = "Color"):
    ''' Set default color attribute used for rendering

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, Name of color attribute
    :type name: typing.Union[str, typing.Any]
    '''

    pass
