"""
Main uses: save and cache data, save figures, change figure color, timing.
"""
import inspect
import warnings
from pathlib import Path
from functools import wraps
from collections.abc import Iterable
from importlib.util import find_spec
from ._helper import NoFigure
if find_spec("plotly") is None:
    plotly_figure = NoFigure
else:
    from plotly.graph_objs._figure import Figure as plotly_figure
if find_spec("matplotlib") is None:
    mpl_figure = NoFigure
else:
    from matplotlib.figure import Figure as mpl_figure
    import matplotlib.pyplot as plt

from . import storage, config
from .paths import datapath, figpath
from .inspection import classify_call_attrs, merge_wrapper_signatures
from ._helper import merge_nested_dict


def savedata(keys_or_function=None, include_classes="file",
             ext=config.EXT_DEFAULT_DATA, keys=config.KEYS_DEFAULT_DATA, funcname_in_filename=config.FUNCNAME_IN_FILENAME_DEFAULT_DATA,
             overwrite=False, save=True, load_opts_default_save=True,  #defaults for extra arguments
             load_opts={}, **save_opts):    
    """
    Decorator for automatically saving output and then loading cached data.
    Default behavior:
        1st function call:   stores the data with extension 'ext'.
        rest:                loads stored data if the key args passed to the function coincide.
        
    NOTE (!) decorated funcs will have extra arguments:
        - save (bool).                 whether to save the output of the function.
        - overwrite (bool).            whether to overwrite the saved version.
        - funcname_in_filename(bool)   whether to include funcname in the filename.
        - keys (dict/str/iterable)   · dict:     specifies filename of the form k1-v1_k2-v2_...kn_vn. 
                                                 k_i do not have to be arguments of the function.
                                     · str:       key of a keyword argument. Example: keys = 'x'.
                                                 "kwargs_defaults"  =>  default kwargs that were not modified.
                                                 "kwargs"           =>  kwargs passed during function call.
                                                 "kwargs_full"      =>  kws_defaults + kws.
                                                 "pos_only"         =>  length of *args
                                                 "args"             =>  attrs != **kwargs, *args.
                                                 "all"              if config.KEYS_ADD_POSONLY_TO_ALL  =>  all attrs
                                                                    else                               =>  all attrs except pos_only: kwargs_full + args
                                                 can combine options using "+" or "-". Example: "args+z", "x+y+kwargs", "all-y".
                                     · iterable: containing a combination of the available string keys (above). ["k1", "k2"] == "k1+k2".
                                                 
    Attrs:
        - function:                function to which the decorator is applied
        - ext:                     storing extension. Selects 'storage' functions save_ext, load_ext.
                                   Supported: 'lzma' (default), 'bz2', 'json', 'csv', 'npz'.
        - include_classes:         include class tree in saving_path.
        - load_opts:               kws for storage.load_ext. default kws are those of 'saving_options', those specified update saving_options dict.
        - save_opts:               kws for storage.save_ext
        - load_opts_default_save:  use save_opts as default for load_opts.
        - rest:                    default behavior for decorated funcs extra arguments (above).
        
    Returns: Function decorator
    """
    if isinstance(keys_or_function, Iterable):
        keys = keys_or_function
        func = None
    elif callable(keys_or_function):
        func = keys_or_function
    else:
        func = None
        
    if load_opts_default_save:
        load_opts = {**save_opts, **load_opts}
        
    def _savedata(func):  
        @wraps(func)
        def wrapper(*args, overwrite=overwrite, keys=keys, save=save, funcname_in_filename=funcname_in_filename, **kwargs):
            key_opts = classify_call_attrs(func, args, kwargs, add_pos_only_to_all=config.KEYS_ADD_POSONLY_TO_ALL)
            save_keys = merge_nested_dict(key_opts, keys, key_default="all")                    
            saving_path = datapath(keys=save_keys, func=func, ext=ext, include_classes=include_classes, funcname_in_filename=funcname_in_filename)
            
            if Path(saving_path).exists() and not overwrite:
                try:
                    result = getattr(storage, f"load_{ext}")(saving_path, **load_opts)
                except EOFError:
                    warnings.warn("Corrupted file. Recomputing and storing ...", RuntimeWarning)
                    result = func(*args, **kwargs)
                    getattr(storage, f"save_{ext}")(result, saving_path, **save_opts)
            else:
                result = func(*args, **kwargs)
                getattr(storage, f"save_{ext}")(result, saving_path, **save_opts)
            return result

        wrapper.__signature__ = merge_wrapper_signatures(wrapper, ["overwrite", "keys", "save", "funcname_in_filename"])
        wrapper.__out__ = "data"
        return wrapper
        
    if func is None:
        return _savedata
    else:
        return _savedata(func)
    

