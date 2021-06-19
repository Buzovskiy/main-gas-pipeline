"""
Графики для расчета изменения параметров газа по длине трубопровода
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter

from copy import copy

from pipe_object import pipe

rcParams["font.size"] = "12"

fig = plt.figure()
plt.subplots_adjust(left=0.136, bottom=0.133, right=0.96, top=0.943, wspace=0.26, hspace=0.305)
rows = 2
cols = 1
axes = {}
graph_ind = 1
axes['ax1'] = fig.add_subplot(rows, cols, graph_ind)
graph_ind += 1
axes['ax2'] = fig.add_subplot(rows, cols, graph_ind)

max_pipe_length = 150e3  # длина трубопровода, м

pipes = []
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
        # Абсолютное давление по длине трубопровода
        variant.pressure_initial = variant.pressure_final
        # Температура по длине трубопровода
        y_tk.append(variant.temperature_final)
        variant.temperature_initial = variant.temperature_final
        y_pk.append(variant.pressure_final)
    axes['ax1'].plot(x, np.array(y_tk) - 273, label=r"$t_{0}=" + str(variant.temperature_soil - 273) + "℃$")
    axes['ax2'].plot(x, y_pk, label=r"$t_{0}=" + str(variant.temperature_soil - 273) + "℃$")

axes['ax1'].plot([0, max_pipe_length/1000], [12, 12], label="Temperature of soil, "+r"$t_{soil}=12℃$")
axes['ax1'].set_ylabel('t, ℃', rotation=0, labelpad=13)
axes['ax1'].set_xlabel('x, km')
axes['ax1'].set_title(label="График изменения температуры газа по длине \n при вариации температуры окружающей среды")

axes['ax2'].set_ylabel(r'$P$' + "\nPa", rotation=0, labelpad=13)
axes['ax2'].set_xlabel('x, km')
axes['ax2'].set_title(label="График изменения абсолютного давления газа по длине \n"
                            " при вариации температуры окружающей среды")

# graph_ind += 1
# # График зависимости средней температуры газа на всем участке от температуры окружающей среды
# axes['ax2'] = fig.add_subplot(rows, cols, graph_ind)
#
# x_t_medium = []  # Список температур грунта
# y_t_medium = []  # Список средних температур газа
#
# for variant in pipes:
#     variant.temperature_initial = 273 + 40
#     print(f"t_initial: 40")
#     print(f"t_medium: {variant.get_temperature_medium(max_pipe_length) - 273}")
#     print(f"t_medium: {variant.temperature_medium - 273}")
#     print(f"t_final: {variant.temperature_final - 273}")
#     print("--------------------------------------------------")



# axes['ax2'].plot(x, y_tk, label="Natural gas temperature")
# # axes['ax2'].plot(x, y_tsr, label="Natural gas medium temperature")
# axes['ax2'].set_ylabel('T, K')
# axes['ax2'].set_xlabel('x, km')
#
#
for key, ax in axes.items():
    ax.grid(True)
    ax.legend()

cm = 1/2.54
fig.set_size_inches(20*cm, 25*cm)

plt.savefig('t_env.jpg', dpi=500)
plt.show()
exit()

#
