# -*- coding: utf-8 -*-

from ed_design import Colors
import matplotlib
import pytest

# %%
@pytest.fixture
def colors():
    return Colors()

def test_class(colors):
    assert isinstance(colors, object)

def test_get_palette(colors):
    palette = colors.get_palette('blues')
    assert len(palette) == 4
    assert palette[1] == '#006EB7'
    
def test_get_cmap(colors):
    camp = colors.get_cmap('BlGr')
    assert isinstance(camp, matplotlib.colors.LinearSegmentedColormap)
    
def test_create_camp(colors):
    c1 = colors.colors['blues'][0]
    c2 = 'white'
    c3 = colors.colors['reds'][1]
    cmap = colors.create_cmap([c1, c2, c3], n_colors=100)
    assert isinstance(cmap, matplotlib.colors.LinearSegmentedColormap)
    
#TODO: implemente test of plotting
# def test_show_palette(colors):  # This will produce plots during pytest - we dont want that
#     assert colors.show_palette()
    
    
