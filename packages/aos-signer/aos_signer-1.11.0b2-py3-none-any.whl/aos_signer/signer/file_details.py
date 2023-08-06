#
#  Copyright (c) 2018-2019 Renesas Inc.
#  Copyright (c) 2018-2019 EPAM Systems Inc.
#

import os
from hashlib import sha3_512


class FileDetailException(Exception):
    pass


class FileDetails:
    BLOCK_SIZE = 65536
    HASH_METHOD = sha3_512

    def __init__(self, root, file):
        self._root = root
        self._file = file
        self._hash = None
        self._size = None

    def calculate(self):
        hash_instance = self.HASH_METHOD()
        ffn = os.path.join(self._root, self._file)
        with open(ffn, "rb") as fp:
            buf = fp.read(self.BLOCK_SIZE)
            while buf:
                hash_instance.update(buf)
                buf = fp.read(self.BLOCK_SIZE)
        self._hash = hash_instance.hexdigest()
        self._size = os.path.getsize(ffn)

    @property
    def name(self):
        return os.path.join(".", self._file)

    @property
    def hash(self):
        if self._hash is None:
            raise FileDetailException("Data unavailable, calculation method was not called.")
        return self._hash

    @property
    def size(self):
        if self._size is None:
            raise FileDetailException("Data unavailable, calculation method was not called.")
        return self._size
