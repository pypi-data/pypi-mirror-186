"""
    PyJAMAS is Just A More Awesome Siesta
    Copyright (C) 2018  Rodrigo Fernandez-Gonzalez (rodrigo.fernandez.gonzalez@utoronto.ca)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# tests for image module
# for coverage, run:
# coverage run -m pytest
# coverage report -i

import numpy
import pytest
import skimage
import skimage.filters as skif

from pyjamas.pjscore import PyJAMAS
from pyjamas.rimage.rimutils import rimutils
from pyjamas.rutils import RUtils
from pyjamas.rcallbacks.rcbimage import projection_types
import pyjamas.tests.unit.pjsfixtures as pjsfixtures

PyJAMAS_FIXTURE: PyJAMAS = PyJAMAS()
PyJAMAS_FIXTURE.options.cbSetCWD(pjsfixtures.TMP_DIR)


@pytest.mark.usefixtures("contrastlimits_fixture")
def test_cbAdjustContrast(contrastlimits_fixture):
    PyJAMAS_FIXTURE.image.cbAdjustContrast(contrastlimits_fixture[0], contrastlimits_fixture[1])

    theqimage = PyJAMAS_FIXTURE._imageItem.pixmap().toImage()
    displayed_image = numpy.empty((PyJAMAS_FIXTURE.height, PyJAMAS_FIXTURE.width), dtype=numpy.uint8)

    for row_index in range(PyJAMAS_FIXTURE.height):
        for col_index in range(PyJAMAS_FIXTURE.width):
            displayed_image[row_index, col_index] = theqimage.pixel(col_index, row_index)

    assert numpy.array_equal(displayed_image,
                             numpy.array(
                                 rimutils.stretch(PyJAMAS_FIXTURE.imagedata,
                                                  contrastlimits_fixture[0],
                                                  contrastlimits_fixture[1]),
                                 dtype=numpy.uint8))


def test_cbPlay():
    assert PyJAMAS_FIXTURE.image.cbPlay()


@pytest.mark.usefixtures("rotatecwpath_fixture")
def test_cbRotateImage(rotatecwpath_fixture):
    original_image = PyJAMAS_FIXTURE.slices.copy()

    PyJAMAS_FIXTURE.image.cbRotateImage(PyJAMAS_FIXTURE.image.CW)
    assert numpy.array_equal(PyJAMAS_FIXTURE.slices, skimage.io.imread(rotatecwpath_fixture))

    PyJAMAS_FIXTURE.image.cbRotateImage(PyJAMAS_FIXTURE.image.CCW)
    assert numpy.array_equal(PyJAMAS_FIXTURE.slices, original_image)


@pytest.mark.usefixtures("fliplrpath_fixture", "flipudpath_fixture")
def test_cbFlipImage(fliplrpath_fixture, flipudpath_fixture):
    original_image = PyJAMAS_FIXTURE.slices.copy()

    PyJAMAS_FIXTURE.image.cbFlipImage(PyJAMAS_FIXTURE.image.LEFT_RIGHT)
    assert numpy.array_equal(PyJAMAS_FIXTURE.slices, skimage.io.imread(fliplrpath_fixture))

    PyJAMAS_FIXTURE.image.cbFlipImage(PyJAMAS_FIXTURE.image.LEFT_RIGHT)
    assert numpy.array_equal(PyJAMAS_FIXTURE.slices, original_image)

    PyJAMAS_FIXTURE.image.cbFlipImage(PyJAMAS_FIXTURE.image.UP_DOWN)
    assert numpy.array_equal(PyJAMAS_FIXTURE.slices, skimage.io.imread(flipudpath_fixture))

    PyJAMAS_FIXTURE.image.cbFlipImage(PyJAMAS_FIXTURE.image.UP_DOWN)
    assert numpy.array_equal(PyJAMAS_FIXTURE.slices, original_image)


@pytest.mark.usefixtures("invertpath_fixture")
def test_cbInvertImage(invertpath_fixture):
    PyJAMAS_FIXTURE.image.cbInvertImage()
    theimage = PyJAMAS_FIXTURE.slices.copy()
    PyJAMAS_FIXTURE.options.cbUndo()

    assert numpy.array_equal(theimage, skimage.io.imread(invertpath_fixture))


@pytest.mark.usefixtures("gradientpath_fixture")
def test_cbGradientImage(gradientpath_fixture):
    PyJAMAS_FIXTURE.image.cbGradientImage()
    theimage = PyJAMAS_FIXTURE.slices.copy()
    PyJAMAS_FIXTURE.options.cbUndo()

    assert numpy.array_equal(theimage, skimage.io.imread(gradientpath_fixture))


@pytest.mark.usefixtures("gaussiansigma_fixture")
def test_cbGaussianImage(gaussiansigma_fixture):
    PyJAMAS_FIXTURE.image.cbGaussianImage(gaussiansigma_fixture)
    theimage = PyJAMAS_FIXTURE.slices.copy()
    PyJAMAS_FIXTURE.options.cbUndo()

    assert numpy.array_equal(theimage, numpy.asarray(
        [skif.gaussian(a_slice, sigma=gaussiansigma_fixture, preserve_range=True) for a_slice in
         PyJAMAS_FIXTURE.slices],
        dtype=numpy.uint16))


@pytest.mark.usefixtures("projectionpath_fixture")
def test_cbProjectImage(projectionpath_fixture):
    for aprojectionpath, aprojectiontype in zip(projectionpath_fixture, projection_types):
        PyJAMAS_FIXTURE.image.cbProjectImage([], aprojectiontype)
        theproj = PyJAMAS_FIXTURE.slices.copy()
        PyJAMAS_FIXTURE.options.cbUndo()

        assert numpy.array_equal(theproj, skimage.io.imread(aprojectionpath))


def test_cbCropImage():
    theimage = PyJAMAS_FIXTURE.slices.copy()

    # crop around the entire image.
    PyJAMAS_FIXTURE.image.cbCrop(numpy.asarray(
        [[0, 0], [PyJAMAS_FIXTURE.width, 0], [PyJAMAS_FIXTURE.width, PyJAMAS_FIXTURE.height],
         [0, PyJAMAS_FIXTURE.height], [0, 0]]))

    assert numpy.array_equal(theimage, PyJAMAS_FIXTURE.slices)


@pytest.mark.usefixtures("logoannotationspath_fixture")
@pytest.mark.usefixtures("kymographpath_fixture")
def test_cbKymograph(logoannotationspath_fixture, kymographpath_fixture):
    PyJAMAS_FIXTURE.io.cbLoadAnnotations([logoannotationspath_fixture])

    PyJAMAS_FIXTURE.image.cbKymograph(RUtils.qpolygonf2ndarray(PyJAMAS_FIXTURE.polylines[0][0]))
    theimage = PyJAMAS_FIXTURE.slices.copy()

    PyJAMAS_FIXTURE.options.cbUndo()

    assert numpy.array_equal(theimage, skimage.io.imread(kymographpath_fixture))


PyJAMAS_FIXTURE.app.quit()
