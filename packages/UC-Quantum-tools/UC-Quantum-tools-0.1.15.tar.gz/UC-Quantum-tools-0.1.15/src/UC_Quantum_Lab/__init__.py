from atexit import register as __register
import os

_config_dir = ".UCQ_config"
_layout_file = os.path.join(_config_dir, "layout.json")
_master_show = False
_show_plt = False
_states = {}
_circs = []
_hists = []
_round_to = 8 # digits past the decimal point to round numbers

__version__ = "0.1.15"

# cleans up the config directory on init of this python module
if _config_dir in os.listdir():
    _master_show = True
    #print("cleaning up config dir")
    for item in os.listdir(_config_dir):
        # deletes png html or the trigger file from the config dir
        if item.endswith(".png") or item.endswith(".html"):# or item == _trigger_file:
            os.remove(os.path.join(_config_dir, item))


from .layout import _layout_at_exit
from .commands import _show_at_exit

# need to be in this order
__register(_layout_at_exit)
__register(_show_at_exit)

from .commands import state, display, counts
from .layout import invert, horizontal_invert, vertical_invert, custom
from .utils import get_binary_strings
from .elements import Image