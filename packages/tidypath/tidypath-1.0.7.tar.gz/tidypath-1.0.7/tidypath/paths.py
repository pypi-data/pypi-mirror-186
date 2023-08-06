"""
Creates paths for automatically organizing files. 
Allows filename modification: If arg added (deleted) to func => add (delete) arg to stored function output files.

Two schemes:
    1. By module => Module -> submodules -> class tree (until classes in module by default) -> func
    2. By class  => Class organization is a class to be inherited. Sets path: parentDir -> subfolder (optionally specified) -> inheritance_tree -> func_name.
(1) is the most appropiate.
"""
import os
import sys
import inspect
import warnings
import numpy as np
from copy import deepcopy
from collections.abc import Iterable
from pathlib import Path
from .fmt import dict_to_id, encoder
from .inspection import get_class_that_defined_method

dataDir = "data"
figDir = "figs"

def module_path(func=None, depth=3, include_classes="file", skip=1):
    """
    returns module path and func_name.
    
    include_classes:   'file': path: module -> class tree contained in func file -> func_name.
                       'all': path: module -> full class tree -> func_name.
    """
    if func is None:
        frame = sys._getframe(depth)
        func_name = frame.f_code.co_name
        module = frame.f_globals["__name__"]
    else:
        func_name = func.__name__
        module = func.__module__
    if include_classes:
        func_class = get_class_that_defined_method(func)
        if func_class is not None:
            if include_classes == "file":
                clsmembers = inspect.getmembers(sys.modules[module], inspect.isclass)
                cls_names, clss = zip(*clsmembers)
                class_tree = "/".join([c.__name__.lower() for c in func_class.mro()[:-skip][::-1] if c in clss])
            elif include_classes == "all":
                "/".join([c.__name__.lower() for c in func.__class__.mro()[:-skip][::-1]])
            else:
                raise ValueError(f"include_classes: {include_classes} not valid. Available: 'file', 'all', ''.")
        else:
            class_tree = ""
    else:
        class_tree = ""
    path = os.path.join(*module.split(".")[1:], class_tree, func_name)
    return path

def saving_path(Dir, ext, keys={}, subfolder="", return_dir=False, funcname_in_filename=False, **kwargs):
    """Tree path: subfolder -> module -> (classes) -> func_name."""
    parentDir = os.path.join(Dir, subfolder, module_path(**kwargs))
    Path(parentDir).mkdir(exist_ok=True, parents=True)   
    if return_dir:
        return parentDir
    else:
        if funcname_in_filename:
            filename = parentDir.split("/")[-1] + f"_{dict_to_id(keys)}_.{ext}"
        else:
            filename = f"{dict_to_id(keys)}_.{ext}"
        return os.path.join(parentDir, filename)
    
def figpath(ext="png", **kwargs):
    return saving_path(figDir, ext, **kwargs)

def datapath(ext="lzma", **kwargs):
    return saving_path(dataDir, ext, **kwargs)

def filename_modifier(process_filename, func=None, directory=None, check_first=True, overwrite=False, **args):
    """
    Base function for adding/deleting/modifying function args encoded in the output filenames.
    
    Attrs:
        - process_filename:    function f(file, k_name, k, v) -> new_filename. 
                               - k, v are the key and value of an arg.
                               - k_name is the string encoding of k. (replace '_' -> '-')
        - func (callable):     function (wrapped by savedata or savefig) for retrieving the corresponding directory where the outputs are stored.
        - directory (str):     directory where files are to be modified. It is recommended to pass the function instead of the directory.
        - check_first (bool):  whether to check the new filenames before applying any changes.   
        - overwrite (bool):    whether to overwrite files when in conflict.
                               Examples:   add/modify/delete an arg -> two filenames are the same -> one remains.
        - args (kwargs):       Arguments to add/delete/modify in the filename.
    """
    if func is not None:
        if directory is not None:
            raise RuntimeError("Please provide 'func' or 'directory' but not both.")
        else:
            if func.__out__ == "data":
                directory = datapath(func=func, return_dir=True)
            else:
                directory = figpath(func=func, return_dir=True)
    elif directory is None:
        raise RuntimeError("Provide 'func' (preferred) or 'directory'.")
        
    args_sorted = {k: args[k] for k in sorted(args)}
    abort_changes = False
    avoid_files = [".ipynb_checkpoints", "__pycache__"]
    for k, v in args_sorted.items():
        check_first_k = deepcopy(check_first)
        if abort_changes:
            break
        else:
            k_name = encoder(k).replace("_", "-")
            for file in os.listdir(directory):
                if file not in avoid_files:
                    new_filename = process_filename(file, k_name, k, v)
                    if new_filename is not None:
                        new_path = os.path.join(directory, new_filename)
                        if Path(new_path).exists() and not overwrite:
                            raise RuntimeError(f"'{new_filename}' already existing before modifying '{file}'. To delete repeated files pass 'overwrite=True'.")
                        else:
                            if check_first_k:
                                update_file = 0
                                while update_file not in ["y", "yes", "n", "no"]:
                                    update_file = input("Filename change example:\n\n'{}' -> '{}'\n\nProceed? [y/n]".format(file, new_filename)).lower()
                                check_first_k = False
                            if update_file in ["y", "yes"]:                    
                                os.rename(os.path.join(directory, file), 
                                          os.path.join(directory, new_filename))
                            else:
                                warnings.warn("Aborted filename changes.", RuntimeWarning)
                                abort_changes = True
                                break
    return

