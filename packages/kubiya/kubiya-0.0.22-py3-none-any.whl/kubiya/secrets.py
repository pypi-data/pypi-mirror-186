from typing import Optional
from os import environ
from .loader import get_all_action_stores

def get_secret(name: str) -> Optional[str]:
    """get a secret from the environment"""
    registered_secrets = [
        secret
        for action_store in get_all_action_stores()
        for secret in action_store.get_registered_secrets()
    ]
    if name not in registered_secrets:
        raise AssertionError(f"secret {name} is not registered")

    if name not in environ:
        raise AssertionError(f"secret {name} is not set")
    return environ[name]