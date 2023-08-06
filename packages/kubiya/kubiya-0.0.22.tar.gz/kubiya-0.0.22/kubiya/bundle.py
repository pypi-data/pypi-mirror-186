from typing import List, Callable, Dict
from pathlib import Path, PosixPath
import importlib.util
from . import ActionStore
from .loader import get_single_action_store
from .http import serve, report_error
from sys import argv, exit,path
from os import environ
import traceback


def get_funcs_from_file(infile: PosixPath) -> List[Callable]:
    if not infile.is_file():
        raise AssertionError(f"File {infile} does not exist")
    try:
        parents = str(infile.parent)
        filename = infile.name
        # print(f"Loading action store {filename} from {parents}")
        spec = importlib.util.spec_from_file_location(parents, infile.absolute())
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        ret = list()
        for o in dir(module):
            if o.startswith("_"):
                continue
            try:
                f = getattr(module, o)
                if not callable(f):
                    continue
                if not hasattr(f, "__module__") or f.__module__  != module.__name__:
                    continue
                ActionStore.validate_action(f)
                ret.append(f)
            except Exception as ex:
                print("Error loading action: "+module.__name__ + "."+ o, ex)
                pass
        return ret

    except Exception as e:
        print(traceback.format_exc())
        raise

def get_all_dir_files(dirpath: PosixPath) -> List[PosixPath]:
    dirpath = Path(dirpath)
    if not dirpath.exists():
        raise AssertionError(f"Directory {dirpath} does not exist")
    return list(dirpath.glob("**/*.py"))

if __name__ == "__main__":
    if len(argv) <2:
        print("Usage: python3 -m kubiya.bundle <paths>")
        paths = [Path(arg) for arg in argv[1:]]
        exit(1)
    funcs = {}
    files = []
    dirs = []
    try:
        for arg in argv[1:]:
            p = Path(arg)
            if p.is_dir():
                dirs.append(p)
                files.extend(get_all_dir_files(p))
                path.append(str(p))
            elif p.is_file():
                path.append(str(p.parent))
                files.append(p)
        
        for filename in files:
            filefuncs = get_funcs_from_file(filename)
            if filefuncs: 
                funcs[filename.stem] = filefuncs

        actionstore = get_single_action_store()
        serve(actionstore)
    except Exception as e:
        print(traceback.format_exc())
        report_error(e)