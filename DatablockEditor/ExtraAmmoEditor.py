from DatablockEditor.Editor import Editor
from DatablockEditor.ModTypes import ModType


class ExtraAmmoOnlyEditor(Editor):
    def __init__(self):
        super(ExtraAmmoOnlyEditor, self).__init__()

    def save(self):
        self.__write_data_block__(ModType.EXTRA_AMMO)
