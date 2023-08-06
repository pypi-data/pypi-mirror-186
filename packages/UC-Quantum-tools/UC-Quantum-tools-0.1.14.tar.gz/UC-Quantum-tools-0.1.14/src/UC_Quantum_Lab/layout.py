from . import _states, _circs, _hists, _layout_file, _master_show
from .elements import Image
import os, json, platform

_layout = {}
_to_flip = {}
_custom = False

# turns path into absolute path if it isn't
def _abs_path(path): return os.path.abspath(path.replace("~", os.path.expanduser("~")))

# converts list of image files to html img elements
def _image_list_to_str(image_list:list[str])->str:
    to_return = ""
    for item in image_list:
        p = _abs_path(item)
        if platform.system() == "Windows":
            p = p[p.index(":")+1:].replace("\\", "/")
        to_return+=Image(p)#f"<img src=\"{{URI}}{p}\" alt=\"no image to display\">"
        #to_return+=f"<div class=\"image-container\">\n<div class=\"image detail-view\" style=\"background-image:url({{URI}}{p});\"></div>\n</div>\n"
    return to_return

def _inverter(layout, flip:dict[str,str]):
    for item in list(layout):
        if item in flip:
            other = layout[item]
            layout[item] = layout[flip[item]]
            layout[flip[item]] = other

    
    for item in list(layout):
        if not isinstance(layout[item], str):
            layout[item] = _inverter(layout[item], flip)

    return layout

def invert() -> None:
    global _to_flip
    _to_flip = {"left" : "right", "top" : "bottom"}

def horizontal_invert() -> None:
    global _to_flip
    _to_flip = {"left" : "right"}


def vertical_invert() -> None:
    global _to_flip
    _to_flip = {"top" : "bottom"}


# default layout of the viewer
def default() -> None:
    global _layout, _states, _circs, _hists
    # if the statevector and an image is to be rendered
    if len(_states) and (len(_hists) or len(_circs)):
        #state_path = _abs_path(os.path.join(_config_dir,  "_state_.html"))
        msg = "\\[\\begin{matrix} "
        length = len(_states)
        for i, item in enumerate(list(_states)):
            if i == 0:
                msg += ("\\text{bits}")
                for j in range(len(_states[item])):
                    msg += f" & \\text{{call {j+1}}}"
                msg += "\\\\"
            if i < length - 1:
                msg+=(f"{item} & " + "&".join(_states[item]) + "\\\\")
            else:
                msg+=(f"{item} & " + "&".join(_states[item]))
        msg+="\\end{matrix}\\]"
        _layout["left"] = msg #f"<div data-include=\"{{URI}}{state_path}\"></div>"

        if len(_hists) and len(_circs):
            _layout["right"] = {"top" : _image_list_to_str(_circs), "bottom" : _image_list_to_str(_hists)}
        elif len(_hists):
            _layout["right"] = _image_list_to_str(_hists)
        elif len(_circs):
            _layout["right"] = _image_list_to_str(_circs)
    
    elif len(_states):
        #state_path = _abs_path(os.path.join(_config_dir,  "_state_.html"))
        msg = "\\[\\begin{matrix} "
        length = len(_states)
        for i, item in enumerate(list(_states)):
            if i == 0:
                msg += ("\\text{bits}")
                for j in range(len(_states[item])):
                    msg += f" & \\text{{call {j+1}}}"
                msg += "\\\\"
            if i < length - 1:
                msg+=(f"{item} & " + "&".join(_states[item]) + "\\\\")
            else:
                msg+=(f"{item} & " + "&".join(_states[item]))
        msg+="\\end{matrix}\\]"
        _layout["only"] = msg #f"<div data-include=\"{{URI}}{state_path}\"></div>"

    elif len(_hists) or len(_circs):
        if len(_hists) and len(_circs):
            _layout["top"] = _image_list_to_str(_circs)
            _layout["bottom"] = _image_list_to_str(_hists)
        elif len(_hists):
            _layout["only"] = _image_list_to_str(_hists)
        elif len(_circs):
            _layout["only"] = _image_list_to_str(_circs)
    
    else:
        _layout["only"] = "<h1>No data to display</h1>"

def custom(layout_json) -> None:
    global _layout, _custom
    _layout = layout_json
    _custom = True

def _run():
    global _layout, _to_flip, _states, _circs, _hists, _master_show, _custom
    if _master_show:
        if not _custom:
            # running the default layout generator
            default()
        if len(_to_flip):
            _layout = _inverter(_layout, _to_flip)

        #print("unloading layout")
        with open(_layout_file, 'w') as f:
            f.write(json.dumps(_layout, indent=2))
        
        # clearing the values
        _to_flip = {}
        _layout = {}
        _states = []
        _circs = [] 
        _hists = []
    
def _layout_at_exit():
    from . import _master_show
    if _master_show:
        _run()