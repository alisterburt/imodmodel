from .parser import ModelParser


def read(filename: str, as_array=False, as_dataframe=False):
    """
    read an IMOD model file

    Parameters
    ----------
    filename : str
               filename to read
    header_only : bool
                  read only the file header
    as_array : bool
               read file as an (n, 4) contour array with columns (x, y, z, contour_idx)
    as_dataframe : bool
                   read file as an (n, 4) pandas dataframe with columns (x, y, z, contour_idx)

    Returns
    -------

    """
    parser = ModelParser(filename)
    model = parser.model
    if as_array:
        model = model.as_contour_array()
    elif as_dataframe:
        model = model.as_dataframe()
    return model

