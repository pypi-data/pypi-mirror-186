import os.path
from typing import Tuple

import cv2
import numpy
import pytest
import skimage

FIXTURE_DIR: str = '/Users/rodrigo/src/pyjamas_dev/pyjamas/tests/unit/fixtures/'
IMAGE_FIXTURE: str = 'image.tif'
CLASSIFIER_FIXTURE: Tuple[str, str] = ('classifier_lr.cfr', 'classifier_svm.cfr')
DISPLAY_FIXTURE: str = 'display.tif'
BINMASKS_FIXTURE: str = 'binmasks.tif'
MOVIE_FIXTURE: str = 'movie.avi'
PJSANNOTATIONS_FIXTURE: str = 'annotations.pjs'
LOGOANNOTATIONS_FIXTURE: str = 'logoannotations.pjs'
MATANNOTATIONS_FIXTURE: str = 'annotations.mat'
SINGLE_CELL_PJSANNOTATIONS_FIXTURE: str = 'cell_00001.pjs'
XMLROIS_FIXTURE: str = 'rois.xml'
PROJECTION_FIXTURE: Tuple[str, str] = ('max_projection.tif', 'sum_projection.tif')
ROTATED_CW_FIXTURE: str = 'rotated_cw.tif'
FLIPPED_LR_FIXTURE: str = 'flipped_lr.tif'
FLIPPED_UD_FIXTURE: str = 'flipped_ud.tif'
INVERTED_FIXTURE: str = 'inverted.tif'
GRADIENT_FIXTURE: str = 'gradient.tif'
KYMOGRAPH_FIXTURE: str = 'kymograph.tif'
TMP_IMG_FILE: str = 'image.tif'
TMP_DIR: str = '/Users/rodrigo/src/pyjamas_dev/pyjamas/tests/tmp/'
TMP_DISP_FILE: str = 'display.tif'
TMP_BINMASKS_FILE: str = 'binmasks.tif'
TMP_MOVIE_FILE: str = 'movie.avi'
TMP_PJS_FILE: str = 'annotations.pjs'
TMP_MAT_FILE: str = 'annotations.mat'
TMP_SINGLE_CELL_PJS_FILE: str = 'cell_00001.pjs'
TMP_XML_FILE: str = 'rois.xml'
PIX_PERCENTILE_LIMITS: Tuple[int, int] = (10, 90)
GAUSSIAN_SIGMA: float = 3.0


@pytest.fixture
def image_fixture():
    return skimage.io.imread(os.path.join(FIXTURE_DIR, IMAGE_FIXTURE))


@pytest.fixture
def display_fixture():
    return skimage.io.imread(os.path.join(FIXTURE_DIR, DISPLAY_FIXTURE))


@pytest.fixture
def binmasks_fixture():
    return skimage.io.imread(os.path.join(FIXTURE_DIR, BINMASKS_FIXTURE))


@pytest.fixture
def pjsannotationspath_fixture():
    return os.path.join(FIXTURE_DIR, PJSANNOTATIONS_FIXTURE)


@pytest.fixture
def logoannotationspath_fixture():
    return os.path.join(FIXTURE_DIR, LOGOANNOTATIONS_FIXTURE)


@pytest.fixture
def singlecellpjsannotationspath_fixture():
    return os.path.join(FIXTURE_DIR, SINGLE_CELL_PJSANNOTATIONS_FIXTURE)


@pytest.fixture
def matannotationspath_fixture():
    return os.path.join(FIXTURE_DIR, MATANNOTATIONS_FIXTURE)


@pytest.fixture
def imagepath_fixture():
    return os.path.join(FIXTURE_DIR, IMAGE_FIXTURE)


@pytest.fixture
def classifierpath_fixture():
    return (os.path.join(FIXTURE_DIR, classifier_fixture_filename) for classifier_fixture_filename in
            CLASSIFIER_FIXTURE)


@pytest.fixture
def xmlroispath_fixture():
    return os.path.join(FIXTURE_DIR, XMLROIS_FIXTURE)


@pytest.fixture
def movie_fixture():
    movie = cv2.VideoCapture(os.path.join(FIXTURE_DIR, MOVIE_FIXTURE))

    success, movie_array = movie.read()
    success, theslice = movie.read()

    while success:
        movie_array = numpy.concatenate((movie_array, theslice), axis=0)
        success, theslice = movie.read()

    return movie_array


@pytest.fixture
def rotatecwpath_fixture():
    return os.path.join(FIXTURE_DIR, ROTATED_CW_FIXTURE)


@pytest.fixture
def fliplrpath_fixture():
    return os.path.join(FIXTURE_DIR, FLIPPED_LR_FIXTURE)


@pytest.fixture
def flipudpath_fixture():
    return os.path.join(FIXTURE_DIR, FLIPPED_UD_FIXTURE)


@pytest.fixture
def invertpath_fixture():
    return os.path.join(FIXTURE_DIR, INVERTED_FIXTURE)


@pytest.fixture
def gradientpath_fixture():
    return os.path.join(FIXTURE_DIR, GRADIENT_FIXTURE)


@pytest.fixture
def projectionpath_fixture():
    return (os.path.join(FIXTURE_DIR, projection_fixture_filename) for projection_fixture_filename in
            PROJECTION_FIXTURE)


@pytest.fixture
def contrastlimits_fixture():
    return PIX_PERCENTILE_LIMITS


@pytest.fixture
def gaussiansigma_fixture():
    return GAUSSIAN_SIGMA


@pytest.fixture
def kymographpath_fixture():
    return os.path.join(FIXTURE_DIR, KYMOGRAPH_FIXTURE)
