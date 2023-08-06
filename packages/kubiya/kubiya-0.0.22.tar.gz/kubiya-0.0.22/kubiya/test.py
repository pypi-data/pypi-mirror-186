from kubiya import action_store
from kubiya.loader import load_action_store
from sys import argv, exit

def show_all():
    instances = action_store.ActionStore._instances
    if not instances:
        print("No action stores found")
        exit(1)
    if len(instances) > 1:
        print("Multiple action stores found: {instances}")
        exit(1)
    for instance in instances:
        print(f"{instance.get_name()}:")
        for action in instance.get_registered_actions():
            print(f"  {action}")

if __name__ == "__main__":    
    if len(argv) != 2:
        print("Usage: python3 -m kubiya.serve <action_store_file.py>")
        exit(1)
    
    load_action_store(argv[1])
    show_all()
