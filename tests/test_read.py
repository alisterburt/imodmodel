import numpy as np
import pandas as pd

import modfile

two_contours = 'two_contour_example.mod'


def test_read():
    model = modfile.read(two_contours)
    assert len(model.objects) == 1
    assert len(model.objects[0].contours) == 2


def test_read_as_contour_dict():
    data = modfile.read(two_contours).as_contour_dict()
    assert isinstance(data, dict)
    assert len(data) == 2


def test_as_contour_array():
    data = modfile.read(two_contours).as_contour_array()
    data2 = modfile.read(two_contours, as_array=True)
    np.testing.assert_array_equal(data, data2)
    assert isinstance(data, np.ndarray)
    assert data.shape == (25, 4)


def test_as_dataframe():
    df = modfile.read(two_contours).as_dataframe()
    data2 = modfile.read(two_contours, as_dataframe=True)
    assert all(df == data2)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (25, 4)
