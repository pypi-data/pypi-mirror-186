"""
Import all possible stuff that can be used.
"""


# start delvewheel patch
def _delvewheel_init_patch_1_2_0():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, '.'))
    is_pyinstaller = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if not is_pyinstaller or os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-pillow_heif-0.9.2')
        if not is_pyinstaller or os.path.isfile(load_order_filepath):
            with open(os.path.join(libs_dir, '.load-order-pillow_heif-0.9.2')) as file:
                load_order = file.read().split()
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                if not is_pyinstaller or os.path.isfile(lib_path):
                    ctypes.WinDLL(lib_path)


_delvewheel_init_patch_1_2_0()
del _delvewheel_init_patch_1_2_0
# end delvewheel patch




from . import options
from ._lib_info import libheif_info, libheif_version
from ._version import __version__
from .as_plugin import (
    AvifImageFile,
    HeifImageFile,
    register_avif_opener,
    register_heif_opener,
)
from .constants import HeifErrorCode
from .error import HeifError
from .heif import (
    HeifFile,
    HeifImage,
    HeifThumbnail,
    from_bytes,
    from_pillow,
    is_supported,
    open_heif,
    read_heif,
)
from .misc import get_file_mimetype, set_orientation
from .thumbnails import add_thumbnails, thumbnail