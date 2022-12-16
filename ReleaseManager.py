import shutil
import os
from distutils.dir_util import copy_tree

from DatablockEditor.ModTypes import ModType


class ReleaseManager:
    def __init__(self):
        self.mod_version = os.environ['MOD_VERSION']
        self.dest_path = os.environ['DESTINATION_PATH']
        self.src_path = os.environ['DATABLOCK_PATH']

    def initialize_directories(self):
        print("initializing directories...")
        base_mode_dir = "/".join(["dist", self.mod_version, ModType.BASE.value, self.dest_path])
        ammo_mod_dir = "/".join(["dist", self.mod_version, ModType.EXTRA_AMMO.value, self.dest_path])
        copy_tree(self.src_path, base_mode_dir)
        copy_tree(self.src_path, ammo_mod_dir)

    def create_release(self):
        print("creating release: " + self.mod_version)
        self.__create_release_zip__(ModType.BASE, "BiggerArsernals")
        self.__create_release_zip__(ModType.EXTRA_AMMO, "BiggerArsernals-ExtraAmmo")

    def __create_release_zip__(self, mod_type, file_prefix):
        filename = "-".join([file_prefix, self.mod_version]);
        shutil.make_archive("release/" + filename, 'zip', "dist/" + self.mod_version + "/" + mod_type.value + "/")


