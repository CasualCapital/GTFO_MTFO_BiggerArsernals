import os

from ReleaseManager import ReleaseManager
from ResourcePackEditor import ResourcePackEditor
from SkinEditor import SkinEditor
from WeaponArcheTypeEditor import WeaponArcheTypeEditor

os.environ['GAMEDATA_VERSION'] = '31994'
os.environ['MOD_VERSION'] = '7.0.4'

os.environ['DATABLOCK_PATH'] = "Datablocks/GameData_" + os.environ['GAMEDATA_VERSION']
os.environ['DESTINATION_PATH'] = "BepInEx/plugins/GameData_" + os.environ['GAMEDATA_VERSION']


def main():
    release = ReleaseManager()
    release.initialize_directories()

    editors = [WeaponArcheTypeEditor(), ResourcePackEditor(), SkinEditor()]
    for editor in editors:
        editor.apply()
        editor.save()

    release.create_release()


main()
