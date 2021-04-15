import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter

from copy import copy

from pipe_object import pipe


rcParams["font.size"] = "12"

pipes = []
for t_gr in [25, 12, 4, 0]:
    pipe_var = copy(pipe)
    pipe_var.temperature_soil = t_gr+273
    pipes.append(pipe_var)

for variant in pipes:
    x = []
    y_tk = []
    for _x in range(0, int(1.5e5), 1000):
        if _x == 0:
            x.append(0)
            y_tk.append(variant.temperature_initial)
            continue
        x.append(_x / 1000)
        variant.get_pressure_by_crd(1000)
        # Абсолютное давление по длине трубопровода
        variant.pressure_initial = variant.pressure_final
        # Температура по длине трубопровода
        y_tk.append(variant.temperature_final)
        variant.temperature_initial = variant.temperature_final
    plt.plot(x, np.array(y_tk) - 273, label=r"$t_{0}=" + str(variant.temperature_soil - 273) + "℃$")

plt.plot([0, 150e3/1000], [12, 12], label="Temperature of soil, "+r"$t_{soil}=12℃$")
plt.ylabel('t, ℃')
plt.xlabel('x, km')
plt.legend()
plt.grid(True)
plt.savefig('t_env.jpg', dpi=500)
# plt.show()
exit()