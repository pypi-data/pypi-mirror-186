from sys import exit
from pathlib import Path
import importlib.util
from . import action_store 

def load_action_store_file(file_path: str) -> str:
    file = Path(file_path).absolute()
    if not file.exists():
        raise AssertionError(f"File {file_path} does not exist")
    try:
        parents = str(file.parent)
        filename = file.name
        # print(f"Loading action store {filename} from {parents}")
        spec = importlib.util.spec_from_file_location(parents, file.absolute())
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.__file__
    except Exception as e:
        print(f"Error loading actions store file: {e}")
        exit(1)

def load_action_store(store_name: str) -> str:
    try:
        return load_action_store_file(store_name)
    except Exception as e:
        print(f"Error loading store {store_name}: ({e})")
        exit(1)

def get_all_action_stores(filename=None):
    return action_store.ActionStore._instances

def get_single_action_store():
    action_stores = get_all_action_stores()
    if len(action_stores) == 0:
        raise AssertionError("No action stores found")
    if len(action_stores) > 1:
        raise AssertionError(f"Multiple action stores found: {action_stores}")
    return action_stores[0]