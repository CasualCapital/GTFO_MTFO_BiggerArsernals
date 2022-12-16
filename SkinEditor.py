import json

from DatablockEditor.Editor import Editor


class SkinEditor(Editor):
    def __init__(self):
        super(SkinEditor, self).__init__()
        self.filename = 'GameData_PlayerOfflineGearDataBlock_bin.json'
        self.excluded = ['NanoSwarm',
                         'DMRSemi_Special',
                         'DMRAuto',
                         'RifleCQB',
                         'RevolverBurst',
                         'Map_Device',
                         'Mine_Deployer_Glue',
                         'RifleSemi']
        self.load()

    def apply(self):
        self.unlock_skins()
        self.add_new_skins()

    def unlock_skins(self):
        for keys in self.data['Blocks']:
            if keys['name'] in self.excluded:
                keys['internalEnabled'] = False
                print(keys['name'] + " set to disabled")
            else:
                keys['internalEnabled'] = True
                print(keys['name'] + " set to enabled")

    def add_new_skins(self):
        with open("resource/new_weapon.json", "r") as read_file:
            new_weapon_data = json.load(read_file)

        for weapon in new_weapon_data['Blocks']:
            self.data.get('Blocks', []).append(weapon)
            print("Adding new weapon skin for " + weapon['name'])