"""
Natural gas pressure drop changing depending the soil humidity
"""
import matplotlib.pyplot as plt
from matplotlib import rcParams

from examples.pipe_object import pipe

rcParams["font.family"] = "Times New Roman"
rcParams["font.size"] = "12"
cm = 1/2.54

pipes = []

soil_humidity_stack = range(10, 31, 1)  # natural gas initial temperature

x = []
y = []

for w in soil_humidity_stack:
    pipe.soil_humidity = w
    x.append(pipe.soil_humidity)
    pipe.get_pressure_by_crd(150e3)
    y.append(pipe.pressure_initial - pipe.pressure_final)

plt.plot(x, y, label="Падение давления при изменении влажности грунта")

plt.xlabel(r"$\mathrm{\omega}, \%$")
plt.ylabel(r"$\mathrm{\Delta}P,$" + "\n Pa")
axes = plt.gca()
axes.set_xlim([10, 31])
axes.set_ylim([2.2e6, 2.6e6])
plt.legend()
plt.grid(True)
plt.show()

