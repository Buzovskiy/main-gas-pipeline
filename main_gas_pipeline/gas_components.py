def get_properties(title):
    """
        Bykov, p. 40
        Density normal, kg/m3: T = 273 K, p = 101300 Pa.
        Density standard, kg/m3: T = 293 K, p = 101300 Pa.
        Molar mass, kg/kmole.
    """
    if title == 'methane':
        return {'formula': 'CH4', 'density_normal': 0.717, 'density_standard': 0.669, 'molar_mass': 16.04}
    elif title == 'ethane':
        return {'formula': 'C2H6', 'density_normal': 1.356, 'density_standard': 1.264, 'molar_mass': 30.07}
    elif title == 'propane':
        return {'formula': 'C3H8', 'density_normal': 2.010, 'density_standard': 1.872, 'molar_mass': 44.09}
    elif title == 'butane':
        return {'formula': 'C4H10', 'density_normal': 2.702, 'density_standard': 2.519, 'molar_mass': 58.12}
    elif title == 'pentane':
        return {'formula': 'C5H12', 'density_normal': 3.457, 'density_standard': 3.228, 'molar_mass': 72.15}
    elif title == 'nitrogen':
        return {'formula': 'N2', 'density_normal': 1.251, 'density_standard': 1.165, 'molar_mass': 28.02}
    elif title == 'carbon_monoxide':
        return {'formula': 'CO', 'density_normal': 1.250, 'density_standard': 1.165, 'molar_mass': 28.01}
    elif title == 'carbon_dioxide':
        return {'formula': 'CO2', 'density_normal': 1.977, 'density_standard': 1.842, 'molar_mass': 44.01}
    elif title == 'hydrogen_sulfide':
        return {'formula': 'H2S', 'density_normal': 1.539, 'density_standard': 1.434, 'molar_mass': 34.02}
    elif title == 'air':
        return {'formula': '-', 'density_normal': 1.293, 'density_standard': 1.206, 'molar_mass': 28.96}
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

