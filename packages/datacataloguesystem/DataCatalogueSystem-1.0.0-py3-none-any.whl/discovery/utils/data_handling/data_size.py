"""
Contains representations for data size
"""


class DataItemSize:
    attributes = {
        "size_representation": "undefined",
    }

    def __init__(self, **kwargs):
        pass

    def get_attributes(self):
        return self.attributes


class FileDataItemSize(DataItemSize):
    def __init__(self, no_of_rows, no_of_bytes):
        self.attributes = {
            "size_representation": "file",
            "no_of_rows": no_of_rows,
            "no_of_bytes": no_of_bytes
        }
