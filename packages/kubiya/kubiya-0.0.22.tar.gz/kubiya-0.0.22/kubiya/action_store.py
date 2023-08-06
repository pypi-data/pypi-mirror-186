import json
from typing import List, Dict, NoReturn, Any, Iterable, Optional
from pydantic import validate_arguments, BaseModel
from jsonschema import validate, ValidationError
import inspect
from logging import getLogger
import functools
import pydantic

logger = getLogger(__name__)

class ActionStore:
    """handles kubiya actions and exeution"""

    _instances = list()

    @classmethod
    def register_action_store(cls, action_store: "ActionStore") -> NoReturn:
        cls._instances.append(action_store)
    
    def __init__(self, store_name: str, version: str = "testing") -> None:
        assert store_name != "", "store_name cannot be empty"
        self._registered_actions = {}
        self._action_metadata = {}
        self._registered_secrets = []
        self._name = store_name
        self._version = version
        self.__class__.register_action_store(self)

    @classmethod
    def validate_action(cls, action: callable) -> NoReturn:
        cls._validate_action_is_callable(action)
        cls._validate_action_signature(action)

    @classmethod
    def _validate_action_is_callable(cls, action: callable) -> NoReturn:
        assert callable(
            action
        ), f"{action} must be callable in order to be registered as an action"

    @classmethod
    def _validate_action_signature(cls, action: callable) -> NoReturn:
        sig = inspect.signature(action)
        mandatory_args = [
            nm
            for nm, par in sig.parameters.items()
            if par.default == inspect.Signature.empty
            and par.kind not in (par.VAR_KEYWORD, par.VAR_POSITIONAL)
        ]
        if len(mandatory_args) > 1:
            raise AssertionError(
                f"{action} must have at most 1 mandatory argument ({mandatory_args})"
            )

    def register_action(self, action_name: str, action: callable) -> NoReturn:
        self.validate_action(action)
        self._registered_actions[action_name] = action

    def uses_secrets(self, secret_names: Iterable[str]) -> NoReturn:
        self._registered_secrets.extend(secret_names)

    def get_registered_actions(self) -> List[str]:
        return list(self._registered_actions.keys())

    def get_registered_action_info(self, action_name: str) -> callable:
        assert (
            action_name in self._registered_actions
        ), f"`{action_name}` is not a registered action"
        return self._registered_actions[action_name]

    def get_registered_actions_info(self) -> List[callable]:
        return self._registered_actions.values()

    def get_registered_secrets(self) -> List[str]:
        return self._registered_secrets

    def execute_action(self, action_name: str, input: Optional[Dict]) -> Any:
        assert (
            action_name in self._registered_actions
        ), f"`{action_name}` is not a registered action"
        action = self._registered_actions[action_name]
        if input is None:
            return action()
        else:
            return action(input)

    def get_version(self) -> str:
        return self._version

    def get_name(self) -> str:
        return self._name

    @staticmethod
    def validate_args(func, input_schema=None):
        """if input type input_schema exists, validate against it"""
        def wrapper(*args, **kwargs):
            if input_schema:
                try:
                    first_arg = func.__code__.co_varnames[0]
                    validate(args[0], input_schema)
                except ValidationError as e:
                    return {"error": {"argument": first_arg, "field": e.schema.get("title"), "message": e.message, "expected_type" : e.schema.get("type")}}
            return func(*args, **kwargs)
        return wrapper

    
    def kubiya_action(self, validate_input=False) -> callable:
        """dict(type for typy in inspect...)"""
        def decorator(func: callable):
            action_data = {
                "action_name": func.__name__,
                "description": func.__doc__,
            }
            parameters = list(inspect.signature(func).parameters.values())
            return_signature = inspect.signature(func).return_annotation
            if return_signature == inspect.Signature.empty:
                output_schema = self.annotation_to_schema(
                    Any, "Output not specified")
            else:
                output_schema = self.annotation_to_schema(
                    return_signature, "Output")

            if len(parameters) > 1:
                raise RuntimeError(
                    f"{func.__name__} must have at most one argument to be registered as a kubiya action")
            if not parameters:
                input_schema = self.annotation_to_schema(
                    Any, "Input not specified")
            if parameters:
                model = parameters[0]
                input_schema = self.annotation_to_schema(
                    model.annotation, model.name)
            action_data["input_schema"] = input_schema
            action_data["output_schema"] = output_schema
            self._action_metadata[func.__name__] = action_data
            if not validate_input:
                self.register_action(func.__name__, func)
            else:
                if action_data.get("input_schema"):
                    wrapped = self.validate_args(func, input_schema=input_schema)
                    self.register_action(func.__name__, wrapped)
                    return wrapped
            self.register_action(func.__name__, func)
            return func
        return decorator


    @staticmethod
    def annotation_to_schema(annotation: Any, title: str) -> str:
        if type(annotation) == pydantic.main.ModelMetaclass:
            return json.loads(annotation.schema_json())
        elif annotation == inspect.Signature.empty:
            return json.loads(pydantic.schema_json_of(Any, title=title))
        else:
            return json.loads(pydantic.schema_json_of(annotation, title=title))
