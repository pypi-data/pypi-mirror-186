import sys
import typing

GenericType = typing.TypeVar("GenericType")


def load(filepath: str) -> typing.Any:
    ''' Load an image from a file.

    :param filepath: the filepath of the image.
    :type filepath: str
    :rtype: typing.Any
    :return: the newly loaded image.
    '''

    pass


def new(size: typing.Any) -> typing.Any:
    ''' Load a new image.

    :param size: The size of the image in pixels.
    :type size: typing.Any
    :rtype: typing.Any
    :return: the newly loaded image.
    '''

    pass


def write(image: typing.Any, filepath: str):
    ''' Write an image.

    :param image: the image to write.
    :type image: typing.Any
    :param filepath: the filepath of the image.
    :type filepath: str
    '''

    pass
