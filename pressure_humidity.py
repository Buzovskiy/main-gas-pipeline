"""
Natural gas pressure drop changing depending the soil humidity
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter

from copy import copy

from pipe_object import pipe

rcParams["font.family"] = "Times New Roman"
rcParams["font.size"] = "12"
cm = 1/2.54

pipes = []

soil_humidity_stack = range(10, 31, 1)  # natural gas initial temperature
# for w in soil_humidity_stack:
#     pipe_variant = copy(pipe)
#     pipe_variant.soil_humidity = w
#     pipes.append(pipe_variant)

x = []
y = []

for w in soil_humidity_stack:
    pipe.soil_humidity = w
    x.append(pipe.soil_humidity)
    pipe.get_pressure_by_crd(150e3)
    y.append(pipe.pressure_initial - pipe.pressure_final)

axes = {}

# for variant in pipes:
#     x.append(variant.soil_humidity)
#     variant.get_pressure_by_crd(150e3)
#     y.append(variant.pressure_initial - variant.pressure_final)


plt.plot(x, y, label="Падение давления при изменении влажности грунта")
#
# plt.plot([0, 150e3/1000], [12, 12], label="Temperature of soil, "+r"$t_{soil}=12℃$")
plt.xlabel(r"$\mathrm{\omega}, \%$")
plt.ylabel(r"$\mathrm{\Delta}P,$" + "\n Pa")
axes = plt.gca()
axes.set_xlim([10, 31])
axes.set_ylim([2.2e6, 2.6e6])
plt.legend()
plt.grid(True)
# fig = plt.gcf()
# # fig.set_size_inches(8*cm, 7*cm)
# # figure(figsize=())
# plt.savefig('t_init.jpg', dpi=500)
plt.show()
# exit()
