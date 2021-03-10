

class NaturalGas:

    def __init__(self, natural_gas_title):
        # if title == 'shebelinka':
        self.pressure_pseudo_critical = 4.64 * 10 ** 6  # ppk


def ng_components(component):
    return {
        'shebelinka': {'ch4': 94.1}
    }[component]


print(ng_components('shebelinka'))
