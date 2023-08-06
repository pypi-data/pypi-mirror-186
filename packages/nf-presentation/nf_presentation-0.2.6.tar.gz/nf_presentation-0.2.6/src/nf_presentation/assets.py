import importlib.resources as pkg_resources
from io import BytesIO

from cairosvg import svg2png

from .settings import RFS_LOGO_FILE_NAME

def get_rfs_logo():
    return pkg_resources.open_binary(__package__, RFS_LOGO_FILE_NAME)

def get_test_data(short=True) -> dict:
    resource_path= 'test_data_short.json' if short else 'test_data.json'
    return pkg_resources.open_text(__package__, resource_path,encoding='utf8')

def get_exercise_test_data() -> dict:
    return pkg_resources.open_text(__package__, 'exercise_test_data_new.json',encoding='utf8')

def get_asset_stream(filename):
    """returns a file-object of resource with given filename"""
    return pkg_resources.open_binary(__package__, filename)

def convert_to_png(filename,width=300,height=300):
    """converts svg to a png and returnds as a stream"""
    stream=BytesIO()
    with get_asset_stream(filename) as f:
        svg2png(file_obj=f,output_width=width,output_height=height,write_to=stream)
    return stream


