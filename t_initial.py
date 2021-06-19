"""
Changing of natural gas comparison for different initial temperature
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

t_init_stack = [40, 35, 30, 25]  # natural gas initial temperature
for t0 in t_init_stack:
    pipe_variant = copy(pipe)
    pipe_variant.temperature_initial = t0+273
    pipe_variant.temperature_initial0 = t0+273
    pipes.append(pipe_variant)

for variant in pipes:
    x = []
    y_tk = []
    for _x in range(0, int(1.5e5), 1000):
        if _x == 0:
            x.append(0)
            y_tk.append(variant.temperature_initial - 273)
            continue
        x.append(_x / 1000)
        variant.get_pressure_by_crd(1000)
        # Абсолютное давление по длине трубопровода
        variant.pressure_initial = variant.pressure_final
        # Температура по длине трубопровода
        y_tk.append(variant.temperature_final - 273)
        variant.temperature_initial = variant.temperature_final
    plt.plot(x, y_tk, label=r"$t_{init}=" + str(variant.temperature_initial0 - 273) + "℃$")

plt.plot([0, 150e3/1000], [12, 12], label="Temperature of soil, "+r"$t_{soil}=12℃$")
plt.ylabel('t, ℃')
plt.xlabel('x, km')
plt.legend()
plt.grid(True)
fig = plt.gcf()
# fig.set_size_inches(8*cm, 7*cm)
# figure(figsize=())
# plt.savefig('t_init.jpg', dpi=500)
plt.show()
exit()
