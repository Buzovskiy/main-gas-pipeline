# from main_gas_pipeline.gas_components import GasComponent
#
# c = GasComponent('CH4', 85)
# class Pipe:
#
#     def __init__(self, D, delta):
#         self.D = D
#         self.delta = delta
#
#     @property
#     def d(self):
#         return self.D - self.delta * 2
#
#
# p = Pipe(1220, 10)
# print(p.d)
# p.D = 1020
# print(p.d)
from main_gas_pipeline.natural_gases import NaturalGas
ng = NaturalGas('shebelinka')
ng.pressure = 6e6
ng.temperature = 300
print(ng.viscosity_dynamic)
ng.temperature = 290
print(ng.viscosity_dynamic)
