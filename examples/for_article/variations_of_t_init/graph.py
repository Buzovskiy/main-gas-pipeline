"""
Changing of natural gas comparison for different initial temperature
The graph of the gas temperature change along the length of the gas pipeline with a variation of the initial gas
temperature t_init.
Fig. 4
"""
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams

from copy import copy

from examples.for_article.pipe_object import pipe

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["mathtext.fontset"] = "stix"
rcParams["font.size"] = "14"
cm = 1/2.54

pipes = []
t_gas_func_x = {}  # a list of functions approximating t(l)

t_init_stack = [40, 35, 27, 19]  # natural gas initial temperature
for t0 in t_init_stack:
    pipe_variant = copy(pipe)
    pipe_variant.temperature_initial = t0+273
    pipe_variant.temperature_initial0 = t0+273
    pipes.append(pipe_variant)

max_pipe_length = int(150e3)  # length of pipeline
step = 1000

for variant in pipes:
    x = []
    y_tk = []
    for _x in range(0, max_pipe_length+step, step):
        if _x == 0:
            x.append(0)
            y_tk.append(variant.temperature_initial)
            continue
        x.append(_x / 1000)
        variant.get_pressure_by_crd(step)
        # Absolute pressure along the length of pipeline
        variant.pressure_initial = variant.pressure_final
        # Final temperature along the length of pipeline
        y_tk.append(variant.temperature_final)
        variant.temperature_initial = variant.temperature_final
    z = np.polyfit(x, y_tk, 4)
    t_gas_func_x[variant.temperature_initial0-273] = np.poly1d(z)

fig, ax = plt.subplots()
data_legend = {}

for t_init in t_init_stack:
    line, = ax.plot(
        [_ / 1000 for _ in range(0, int(max_pipe_length)+step, step)],
        [t_gas_func_x[t_init](_ / 1000)-273 for _ in range(0, int(max_pipe_length)+step, step)])

if len(data_legend.values()):
    ax.legend(data_legend.values(), data_legend.keys())

ax.plot(
    [0, max_pipe_length / 1000],
    [pipe.temperature_soil-273, pipe.temperature_soil-273],
    ls='--', dashes=(12, 10), color='black', lw=0.6
)

ax.set_ylabel("t,"+"\n"+"℃", rotation=0, labelpad=33, ha='left', va='center')
ax.set_xlabel("x, km")
ax.set_xlim(0)
ax.set_ylim(5)
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))

xann = max_pipe_length*0.2 / 1000
counterann = 0
annotates_list = {}
for t_init in t_init_stack:
    counterann += 1
    xytext = (xann*1.13, t_gas_func_x[t_init](xann*1.1)-273+3) if counterann != 2 else \
        (xann * 1.13, t_gas_func_x[t_init](xann * 1.1) - 273 + 1)
    ax.annotate(
        counterann,
        xy=(xann, t_gas_func_x[t_init](xann) - 273),
        xytext=xytext,
        arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6),
        bbox=dict(facecolor='white', edgecolor='none', boxstyle='round', pad=0.2)
    )

a4x = fsolve(t_gas_func_x[19] - pipe.temperature_soil, 0)
a4y = pipe.temperature_soil-273
ax.annotate(r"$\mathrm{a}$", xy=(a4x, a4y), xytext=(a4x*0.9, a4y-2),
            arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6),
            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round', pad=0))
ax.annotate(r"$\mathrm{t_{soil}}$", xy=(0, a4y), xytext=(6, a4y+1),
            arrowprops=dict(arrowstyle='-', ls='-', shrinkA=0, shrinkB=0, lw=0.6),
            bbox=dict(facecolor='white', edgecolor='none', boxstyle='round', pad=0))

plt.subplots_adjust(left=0.152, bottom=0.155, right=0.971, top=0.98, wspace=0.26, hspace=0.305)
ax.grid(True)
cm = 1/2.54
fig.set_size_inches(15*cm, 10*cm)
plt.savefig('fig.4.jpg', dpi=1000)
plt.show()
