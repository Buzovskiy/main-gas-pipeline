"""
Plot for the parameter of the transported gas depending the humidity of soil.
Figures 12, 13, 14, 15, 16
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams, ticker
from copy import copy
from examples.for_article.pipe_object import pipe

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["mathtext.fontset"] = "stix"
rcParams["font.size"] = "14"

pipes = []
parameters_list = range(0, 21, 1)  # the variation of soil humidity, %
for parameter in parameters_list:
    pipe_var = copy(pipe)
    pipe_var.soil_humidity = parameter
    pipes.append(pipe_var)

axes = {}
fig = {}
figures = ['fig.12', 'fig.13', 'fig.14', 'fig.15', 'fig.16']

for figure in figures:
    fig[figure], axes[figure] = plt.subplots()

x, y1, y2, y3, y4, y5, y6, y7, y8, y9 = [[] for _ in range(0, 10)]

for variant in pipes:
    x.append(variant.soil_humidity)
    variant.get_pressure_by_crd(150e3)
    y1.append(variant.temperature_medium - 273)
    y2.append(variant.temperature_final - 273)
    y3.append(variant.pressure_final/1e5)
    y4.append(variant.pressure_initial - variant.pressure_final)
    y5.append(variant.reynolds)
    y6.append(round(variant.hydraulic_resistance_coefficient, 7))
    y7.append(variant.natural_gas.viscosity_kinematic)
    y8.append(variant.velocity)
    y9.append(variant.soil_heat_conductivity)

axes['fig.12'].plot(x, y9, label="coefficient of heat conductivity")
axes['fig.12'].set_ylabel(r"$\mathrm{\lambda_{soil}}$, " + "\n" + r"$\mathrm{\dfrac{W}{m \cdot K}}$", rotation=0, labelpad=19)
axes['fig.12'].set_xlabel(r'$\mathrm{\omega}$, %')
axes['fig.12'].set_ylim(1)
axes['fig.12'].yaxis.set_major_locator(ticker.MultipleLocator(0.1))

axes['fig.13'].plot(x, y1, label="Medium temperature of natural gas")
axes['fig.13'].set_ylabel(r'$\mathrm{t_{med}}$,' + '\n℃', rotation=0, labelpad=17)
axes['fig.13'].set_xlabel(r'$\mathrm{\omega}$, %')
axes['fig.13'].set_ylim(26.5)

axes['fig.14'].plot(x, y3, label="Final pressure of natural gas")
axes['fig.14'].set_ylabel(r'$\mathrm{P_{fin}}$,' + '\nbar', rotation=0, labelpad=17)
axes['fig.14'].set_xlabel(r'$\mathrm{\omega}$, %')
axes['fig.14'].set_ylim(35.8)

axes['fig.15'].plot(x, y8, label="Natural gas velocity \n for medium parameters")
axes['fig.15'].set_ylabel("v, \n" + r"$\mathrm{\dfrac{m}{s}}$", rotation=0, labelpad=17)
axes['fig.15'].set_xlabel(r'$\mathrm{\omega}$, %')
axes['fig.15'].set_ylim(8.46)

axes['fig.16'].plot(x, y7, label="Kinematic viscosity coefficient \n for medium parameters")
axes['fig.16'].set_ylabel(r"$\mathrm{\nu},$" + "\n" + r"$\mathrm{\dfrac{m^2}{s}}$", rotation=0, labelpad=17)
axes['fig.16'].set_xlabel(r'$\mathrm{\omega}$, %')
axes['fig.16'].set_ylim(3.11e-7)

cm = 1/2.54
for key, ax in axes.items():
    ax.grid(True)
    ax.set_xlim(min(x), max(x))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    fig[key].set_size_inches(15*cm, 7*cm)
    fig[key].subplots_adjust(left=0.171, bottom=0.212, right=0.971, top=0.92, wspace=0.26, hspace=0.42)
    fig[key].savefig(f'{key}.jpg', dpi=1000)

plt.show()

