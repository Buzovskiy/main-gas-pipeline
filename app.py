import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
from main_gas_pipeline.main_gas_pipeline import Pipeline
from main_gas_pipeline import formula_old as formula
from main_gas_pipeline.constants import Constants

pipe = Pipeline(
    natural_gas_title='shebelinka',
    pressure_initial=6 * 10 ** 6,  # p0
    volume_flow_standard=30 * 10 ** 6 / (24 * 60 * 60),  # Qk
    equivalent_roughness=0.03 * 10 ** -3,  # k
    inner_diameter=1000 * 10 ** -3,  # d
    temperature_initial=313,  # T0
    temperature_soil=12+273,
)


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
# exit(pipe.get_pressure_by_crd(30000))
print(pipe.get_pressure_by_crd(30000))
exit(pipe.mass_flow)


# temperature = lambda x: formula.temperature_final(x, Ksr=1.75, d=1.2, M=0.62*Constants.density_standard_air*32e6/(24*60*60), Cp=2500, Tgr=273, T0=303, Ddj=0.3, p0=6, pk=3.5)
# for t in [x*1e3 for x in [20, 40, 60, 80, 100, 120, 140]]:
#     print(temperature(t)-273)

#exit(formula.temperature_medium(20e3, Ksr=1.75, d=1.2, M=0.62*Constants.density_standard_air*32e6/(24*60*60), Cp=2500, Tgr=273, T0=303, Ddj=0.3, p0=6, pk=3.5)-273)



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