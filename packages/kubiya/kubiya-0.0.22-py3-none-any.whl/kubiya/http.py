from operator import ge
from fastapi import FastAPI
import uvicorn
import os

import kubiya
from .action_store import ActionStore
from typing import Optional, Dict, Any
from uvicorn import run
from pydantic import BaseModel
import traceback

class Request(BaseModel):
    action: Optional[str]
    input: Optional[Any]
    secrets: Optional[Dict]

async def execute_handler(request: Request, action_store: ActionStore) -> Any:
    try:
        if request.action == '__KUBIYA_DISCOVER__':
            return {
                "name": action_store.get_name(),
                "version": action_store.get_version(),
                "registered_actions": action_store.get_registered_actions(),
                "secrets": action_store.get_registered_secrets(),
                "kubiya_version": "python-sdk: " + kubiya.__version__,
                "actions_metadata": action_store._action_metadata,
            }

        if request.secrets:
            for secret, secret_value in request.secrets.items():
                print("Setting secret: ", secret)
                os.environ[secret] = secret_value
        else:
            print("No secrets defined")
        return action_store.execute_action(request.action, request.input)
    except Exception as e:
        return {
            "error": str(e),
            "stacktrace": traceback.format_exc(),
        }

def serve(action_store: ActionStore, filename=None):
    kubiya_server = FastAPI(openapi_url=None)

    @kubiya_server.post("/")
    async def root(request: Request):
        return await execute_handler(request=request, action_store=action_store)

    uvicorn.run(kubiya_server, host="0.0.0.0", port=8080)

def report_error(error: Exception):
    kubiya_server = FastAPI(openapi_url=None)

    @kubiya_server.post("/", status_code=500)
    async def root(request: Request):
        return {
            "error": {
                "message": str(error),
                "trace": traceback.format_exc(),
            }
        }

    uvicorn.run(kubiya_server, host="0.0.0.0", port=8080)
