from napari_file_watcher.main_module import ScriptingWidget
import napari
import filecmp
import shutil
import os


def test_open(widget=None):
    if not widget:
        widget = ScriptingWidget(napari.Viewer(show=False))
    path = 'example_data/timelapse.py'
    widget.open(path=path)


def test_browse(widget=None):
    if not widget:
        widget = ScriptingWidget(napari.Viewer(show=False))
    try:
        os.mkdir('example_data/run')
    except FileExistsError:
        pass
    path = 'example_data/run'
    widget.browse(path=path)


def test_add():
    widget = ScriptingWidget(napari.Viewer(show=False))
    test_open(widget)
    test_browse(widget)
    widget.add()
    assert(filecmp.cmpfiles('example_data/', 'example_data/run/', ['timelapse.py', 'experiment.py']))
    try:
        shutil.rmtree('example_data/run')
    except FileNotFoundError:
        pass
