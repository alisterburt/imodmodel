import numpy as np
import pandas as pd

from imodmodel import ModelParser, read

two_contours = 'two_contour_example.mod'


def test_parser():
    parser = ModelParser(two_contours)


def test_read():
    model = read(two_contours)
    assert len(model.objects) == 1
    assert len(model.objects[0].contours) == 2


def test_as_contour_dict():
    data = read(two_contours).as_contour_dict()
    assert isinstance(data, dict)
    assert len(data) == 2


def test_as_contour_array():
    data = read(two_contours).as_contour_array()
    assert isinstance(data, np.ndarray)
    assert data.shape == (25, 4)


def test_as_dataframe():
    df = read(two_contours).as_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (25, 4)
