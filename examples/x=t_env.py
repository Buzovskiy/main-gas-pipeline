"""
Dependence of natural gas parameters on the variation of temperature of the environment
"""

import numpy as np
import matplotlib.pyplot as plt

from copy import copy
from examples.pipe_object import pipe

pipes = []
t_gr_list = range(0, 26, 1)
for t_gr in t_gr_list:
    pipe_var = copy(pipe)
    pipe_var.temperature_soil = t_gr+273
    pipes.append(pipe_var)

axes = {}
rows = 5
cols = 2

fig = plt.figure()
fig.subplots_adjust(left=0.1, bottom=0.05, right=0.96, top=0.98, wspace=0.26, hspace=0.4)

x, y1, y2, y3, y4, y5, y6, y7, y8 = [[] for _ in range(0, 9)]
for variant in pipes:
    x.append(variant.temperature_soil - 273)
    variant.get_pressure_by_crd(150e3)
    y1.append(variant.temperature_medium - 273)
    y2.append(variant.temperature_final - 273)
    y3.append(variant.pressure_final)
    y4.append(variant.pressure_initial - variant.pressure_final)
    y5.append(variant.reynolds)
    y6.append(round(variant.hydraulic_resistance_coefficient, 7))
    y7.append(variant.natural_gas.viscosity_kinematic)
    y8.append(variant.velocity)
graph_ind = 1
axes['ax1'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax1'].plot(x, y1, label="Medium temperature of natural gas")
axes['ax1'].set_ylabel(r'$t_{med}$,' + '\n℃', rotation=0, labelpad=13)
axes['ax1'].set_xlabel(r'$t_{env}$, ℃')

graph_ind += 1
axes['ax2'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax2'].plot(x, y2, label="Final temperature of natural gas")
axes['ax2'].set_ylabel(r'$t_{f}$,' + '\n℃', rotation=0, labelpad=13)
axes['ax2'].set_xlabel(r'$t_{env}$, ℃')

graph_ind += 1
axes['ax3'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax3'].plot(x, y3, label="Final pressure of natural gas")
axes['ax3'].set_ylabel(r'$p_{f}$,' + '\nPa', rotation=0, labelpad=13)
axes['ax3'].set_xlabel(r'$t_{env}$, ℃')

graph_ind += 1
axes['ax4'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax4'].plot(x, y4, label="Differential pressure of natural gas")
axes['ax4'].set_ylabel(r'$\mathrm{\Delta}p$,' + '\nPa', rotation=0, labelpad=13)
axes['ax4'].set_xlabel(r'$t_{env}$, ℃')

graph_ind += 1
axes['ax5'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax5'].plot(x, y5, label="Reynolds number for medium parameters")
axes['ax5'].set_ylabel("Re", rotation=0, labelpad=13)
axes['ax5'].set_xlabel(r'$t_{env}$, ℃')
axes['ax5'].ticklabel_format(axis='y', style='plain', useOffset=False)

graph_ind += 1
axes['ax6'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax6'].plot(x, y6, label="Hydraulic resistance coefficient \n for medium parameters")
axes['ax6'].set_ylabel(r"$\mathrm{\lambda}$", rotation=0, labelpad=13)
axes['ax6'].set_xlabel(r'$t_{env}$, ℃')
axes['ax6'].ticklabel_format(axis='y', style='plain', useOffset=False)
axes['ax6'].yaxis.set_ticks([0.011360, 0.011362, 0.011364])
axes['ax6'].yaxis.set_ticks(np.linspace(0.011358, 0.011368, num=6))

graph_ind += 1
axes['ax7'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax7'].plot(x, y7, label="Kinematic viscosity coefficient \n for medium parameters")
axes['ax7'].set_ylabel(r"$\mathrm{\nu}$" + "\n" + r"$\frac{m^2}{s}$", rotation=0, labelpad=13)
axes['ax7'].set_xlabel(r'$t_{env}$, ℃')

graph_ind += 1
axes['ax8'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax8'].plot(x, y8, label="Natural gas velocity \n for medium parameters")
axes['ax8'].set_ylabel("v, \n" + r"$\frac{m}{s}$", rotation=0, labelpad=13)
axes['ax8'].set_xlabel(r'$t_{env}$, ℃')

for key, ax in axes.items():
    ax.grid(True)
    ax.legend()

fig = plt.gcf()
cm = 1/2.54
fig.set_size_inches(30*cm, 40*cm)
plt.show()

