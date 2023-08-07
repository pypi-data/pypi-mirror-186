import datetime
import json

from deep_serialization.memory_objects import PythonSerializer
from deep_serialization.json_converter import MemoryDumpEncoder


class B:
    def __init__(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.time = datetime.datetime.now()


if __name__ == '__main__':
    from pprint import pprint

    a = [1, 2, 3, {1: 1}, None, B(1, 2, 3)]
    serializer_ = PythonSerializer()
    pprint(serializer_.write_object_to_memory(a))
    pprint(serializer_.memory.objects)
    with open('test_json.json', 'w') as fout:
        print(json.dumps(serializer_.memory, cls=MemoryDumpEncoder, indent=True), file=fout)
