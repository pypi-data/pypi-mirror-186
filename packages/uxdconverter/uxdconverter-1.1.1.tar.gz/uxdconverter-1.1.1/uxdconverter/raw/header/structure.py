import struct


class AbstractStructure(object):

    LENGTH_INTEGER = 4
    LENGTH_FLOAT = 4
    LENGTH_DOUBLE = 8
    BYTEORDER = 'little'

    def __init__(self, raw):
        if not isinstance(raw, bytes):
            raise RuntimeError("Given data is not an instance of bytes")

        self._raw = raw

    def get_data(self, address, length):
        if address < 0 or length < 0 or not isinstance(address, int) or not isinstance(length, int):
            raise RuntimeError("Address and length must be non-negative integers")

        if len(self._raw) < address + length:
            raise RuntimeError("Cannot access data at address %s with length %s" % (address, length))

        return self._raw[address: address + length]

    def get_string(self, address, length):
        # Note that the string must end with \0
        data = self.get_data(address, length)

        return data.decode('utf-8').strip(chr(0x0))

    def get_integer(self, address, signed=False):
        return int.from_bytes(self.get_data(address, self.LENGTH_INTEGER), byteorder=self.BYTEORDER, signed=signed)

    def get_float(self, address):
        return self.get_float4(address)

    def get_double(self, address):
        return self.get_float8(address)

    def get_float4(self, address):
        return struct.unpack('<f', self.get_data(address, 4))[0]

    def get_float8(self, address):
        return struct.unpack('<d', self.get_data(address, self.LENGTH_DOUBLE))[0]
