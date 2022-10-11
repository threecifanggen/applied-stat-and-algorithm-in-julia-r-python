import pytest
import numpy as np
from pytools.exp_design import (
    num_of_quality_subjects,
    num_of_quantity_subjects
)

def test_num_of_quality_subjects():
    assert np.floor(num_of_quality_subjects(0.02, 0.25, 0.05)) == 1800

def test_num_of_quantity_subjects():
    assert num_of_quantity_subjects(0.5, 4, 0.05) == pytest.approx(246, 1)