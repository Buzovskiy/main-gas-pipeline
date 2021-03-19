def get_properties(title):
    if title == 'CH4':
        return {'density_normal': 0.717, 'density_standard': 0.669, 'molar_mass': 16.04}
    elif title == 'C2H6':
        return {'density_normal': 1.356, 'density_standard': 1.264, 'molar_mass': 30.07}
    else:
        return {}


class GasComponent:

    def __init__(self, title, volume_percentage):
        self._density_normal = get_properties(title)['density_normal']
        self._density_standard = get_properties(title)['density_standard']
        self._molar_mass = get_properties(title)['molar_mass']
        self._volume_percentage = volume_percentage

    @property
    def density_normal(self):
        return self._density_normal

    @property
    def density_standard(self):
        return self._density_standard

    @property
    def molar_mass(self):
        return self._molar_mass

    @property
    def volume_percentage(self):
        return self._volume_percentage

