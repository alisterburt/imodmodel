from struct import Struct
import binascii

from typing import Union
import numpy as np

from .specification import id_spec, header_spec


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
    pass



class ModelFileParser:
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None
        self.buffer = None
        self.parse_file()

    def parse_file(self):
        self.open_file()
        self.parse_id()
        self.parse_header()
        self.parse_object()
        self.close_file()

    def open_file(self):
        self.file = open(self.filename, 'rb')

    def parse_id(self):
        self.id = self.parse_from_specification(self._id_spec)

    def parse_header(self):
        self.header = self.parse_from_specification(self._header_spec)

    def parse_object(self):

    def format_from_specification(self, specification: dict):
        return f">{''.join(specification.values())}"

    def parse_from_specification(self, specification):
        format = self.format_from_specification(specification)
        struct = Struct(format)
        self.read_into_buffer(struct.size)
        return self.unpack_buffer(struct, specification)

    def read_into_buffer(self, n: int):
        self.buffer = self.file.read(n)

    def unpack_buffer(self, struct: Struct, specification: dict):
        return {key: value for key, value in zip(specification.keys(), struct.unpack(self.buffer))}

    def close_file(self):
        self.file.close()

    @property
    def _id_spec(self):
         return id_spec

    @property
    def _header_spec(self):
        return header_spec






