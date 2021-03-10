from . import formula
from .natural_gases import NaturalGas


class Pipeline:

    def __init__(self, natural_gas_title='shebelinka'):
        self.natural_gas = NaturalGas(natural_gas_title)



        self.equivalent_roughness = None
        self.delta = None
        self.inner_diameter = None
        self.temperature_critical = None
        self.temperature_medium = None
        self.volume_flow_standard = None
        self.pressure_initial = None
        self.pressure_critical = None
        self.pressure_medium = None

    def get_pressure_by_crd(self, x):
        psr_calc = pk = 0
        inaccuracy = 1
        while inaccuracy > 0.001:
            self.pressure_medium = psr_calc
            pk = self.get_final_pressure_by_x(x)
            psr_calc = formula.pressure_medium(self.pressure_initial, pk)
            inaccuracy = abs(self.pressure_medium - psr_calc)
            print(psr_calc)
        return pk

    def get_final_pressure_by_x(self, x):
        return formula.pressure_final(
            p0=self.pressure_initial,
            psr=self.pressure_medium,
            pkr=self.natural_gas.pressure_pseudo_critical,
            Q=self.volume_flow_standard,
            Tsr=self.temperature_medium,
            Tkr=self.temperature_critical,
            d=self.inner_diameter,
            delta=self.delta,
            k=self.equivalent_roughness,
            x=x
        )

    def get_compressibility(self):
        return formula.ng_compressibility_factor(
            pkr=self.natural_gas.pressure_pseudo_critical,
            tkr=self.temperature_critical,
            p=self.pressure_medium,
            t=self.temperature_medium
        )
