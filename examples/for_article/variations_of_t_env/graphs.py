"""
Changing the parameters of natural gas along the length of the gas pipeline.
Calculations with variations in ambient temperature.
File graph.py - Fig. 3
"""
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.ticker as ticker

from copy import copy

from examples.for_article.pipe_object import pipe


max_pipe_length = 150e3  # pipeline length, m

pipes = []  # list of pipe class instances with different soil temperatures
t_gas_func_x = {}  # a list of approximating t(l) functions
t_gr_list = [25, 12, 4, 0]
for t_gr in t_gr_list:
    pipe_var = copy(pipe)
    pipe_var.temperature_soil = t_gr+273
    pipes.append(pipe_var)

for variant in pipes:
    x = []
    y_tk = []
    y_pk = []
    for _x in range(0, int(max_pipe_length), 1000):
        if _x == 0:
            x.append(0)
            y_tk.append(variant.temperature_initial)
            y_pk.append(variant.pressure_final)
            continue
        x.append(_x / 1000)
        variant.get_pressure_by_crd(1000)
        # Absolute pressure along the pipe length
        variant.pressure_initial = variant.pressure_final
        # Gas temperature along the pipe length
        y_tk.append(variant.temperature_final)
        variant.temperature_initial = variant.temperature_final
        y_pk.append(variant.pressure_final)
    z = np.polyfit(x, y_tk, 4)
    t_gas_func_x[variant.temperature_soil-273] = np.poly1d(z)

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["mathtext.fontset"] = "stix"
rcParams["font.size"] = "14"

fig, ax = plt.subplots()
data_legend = {}
for t_gr in t_gr_list:
    line, = ax.plot(
        [_ / 1000 for _ in range(0, int(max_pipe_length), 1000)],
        [t_gas_func_x[t_gr](_ / 1000)-273 for _ in range(0, int(max_pipe_length), 1000)])
if len(data_legend.values()):
    ax.legend(data_legend.values(), data_legend.keys())

ax.plot(
    [0, max_pipe_length / 1000],
    [pipe.temperature_soil-273, pipe.temperature_soil-273],
    ls='--', dashes=(10, 10), color='black', lw=0.6
)
ax.set_ylabel("t,"+"\n"+"℃", rotation=0, labelpad=33, ha='left', va='center')
ax.set_xlabel("x, km")
ax.set_xlim(0)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))

xann = max_pipe_length*0.9 / 1000
counterann = 0
annotates_list = {}
for t_gr in t_gr_list:
    counterann += 1
    xytext = (xann*1.13, t_gas_func_x[t_gr](xann*1.1)-273+2) if counterann == 4 else \
        (xann*1.13, t_gas_func_x[t_gr](xann*1.1)-273+3)
    ax.annotate(
        counterann,
        xy=(xann, t_gas_func_x[t_gr](xann) - 273),
        xytext=xytext,
        arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6)
    )

a4x = fsolve(t_gas_func_x[0] - pipe.temperature_soil, 0)
a4y = pipe.temperature_soil-273
ax.annotate(r"$\mathrm{a_{4}}$", xy=(a4x, a4y), xytext=(a4x*0.8, a4y+1),
            arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6),
            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round', pad=0))
ax.annotate(r"$\mathrm{t_{soil}}$", xy=(0, a4y), xytext=(6, a4y+1),
            arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6),
            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round', pad=0))

plt.subplots_adjust(left=0.152, bottom=0.19, right=0.971, top=0.98, wspace=0.26, hspace=0.305)
ax.grid(True)
cm = 1/2.54
fig.set_size_inches(15*cm, 8*cm)
plt.savefig('fig.3.jpg', dpi=1000)
plt.show()
