"""
Changing the parameters of natural gas along the length of the gas pipeline.
Calculations with variations in ambient temperature.
fig. 5, 6
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams, ticker

from copy import copy
from examples.for_article.pipe_object import pipe

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["mathtext.fontset"] = "stix"
rcParams["font.size"] = "14"

pipes = []
t_gr_list = range(0, 26, 1)
for t_gr in t_gr_list:
    pipe_var = copy(pipe)
    pipe_var.temperature_soil = t_gr+273
    pipes.append(pipe_var)

axes = {}
fig = {}
figures = ['fig.5', 'fig.6']

for figure in figures:
    fig[figure], axes[figure] = plt.subplots()

x, y1, y2, y3, y4, y5, y6, y7, y8 = [[] for _ in range(0, 9)]
for variant in pipes:
    x.append(variant.temperature_soil - 273)
    variant.get_pressure_by_crd(150e3)
    y1.append(variant.temperature_medium - 273)
    y2.append(variant.temperature_final - 273)
    y3.append(variant.pressure_final/1e5)
    y4.append(variant.pressure_initial - variant.pressure_final)
    y5.append(variant.reynolds)
    y6.append(round(variant.hydraulic_resistance_coefficient, 7))
    y7.append(variant.natural_gas.viscosity_kinematic)
    y8.append(variant.velocity)

# Gas final temperature depending the temperature of environment
axes['fig.5'].plot(x, y2, label="Final temperature of natural gas")
axes['fig.5'].set_ylabel(r'$\mathrm{t_{fin}}$,' + '\n℃', rotation=0, labelpad=25)
axes['fig.5'].set_xlabel(r'$\mathrm{t_{env}}$, ℃')
axes['fig.5'].yaxis.set_major_locator(ticker.MultipleLocator(5))
axes['fig.5'].yaxis.set_minor_locator(ticker.MultipleLocator(1))
axes['fig.5'].set_ylim(5)

# Gas final pressure depending the temperature of environment
axes['fig.6'].plot(x, y3, label="Final pressure of natural gas")
axes['fig.6'].set_ylabel(r'$\mathrm{P_{fin}}$,' + '\nbar', rotation=0, labelpad=15)
axes['fig.6'].set_xlabel(r'$\mathrm{t_{env}}$, ℃')
axes['fig.6'].yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
axes['fig.6'].set_ylim(35)

cm = 1/2.54
for key, ax in axes.items():
    ax.grid(True)
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.set_xlim(0)
    fig[key].set_size_inches(15*cm, 7*cm)
    fig[key].subplots_adjust(left=0.171, bottom=0.212, right=0.971, top=0.92, wspace=0.26, hspace=0.42)
    fig[key].savefig(f'{key}.jpg', dpi=1000)

plt.show()