def savefig(keys_or_function=None, include_classes="file", 
            ext=config.EXT_DEFAULT_FIG, keys=config.KEYS_DEFAULT_FIG, funcname_in_filename=config.FUNCNAME_IN_FILENAME_DEFAULT_FIG, return_fig=config.RETURN_FIG_DEFAULT,
            overwrite=True, save=True,  #defaults for extra arguments
            **save_opts):    
    """
    Generates figsaver decorator.
    Figure returned by function is automatically saved. Compatible with matplotlib and plotly.
        
    NOTE (!) decorated funcs will have extra arguments:
        - return_fig (bool)            whether to return the figure (output of function).
        - save (bool).                 whether to save the figure.
        - overwrite (bool).            whether to overwrite the saved version.
        - funcname_in_filename(bool)   whether to include funcname in the filename.
        - keys (dict/str/iterable)   · dict:     specifies filename of the form k1-v1_k2-v2_...kn_vn. 
                                                 k_i do not have to be arguments of the function.
                                     · str:       key of a keyword argument. Example: keys = 'x'.
                                                 "kwargs_defaults"  =>  default kwargs that were not modified.
                                                 "kwargs"           =>  kwargs passed during function call.
                                                 "kwargs_full"      =>  kws_defaults + kws.
                                                 "pos_only"         =>  length of *args. Also self and cls are counted as pos_only arguments.
                                                 "args"             =>  attrs != **kwargs, *args.
                                                 "all"              if config.KEYS_ADD_POSONLY_TO_ALL  =>  all attrs
                                                                    else                               =>  all attrs except pos_only: kwargs_full + args
                                                 can combine options using "+" or "-". Example: "args+z", "x+y+kwargs", "all-y".
                                     · iterable: containing a combination of the available string keys (above). ["k1", "k2"] == "k1+k2".                                         
        
    Attrs:
        - function:                function to which the decorator is applied
        - ext:                     storing extension. 'eps' recommended for articles.
                                   Supported: any extension supported by matplotlib/plotly. Example: 'png', 'eps', 'html' (plotly), etc.
        - include_classes:         include class tree in saving_path.
        - save_opts:               kws for saving function.
        - rest:                    default behavior for decorated funcs extra arguments (above).
        
    Returns: Function decorator
    """
    if isinstance(keys_or_function, Iterable):
        keys = keys_or_function
        func = None
    elif callable(keys_or_function):
        func = keys_or_function
    else:
        func = None
        
    mpl_save_defaults = dict(bbox_inches="tight")
        
    def _savefig(func):  
        @wraps(func)
        def wrapper(*args, overwrite=overwrite, keys=keys, save=save, return_fig=return_fig, funcname_in_filename=funcname_in_filename, **kwargs):
            fig = func(*args, **kwargs)
            key_opts = classify_call_attrs(func, args, kwargs, add_pos_only_to_all=config.KEYS_ADD_POSONLY_TO_ALL)
            save_keys = merge_nested_dict(key_opts, keys, key_default="all")                    
            saving_path = figpath(keys=save_keys, func=func, ext=ext, include_classes=include_classes, funcname_in_filename=funcname_in_filename)
            
            if not Path(saving_path).exists() or overwrite:
                if isinstance(fig, mpl_figure):
                    fig.savefig(saving_path, format=ext, **{**mpl_save_defaults, **save_opts})
                    plt.close(fig)
                elif isinstance(fig, plotly_figure):
                    if ext == "html":
                        fig.write_html(saving_path, **save_opts)
                    else:
                        fig.write_image(saving_path, format=ext, **save_opts)
                else:
                    raise TypeError(f"fig type '{type(fig)}' not valid. Available: 'matplotlib.figure.Figure', 'plotly.grap_objs._figure.Figure'.")
                    
            if return_fig:
                return fig
            else:
                return
            
        wrapper.__signature__ = merge_wrapper_signatures(wrapper, ["overwrite", "keys", "save", "funcname_in_filename", "return_fig"])
        wrapper.__out__ = "figure"
        return wrapper
    
    if func is None:
        return _savefig
    else:
        return _savefig(func)