def get_properties(title):
    if title == 'CH4':
        return {'density_normal': 0.717, 'density_standard': 0.669, 'molar_mass': 16.04}
    elif title == 'C2H6':
        return {'density_normal': 1.356, 'density_standard': 1.264, 'molar_mass': 30.07}
    else:
        return {}


class GasComponent:

    def __init__(self, title, volume_percentage):
        self.density_normal = get_properties(title)['density_normal']
        self.density_standard = get_properties(title)['density_standard']
        self.molar_mass = get_properties(title)['molar_mass']
        self.volume_percentage = volume_percentage

