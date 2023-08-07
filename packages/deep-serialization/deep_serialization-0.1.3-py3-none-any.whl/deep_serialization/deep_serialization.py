import json
from typing import Any, Tuple, List

from deep_serialization.memory_objects import PythonSerializer
from deep_serialization.json_converter import MemoryDumpEncoder


def serialize_object(obj: Any) -> Tuple[str, str]:
    """
    Serialize one object.
    Returns the object id and memory dump.
    """

    serializer = PythonSerializer()
    id_ = serializer.write_object_to_memory(obj)
    return id_, json.dumps({'objects': serializer.memory}, cls=MemoryDumpEncoder)


def serialize_objects(objs: List[Any]) -> Tuple[List[str], str]:
    """
    Serialize objects with shared memory.
    Returns list of object ids and memory dump.
    """

    serializer = PythonSerializer()
    ids = [
        serializer.write_object_to_memory(obj)
        for obj in objs
    ]
    return ids, json.dumps({'objects': serializer.memory}, cls=MemoryDumpEncoder)
