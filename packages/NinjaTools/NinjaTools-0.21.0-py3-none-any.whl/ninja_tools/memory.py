from typing import List

try:
    import psutil
    import pymem
except ImportError:
    raise 'pip install ninjatools[memory] or ninjatools[all]  to use image functions!'

# from ninja_tools.utils import Utilities
# Utilities.try_import('ReadWriteMemory', 'git+https://github.com/vsantiago113/ReadWriteMemory')

from ninja_tools.ReadWriteMemory import ReadWriteMemory


class Parser:
    def __init__(self, pid: int):
        self.pid = pid

        self.rwm = ReadWriteMemory()
        self.process = self.rwm.get_process_by_id(pid)
        self.process.open()

        self.process_name = self.process.name

        self.pm = pymem.Pymem()
        self.pm.open_process_from_id(pid)
        self.base_address = pymem.process.module_from_name(
            self.pm.process_handle, self.process_name).lpBaseOfDll

    # Readers
    def read(self, address):
        # return self.process.read(address)
        return self.pm.read_int(address)

    def read_str(self, address: int, length: int):
        # return self.process.readString(address, length)
        return self.pm.read_string(address, length)

    def read_byte(self, address: int, length: int = 1):
        # return self.process.readByte(address, length)
        return self.pm.read_bytes(address, length)

    # Writers
    def write(self, address: int, integer: int):
        # return self.process.write(address, integer)
        return self.pm.write_int(address, integer)

    def write_str(self, address: int, string: str):
        # return self.process.writeString(address, string)
        return self.pm.write_string(address, string)

    def write_byte(self, address: int, bytes_: List[hex]):
        return self.process.writeByte(address, bytes_)
        # return self.pm.write_bytes(address, bytes_)

    # Resolvers
    def resolve(self, address: int, offsets: List):
        return self.process.get_pointer(address, offsets=offsets)

    def resolver(self, address: int, offsets: List):
        # return self.process.read(self.resolve(address, offsets))
        return self.pm.read_int(self.resolve(address, offsets))

    def resolver_str(self, address: int, length: int, offsets: List):
        # return self.read_str(self.resolve(address, offsets), length)
        return self.pm.read_string(self.resolve(address, offsets), length)

    def resolver_byte(self, address: int, length: int = 1, offsets: List = ()):
        # return self.read_byte(self.resolve(address, offsets), length)
        return self.pm.read_bytes(self.resolve(address, offsets), length)