def add_arg(func=None, directory=None, check_first=True, overwrite=False, **args):
    """
    Encodes new function args into filename.
    Useful when:
        (1) Adding a new arg to a function wrapped by savedata. Allows loading the available data without recomputing.
        (2) Modifying figure names produced by a function.
    
    Attrs:
        - args (kwargs):       new arguments to encode into filename.
        - func (callable):     function (wrapped by savedata or savefig) for retrieving the corresponding directory where the outputs are stored.
        - directory (str):     directory where files are to be modified. It is recommended to pass the function instead of the directory.
        - check_first (bool):  whether to check the new filenames before applying any changes.
        - overwrite (bool):    whether to overwrite files when in conflict.
                               Example:   add an arg -> two filenames are the same -> one remains.
    """
    def process_filename(file, k_name, k, v):
        arg_val = dict_to_id({k:v})
        if arg_val not in file:
            args_in_file = np.sort(os.path.splitext(file)[0].split("_")[:-1] + [k])
            pos_new_arg = np.where(args_in_file == k)[0][0]
            if pos_new_arg == 0:
                new_filename = f"{arg_val}_{file}"
            else:
                if pos_new_arg + 1 == len(args_in_file):
                    insert_before = "."
                else:
                    insert_before = args_in_file[pos_new_arg + 1]
                new_filename = file.replace(f"_{insert_before}", f"_{arg_val}_{insert_before}")
            return new_filename
        else:
            return None
    filename_modifier(process_filename, func=func, directory=directory, check_first=check_first, overwrite=overwrite, **args)
    return 

def delete_arg(func=None, arg=None, directory=None, check_first=True, overwrite=False):
    """
    Delete encoded function arg from filename.
    Useful when:
        (1) Deleting an arg from a function wrapped by savedata. Allows loading the available data without recomputing.
        (2) Modifying figure names produced by a function.
    
    Attrs:
        - arg (str or iterable):       key of an arg (k in k=v) to be deleted, or an iterable containing keys.
        - func (callable):             function (wrapped by savedata or savefig) for retrieving the corresponding directory where the outputs are stored.
        - directory (str):             directory where files are to be modified. It is recommended to pass the function instead of the directory.
        - check_first (bool):          whether to check the new filenames before applying any changes.
        - overwrite (bool):            whether to overwrite files when in conflict.
                                       Examples:   Delete an arg -> two filenames are the same -> one remains.
    """
    if isinstance(arg, str):
        arg_dict = {arg: None}
    elif isinstance(arg, Iterable):
        if all(isinstance(a, str) for a in arg):
            arg_dict = {a: None for a in arg}
        else:
            raise ValueError(f"arg {arg} not valid. Must be a string or an iterable of strings.")
    else:
        raise ValueError(f"arg {arg} not valid. Must be a string or an iterable of strings.")
        
    def process_filename(file, k_name, k, v):
        if file.startswith(f"{k_name}-"):
            return "_".join(file.split("_")[1:])
        else:
            mid_file_k_name = f"_{k_name}-"
            if mid_file_k_name in file:
                arg_val_encoded = "{}{}".format(mid_file_k_name, file.split(mid_file_k_name)[1].split("_")[0])
                return file.replace(arg_val_encoded, "")
            else:
                return None
    filename_modifier(process_filename, func=func, directory=directory, check_first=check_first, overwrite=overwrite, **arg_dict)
    return 

def modify_arg(func=None, directory=None, check_first=True, overwrite=False, **args):
    """
    Modified encoded function arg from filename.
    Useful when:
        (1) Renaming an arg value with a more suitable one (more comprehensible, better defined...), leaving the func output unchanged. Allows loading the available data without recomputing.
        (2) Modifying figure names produced by a function.
    
    Attrs:
        - args (kwargs):       arguments to modify in the filename.
        - func (callable):     function (wrapped by savedata or savefig) for retrieving the corresponding directory where the outputs are stored.
        - directory (str):     directory where files are to be modified. It is recommended to pass the function instead of the directory.
        - check_first (bool):  whether to check the new filenames before applying any changes.
        - overwrite (bool):    whether to overwrite files when in conflict.
                               Examples:   Modify an arg -> two filenames are the same -> one remains.
    """
    def process_filename(file, k_name, k, v):
        if file.startswith(f"{k_name}-"):
            return "_".join([dict_to_id({k:v})] + file.split("_")[1:])
        else:
            mid_file_k_name = f"_{k_name}-"
            if mid_file_k_name in file:
                arg_val_encoded = "{}{}".format(mid_file_k_name, file.split(mid_file_k_name)[1].split("_")[0])
                return file.replace(arg_val_encoded, "_{}".format(dict_to_id({k:v})))
            else:
                return None

    filename_modifier(process_filename, func=func, directory=directory, check_first=check_first, overwrite=overwrite, **args)
    return 

class Organizer():
    dataDir = dataDir
    figDir = figDir
    subfolder = ""
    
class ClassPath(Organizer):
    """
    Updates fig and data dir of the class as follows:
    parentDir -> subfolder -> inheritance_tree -> func_name
    """
    
    @classmethod
    def inheritance_path(cls, skip=2):
        return "/".join([c.__name__.lower() for c in cls.mro()[:-skip][::-1]])
    
    @classmethod
    def create_dir(cls, dirKey, depth=2):
        """Creates tree: parentDir -> subfolder -> inheritance_tree -> func_name"""
        path = os.path.join(getattr(cls, f"{dirKey}Dir"),
                            cls.subfolder,
                            cls.inheritance_path(),
                            sys._getframe(depth).f_code.co_name
                           )
        Path(path).mkdir(exist_ok=True, parents=True)
        return path
        
    @classmethod
    def create_figDir(cls):
        return cls.create_dir("fig")
    
    @classmethod
    def create_dataDir(cls):
        return cls.create_dir("data")
    