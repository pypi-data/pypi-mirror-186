#!/usr/bin/env python3

# Standard libraries
from copy import deepcopy
from io import TextIOWrapper
from sys import maxsize
from typing import Any, Dict, List

# Modules libraries
from yaml import dump as yaml_dump, load as yaml_load
from yaml import SafeLoader as yaml_SafeLoader, YAMLError as yaml_Error
from yaml.nodes import SequenceNode as yaml_SequenceNode

# YAML class
class YAML:

    # Data type
    Data = Dict[str, Any]

    # Error type
    Error = yaml_Error

    # Reference class
    class Reference:

        # Constants
        NESTED_LIMIT: int = 10
        TAG: str = '!reference'

        # Constructor
        def __init__(self, values: List[str]):
            self._values = values

        # Values
        @property
        def values(self) -> List[str]:
            return self._values

        # Add constructor
        @staticmethod
        def add_constructor(loader: yaml_SafeLoader,
                            node: yaml_SequenceNode) -> 'YAML.Reference':
            return YAML.Reference(loader.construct_sequence(node))

        # Resolve, pylint: disable=too-many-branches
        @staticmethod
        def resolve(data: Any, node: Any) -> bool:

            # Variables
            changed: bool = False

            # Dictionnaries
            if isinstance(node, dict):
                for key in list(node.keys()):
                    if isinstance(node[key], YAML.Reference):
                        references = list(node[key].values)
                        referenced_node = data
                        for reference in references:
                            if reference in referenced_node:
                                referenced_node = referenced_node[reference]
                            else: # pragma: no cover
                                referenced_node = None
                                break
                        changed = True
                        if referenced_node:
                            node[key] = deepcopy(referenced_node)
                        else: # pragma: no cover
                            del node[key]
                    elif YAML.Reference.resolve(data, node[key]):
                        changed = True

            # Lists
            elif isinstance(node, list):
                for index in reversed(range(len(node))):
                    if isinstance(node[index], YAML.Reference):
                        references = list(node[index].values)
                        referenced_node = data
                        for reference in references:
                            if reference in referenced_node:
                                referenced_node = referenced_node[reference]
                            else: # pragma: no cover
                                referenced_node = None
                                break
                        changed = True
                        if referenced_node:
                            node[index:index + 1] = deepcopy(referenced_node)
                        else: # pragma: no cover
                            del node[index]
                    elif YAML.Reference.resolve(data, node[index]):
                        changed = True # pragma: no cover

            # Standard types
            else:
                pass

            # Result
            return changed

    # Load
    @staticmethod
    def load(stream: TextIOWrapper) -> Data:

        # Prepare loader class
        loader = yaml_SafeLoader
        loader.add_constructor(YAML.Reference.TAG, YAML.Reference.add_constructor)

        # Load YAML data
        data: YAML.Data = yaml_load(stream, Loader=loader)

        # Result
        return data

    # Dump
    @staticmethod
    def dump(data: Data) -> str:

        # Dump YAML data
        return str(yaml_dump(data, indent=2, sort_keys=False, width=maxsize))

    # Resolve
    @staticmethod
    def resolve(data: Dict[Any, Any]) -> None:

        # Resolve references
        for _ in range(YAML.Reference.NESTED_LIMIT):
            if not YAML.Reference.resolve(data, data):
                break
        else:
            # error
            pass
