def get_properties(title):
    if title == 'CH4':
        return {'density_standard': 0.669, 'density_normal': 0.717}
    elif title == 'C2H6':
        return {{'density_standard': 1.264, 'density_normal': 1.356}}
    else:
        return {}


class GasComponent:

    def __init__(self, title, volume_percentage):
        self.density_standard = get_properties(title)['density_standard']
        self.density_normal = get_properties(title)['density_normal']
        self.volume_percentage = volume_percentage

