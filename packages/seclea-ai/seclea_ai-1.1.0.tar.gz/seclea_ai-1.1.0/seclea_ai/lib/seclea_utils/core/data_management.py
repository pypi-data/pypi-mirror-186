class ToVariableWriter:
    def __init__(self):
        self._data_bytes = []

    @property
    def data_bytes(self):
        return b"".join(self._data_bytes)

    @property
    def data_str(self):
        return self.data_bytes.decode("utf-8")

    def write(self, d: bytes):
        self._data_bytes.append(d)
