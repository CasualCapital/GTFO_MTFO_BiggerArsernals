from DatablockEditor.Editor import Editor
from DatablockEditor.ModTypes import ModType


class FlashLightOnlyEditor(Editor):
    def __init__(self):
        super(FlashLightOnlyEditor, self).__init__()

    def save(self):
        self.__write_data_block__(ModType.FLASH_LIGHT)
