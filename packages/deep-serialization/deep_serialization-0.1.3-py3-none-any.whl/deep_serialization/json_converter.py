import json
from deep_serialization.memory_objects import (
    MemoryObject,
    ReprMemoryObject,
    ListMemoryObject,
    DictMemoryObject,
    ReduceMemoryObject,
    MemoryDump
)


class MemoryObjectEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, MemoryObject):
            base_json = {
                'strategy': o.strategy,
                'kind': o.kind,
                'comparable': o.comparable,
            }
            if isinstance(o, ReprMemoryObject):
                base_json['value'] = o.value
            elif isinstance(o, (ListMemoryObject, DictMemoryObject)):
                base_json['items'] = o.items
            elif isinstance(o, ReduceMemoryObject):
                base_json['constructor'] = o.constructor
                base_json['args'] = o.args
                base_json['state'] = o.state
                base_json['listitems'] = o.listitems
                base_json['dictitems'] = o.dictitems
            return base_json
        return json.JSONEncoder.default(self, o)


class MemoryDumpEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, MemoryDump):
            return {id_: MemoryObjectEncoder().default(o) for id_, o in o.objects.items()}
        return json.JSONEncoder.default(self, o)
