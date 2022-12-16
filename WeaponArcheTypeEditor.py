from DatablockEditor.ExtraAmmoEditor import ExtraAmmoOnlyEditor


class WeaponArcheTypeEditor(ExtraAmmoOnlyEditor):
    def __init__(self):
        super(WeaponArcheTypeEditor, self).__init__()
        self.filename = 'GameData_ArchetypeDataBlock_bin.json'
        self.excluded = ['GEAR_SentryGun_Semi_sniper',
                         'GEAR_SentryGun_Burst',
                         'GEAR_SentryGun_Auto_staggering',
                         'GEAR_SentryGun_Shotgun_Semi']
        self.load()

    def apply(self):
        self.add_extra_ammo(2.0)

    def add_extra_ammo(self, factor=2.0):
        for keys in self.data['Blocks']:
            if keys['name'] not in self.excluded:
                before = keys['CostOfBullet']
                keys['CostOfBullet'] /= factor
                print(keys['name'] + " Cost change from " + str(before) + " to " + str(keys['CostOfBullet']))
