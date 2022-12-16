import json
import os

from DatablockEditor.ModTypes import ModType


class Editor:
    def __init__(self):
        self.src_path = os.environ['DATABLOCK_PATH']
        self.dest_path = os.environ['DESTINATION_PATH']
        self.mod_version = os.environ['MOD_VERSION']
        self.filename = ""
        self.data = {}

    def load(self):
        filename = "/".join([self.src_path, self.filename])
        with open(filename, "r") as read_file:
            self.data = json.load(read_file)

    def apply(self):
        pass

    def save(self):
        self.__write_data_block__(ModType.BASE)
        self.__write_data_block__(ModType.EXTRA_AMMO)

    def __write_data_block__(self, mod_type):
        filename = "/".join(["dist", self.mod_version, mod_type.value, self.dest_path, self.filename])
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as write_file:
            json.dump(self.data, write_file, sort_keys=True, indent=4)
