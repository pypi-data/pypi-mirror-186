from kubiya import action_store
from kubiya.http import serve
from kubiya.loader import get_all_action_stores, load_action_store
from sys import argv, exit


def serve_all(filename=None):
    action_stores = get_all_action_stores()
    if not action_stores:
        print("No action stores found")
        exit(1)
    if len(action_stores) > 1:
        print("Multiple stores found: {instances}")
        exit(1)
    serve(action_stores[0], filename)

if __name__ == "__main__":    
    if len(argv) != 2:
        print("Usage: python3 -m kubiya.serve <action_store_file.py>")
        exit(1)
    
    store_file = load_action_store(argv[1])
    serve_all(store_file)
