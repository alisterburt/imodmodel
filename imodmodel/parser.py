from struct import Struct
import binascii

from typing import Union
import numpy as np

from .specification import header_spec

header_format = f">{''.join(header_spec.values())}"  # big endian
header_struct = Struct(header_format)


def read(filename: str, header_only=False):
    """
    read an IMOD model file

    Parameters
    ----------
    filename : str
               filename to read
    header_only : bool
                  read only the file header

    Returns
    -------

    """
    with open(filename, 'rb') as file:
        buffer = file.read(header_struct.size)
        header = {key: value for key, value in zip(header_spec.keys(),
                                                   header_struct.unpack(buffer))}
        4
