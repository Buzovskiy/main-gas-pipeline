# python -m main_gas_pipeline.natural_gases
from .gas_components import GasComponent
from .constants import Constants


class NaturalGas:

    def __init__(self, natural_gas_title, temperature=None, pressure=None):
        self.temperature = temperature
        self.pressure = pressure

        self.components = ng_components(natural_gas_title)

    @property
    def density_standard(self):
        """Natural gas density at standard temperature, kg/m3"""
        density_standard = 0
        for component in self.components:
            density_standard += component.density_standard * component.volume_percentage * 0.01
        return density_standard

    @property
    def molar_mass(self):
        """Natural gas molar mass, kg/kmole"""
        molar_mass = 0
        for component in self.components:
            molar_mass += component.molar_mass * component.volume_percentage * 0.01
        return molar_mass

    @property
    def gas_constant(self):
        """Gas constant of natural gas, J/(kg*K)"""
        return Constants.gas_constant / self.molar_mass

    @property
    def temperature_pseudocritical(self):
        """Natural gas pseudocritical temperature (CH4 > 85%), K"""
        return 155.24 * (0.564 + self.density_standard)

    @property
    def pressure_pseudocritical(self):
        """Natural gas pseudocritical pressure (CH4 > 85%), MPa"""
        return 0.1737 * (26.831 - self.density_standard)

    @property
    def density_relative(self):
        """Natural gas density relative to standard air density"""
        return self.density_standard / Constants.density_standard_air

    @property
    def pressure_reduced(self):
        return self.pressure * 10**-6 / self.pressure_pseudocritical

    @property
    def temperature_reduced(self):
        return self.temperature / self.temperature_pseudocritical

    @property
    def compressibility_factor(self):
        tau = 1 - 1.68 * self.temperature_reduced + 0.78 * self.temperature_reduced**2 + \
              0.0107 * self.temperature_reduced**3
        return 1 - 0.0241 * self.pressure_reduced / tau

    @property
    def specific_heat_capacity(self):
        """Isobar specific heat capacity Cp kJ/(kg*K)"""
        return 1.695 + 1.838 * 10**-3 * self.temperature + 1.96 * 10**6 * \
               (self.pressure * 10**-6 - 0.1) / self.temperature**3

    @property
    def joile_tomson_factor(self):
        """Joile-Tomson factor Di (K/MPa)"""
        return (1 / self.specific_heat_capacity) * (0.98 * 10**6 / self.temperature**2 - 1.5)

    @property
    def viscosity_dynamic(self):
        return 5.1 * 10**-6 * (1 + self.density_standard * (1.1 - 0.25 * self.density_standard)) * \
               (0.037 + self.temperature_reduced * (1 - 0.104 * self.temperature_reduced)) * \
               (1 + self.pressure_reduced**2 / (30 * (self.temperature_reduced - 1)))



def ng_components(component):
    return {
        'shebelinka': [GasComponent('CH4', 94.1), GasComponent('C2H6', 3.1)]
    }[component]







# print(ng_components('shebelinka')[0].__dict__)
# ng = NaturalGas('shebelinka')
# print(ng.density_standard)
# print(ng.molar_mass)
# print(ng.gas_constant)
# print(ng.temperature_pseudocritical)
# print(ng.pressure_pseudocritical)
# print(ng.density_relative)
