# -*- coding: utf-8 -*-

from ed_design import ed_logo
import numpy as np

# %%
def test_ed_logo_print():
    logo = ed_logo('print')
    assert isinstance(logo, np.ndarray)
    assert logo.sum() == 43028432
    
def test_ed_logo_web():
    logo = ed_logo('web')
    assert isinstance(logo, np.ndarray)
    assert logo.sum() == 6784625.0

def test_ed_logo_base():
    logo = ed_logo()
    assert isinstance(logo, np.ndarray)
    assert logo.sum() == 43028432
    
    