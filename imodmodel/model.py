from .specification import header_spec, object_spec, contour_spec, imat_spec


class ImodDataStructure:
    def _initialise_from_specification(self, specification):
        for key in specification.keys():
            self.__setattr__(key, None)

    def add_data_from_dict(self, data):
        for key, value in data.items():
            self.__setattr__(key, value)


class Model:
    def __init__(self):
        self.header = None
        self.objects = []

    def _add_object(self, object):
        self.objects.append(object)


class Object(ImodDataStructure):
    def __init__(self):
        self._initialise_from_specification(object_spec)
        self.contours = []
        self.meshes = []
        self.imat = None

    def add_data(self, data):
        if isinstance(data, Contour):
            self._add_contour(data)
        elif isinstance(data, Mesh):
            self._add_mesh(data)
        elif isinstance(data, Imat):
            self.imat = Imat

    def _add_contour(self, contour):
        self.contours.append(contour)

    def _add_mesh(self, mesh):
        self.meshes.append(mesh)


class Header(ImodDataStructure):
    def __init__(self):
        self._initialise_from_specification(header_spec)


class Contour(ImodDataStructure):
    def __init__(self):
        self._initialise_from_specification(contour_spec)


class Mesh(ImodDataStructure):
    pass


class Imat(ImodDataStructure):
    def __init__(self):
        self._initialise_from_specification(imat_spec)
