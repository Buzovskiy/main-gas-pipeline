import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
from main_gas_pipeline.main_gas_pipeline import Pipeline
from main_gas_pipeline import formula

pipe = Pipeline(
    natural_gas_title='shebelinka'
)
pipe.pressure_initial = 6 * 10 ** 6  # p0
pipe.volume_flow_standard = 30 * 10 ** 6 / (24 * 60 * 60)  # Qk
pipe.equivalent_roughness = 0.03 * 10 ** -3  # k
pipe.inner_diameter = 1000 * 10 ** -3  # d
pipe.temperature_initial = 313  # T0
pipe.natural_gas_title = 'shebelinka'
pipe.temperature_medium = pipe.temperature_initial


# pipe.delta = 0.62
# pipe.temperature_critical = 190.55  # Tkr
# print(round(pipe.get_pressure_by_crd(70000)))

rcParams['font.family'] = 'fantasy'
rcParams['font.fantasy'] = 'Arial'

# pk = formula.pressure_final(pipe.pressure_initial, 5414930, pipe.pressure_critical, pipe.volume_flow_standard,
#                        pipe.temperature_initial, pipe.temperature_critical, pipe.inner_diameter, pipe.delta,
#                        pipe.equivalent_roughness, 30000)
#
# pipe.pressure_medium = 5414930
# pk = pipe.get_final_pressure_by_x(30000)
# print(pk)

x = []
y = []
for _x in range(0, 51000, 1000):
    if _x == 0:
        x.append(0)
        y.append(pipe.pressure_initial)
    else:
        x.append(_x)
        pk = pipe.get_pressure_by_crd(1000)
        y.append(round(pk))
        pipe.pressure_initial = pk
        print(pk)
plt.plot(x, y, label="b")
plt.ylabel('P, Pa')
plt.xlabel('x, m')
plt.grid(True)
plt.title(r'$\mathrm{\alpha > \beta}$')
plt.legend()
plt.show()
# # plt.savefig('line_plot.svg')

# https://matplotlib.org/stable/tutorials/text/mathtext.html