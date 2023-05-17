import pytest

from napari_matplotlib import SliceWidget


@pytest.mark.mpl_image_compare
def test_slice(make_napari_viewer, brain_data):
    viewer = make_napari_viewer()
    viewer.add_image(brain_data[0], **brain_data[1])
    fig = SliceWidget(viewer).figure
    return fig
