# python -m main_gas_pipeline.natural_gases
from .gas_components import GasComponent
from .constants import Constants
from .formulas import natural_gas as f_natural_gas


class NaturalGas:

    def __init__(self, natural_gas_title, temperature=None, pressure=None):
        self.temperature = temperature
        self.pressure = pressure

        self.components = ng_components(natural_gas_title)

    @property
    def density_standard(self):
        """Natural gas density at standard temperature, kg/m3"""
        return f_natural_gas.density_standard(components=self.components)

    @property
    def density(self):
        """Natural gas density, kg/m3"""
        return f_natural_gas.density(
            p=self.pressure,
            Z=self.compressibility_factor,
            R=self.gas_constant,
            T=self.temperature
        )

    @property
    def molar_mass(self):
        """Natural gas molar mass, kg/kmole"""
        return f_natural_gas.molar_mass(components=self.components)

    @property
    def gas_constant(self):
        """Gas constant of natural gas, J/(kg*K)"""
        return f_natural_gas.gas_constant(R=Constants.gas_constant, mu=self.molar_mass)

    @property
    def temperature_pseudocritical(self):
        """Natural gas pseudocritical temperature (CH4 > 85%), K"""
        return f_natural_gas.temperature_pseudocritical(ro_st=self.density_standard)

    @property
    def pressure_pseudocritical(self):
        """Natural gas pseudocritical pressure (CH4 > 85%), MPa"""
        return f_natural_gas.pressure_pseudocritical(ro_st=self.density_standard)

    @property
    def density_relative(self):
        """Natural gas density relative to standard air density"""
        return f_natural_gas.density_relative(ro_st=self.density_standard, ro_air_st=Constants.density_standard_air)

    @property
    def pressure_reduced(self):
        """Reduced pressure of the natural gas, dimensionless"""
        return f_natural_gas.pressure_reduced(p=self.pressure, p_pkr=self.pressure_pseudocritical)

    @property
    def temperature_reduced(self):
        """Reduced temperature of the natural gas, dimensionless"""
        return f_natural_gas.temperature_reduced(t=self.temperature, t_pkr=self.temperature_pseudocritical)

    @property
    def compressibility_factor(self):
        """Compressibility factor, dimensionless"""
        return f_natural_gas.compressibility_factor(t_pr=self.temperature_reduced, p_pr=self.pressure_reduced)

    @property
    def specific_isobaric_heat_capacity(self):
        """Isobar specific heat capacity Cp J/(kg*K)"""
        return f_natural_gas.specific_isobaric_heat_capacity(p=self.pressure, t=self.temperature)

    @property
    def joile_tomson_factor(self):
        """Joile-Tomson factor Di (K/MPa)"""
        return f_natural_gas.joile_tomson_factor(Cp=self.specific_isobaric_heat_capacity, t=self.temperature)

    @property
    def viscosity_dynamic(self):
        """Dynamic viscosity of the natural gas, Pa*s"""
        return f_natural_gas.viscosity_dynamic(ro_st=self.density_standard,
                                               T_pr=self.temperature_reduced,
                                               p_pr=self.pressure_reduced)

    @property
    def viscosity_kinematic(self):
        """Natural gas kinematic viscosity, m2/s"""
        return f_natural_gas.viscosity_kinematic(
            mu=self.viscosity_dynamic,
            ro=self.density
        )



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
