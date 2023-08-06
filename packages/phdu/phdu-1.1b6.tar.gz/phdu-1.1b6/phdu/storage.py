"""
Move/delete data
"""
import os
from pathlib import Path
import re

parent_dir =  'data'

def move_files(keyword, folder=None, parent_dir=parent_dir, verbose=1):
    """
    Moves all files in the parent directory starting with a keyword to a folder.
    
    Attributes:    
        - keyword: keyword to look for during file matching-
        - folder: Created folder to store all files matched by the keyword
        - parend_dir: Initial directory in which the files are contained.
    """
    folder = folder if folder is not None else keyword
    Path(os.path.join(parent_dir, folder)).mkdir(exist_ok=True, parents=True)
    processed = 0
    for path in os.listdir(parent_dir):
        if path == folder:
            continue
        else:
            if re.findall(key, path):
                os.rename(os.path.join(parent_dir, path), 
                          os.path.join(parent_dir, folder, path))
                processed += 1
    if verbose:
        print(f"Moved {processed} files from '{parent_dir}' to '{folder}' subdirectory.")        
    return

def delete_files_by_ext(parent_dir, extensions, verbose=1):
    """
    Removes files in parent_dir with extensions starting by (or being equal to) a certain character.
    """
    deleted = 0
    for path in os.listdir(parent_dir):
        for extension in extensions:
            if os.path.splitext(path)[1].startswith(extension):
                os.remove(os.path.join(parent_dir, path))
                deleted += 1
    if verbose:
        print(f"Deleted {deleted} files.")        
    return

def delete_stdin_files(parent_dir="nuredduna_programmes/stdin_files", verbose=1, completed_only=True, key="Done"):
    """
    Removes nuredduna standard input (stdin) files, of the form python.exxxx (s. error) and python.oxxxx (s. output).
    """
    if completed_only:
        deleted = 0
        for f in os.listdir(parent_dir):
            if f.endswith("out"):
                ff = os.path.join(parent_dir, f)
                if any(l.startswith(key) for l in open(ff).readlines()):
                    os.remove(ff)
                    os.remove("{}.err".format(os.path.splitext(ff)[0]))
                    deleted += 1
        if verbose:
            print(f"Deleted {2*deleted} files ({deleted} completed programmes).")   
    else:
        delete_files_by_ext(parent_dir, [".e", ".o"], verbose)
    return

def empty_trash(verbose=1):
    home = os.path.expanduser("~")
    binDir = f"{home}/.local/share/Trash"
    deleted = 0
    for root, dirs, files in os.walk(binDir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
            deleted += 1
    if verbose:
        print(f"Deleted {deleted} files.")
    return