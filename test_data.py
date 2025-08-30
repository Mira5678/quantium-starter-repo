#run with 'pytest'

import pytest
from data_visualization import app
from data_visualization import update_visualization

#Test if header exists
def test_header_exists():
    layout = app.layout
    layout_str = str(layout) #convert to string

    #Test whether header exists or not
    assert "header" in layout_str, "Header is not found"
    #Test whether the title "Pink Morsel Sales Visualizer" of the graph exists or not by checking ID
    assert "Pink Morsel Sales Visualizer" in layout_str, "Title of the graph is not found"


#Test if visualization exists
def test_visualization():
    layout = app.layout
    layout_str = str(layout)

    assert "line_graph" in layout_str, "Line graph is not found"

#Test if region picker exists
def test_region_picker():
    layout = app.layout
    layout_str = str(layout)

    assert "region_choice" in layout_str, "Region picker is not found"




    













