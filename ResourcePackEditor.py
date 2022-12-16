from DatablockEditor.ExtraAmmoEditor import ExtraAmmoOnlyEditor


class ResourcePackEditor(ExtraAmmoOnlyEditor):
    def __init__(self):
        super(ResourcePackEditor, self).__init__()
        self.filename = 'GameData_PlayerDataBlock_bin.json'
        self.load()

    def apply(self):
        for keys in self.data['Blocks']:
            before_ammo = keys['AmmoStandardResourcePackMaxCap']
            before_special = keys['AmmoSpecialResourcePackMaxCap']
            keys['AmmoStandardResourcePackMaxCap'] = 900
            keys['AmmoSpecialResourcePackMaxCap'] = 585
            print("Setting AmmoPack from " + str(before_ammo) + " to " + str(keys['AmmoStandardResourcePackMaxCap']))
            print("Setting SpecialAmmoPack from " + str(before_special) + " to "
                  + str(keys['AmmoSpecialResourcePackMaxCap']))
