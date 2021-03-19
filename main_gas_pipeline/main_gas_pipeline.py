from . import formula
from .natural_gases import NaturalGas


class Pipeline:

    def __init__(self, pressure_initial, volume_flow_standard, equivalent_roughness, inner_diameter,
                 temperature_initial, temperature_soil, natural_gas_title='shebelinka'):
        # Задаем природный газ
        self.natural_gas = NaturalGas(natural_gas_title)
        # self.natural_gas_title = natural_gas_title
        self.pressure_initial = pressure_initial
        self.volume_flow_standard = volume_flow_standard
        self.equivalent_roughness = equivalent_roughness
        self.inner_diameter = inner_diameter
        self.temperature_initial = temperature_initial
        self.temperature_soil = temperature_soil
        self.temperature_medium = temperature_initial

        self.pressure_medium = None

    def get_pressure_by_crd(self, x):
        psr_calc = self.pressure_initial
        pk = 0
        inaccuracy_p = 1
        while inaccuracy_p > 0.001:
            self.pressure_medium = psr_calc
            # self.natural_gas = NaturalGas(self.natural_gas_title, self.temperature_medium, self.pressure_medium)
            self.natural_gas.temperature = self.temperature_medium
            self.natural_gas.pressure = self.pressure_medium
            pk = self.get_final_pressure_by_x(x)
            psr_calc = formula.pressure_medium(self.pressure_initial, pk)
            inaccuracy_p = abs(self.pressure_medium - psr_calc)
            # print(psr_calc)
        return pk

    def get_final_pressure_by_x(self, x):
        return formula.pressure_final(
            p0=self.pressure_initial,
            psr=self.pressure_medium,
            Q=self.volume_flow_standard,
            Tsr=self.temperature_medium,
            Z=self.natural_gas.compressibility_factor,
            R=self.natural_gas.gas_constant,
            d=self.inner_diameter,
            ro_st=self.natural_gas.density_standard,
            k=self.equivalent_roughness,
            x=x
        )

    def get_final_temperature_by_x(self, x):
        return formula.temperature_final(
            x=x,
            Ksr=1.5,
            d=self.inner_diameter,
            p0=self.pressure_initial,
            psr=self.pressure_medium,
            Q=self.volume_flow_standard,
            Tsr=self.temperature_medium,
            Z=self.natural_gas.compressibility_factor,
            R=self.natural_gas.gas_constant,

            ro_st=self.natural_gas.density_standard,
            k=self.equivalent_roughness,
        )

    @property
    def mass_flow(self):
        return self.volume_flow_standard * self.natural_gas.density_standard

    # def get_compressibility(self):
    #     return formula.ng_compressibility_factor(
    #         pkr=self.natural_gas.pressure_pseudo_critical,
    #         tkr=self.temperature_critical,
    #         p=self.pressure_medium,
    #         t=self.temperature_medium
    #     )

    # @property
    # def drag_coefficient(self):
    #     """Hydraulic drag coefficient"""
    #     Eh = 0.95
    #     return (1.05 * Eh ** 2) * 0.067 * (158/self.Reynolds + 2 * self.)
