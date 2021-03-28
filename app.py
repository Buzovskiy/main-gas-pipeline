import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
from main_gas_pipeline.main_gas_pipeline import Pipeline
# from main_gas_pipeline import formula_old as formula
from main_gas_pipeline.constants import Constants

pipe = Pipeline(
    pressure_initial=6e6,  # p0
    volume_flow_standard=30e6 / (24 * 60 * 60),  # Qk
    equivalent_roughness=0.03e-3,  # k
    outer_diameter=1020e-3,  # d
    wall_thickness=10e-3,
    temperature_initial=313,  # T0
    hydraulic_efficiency=0.95,
    wind_velocity=2,
    pipeline_depth=1.5,
    soil_heat_conductivity=1,
    isolation_heat_conductivity=0.1,
    isolation_thickness=10e-3,
    snow_thickness=0,
    snow_heat_conductivity=0.1,
    temperature_soil=12+273,
    natural_gas_title='shebelinka',
)

# pipe.pressure_final = 4.5e6
# result = pipe.get_final_temperature_by_x(1e5)
pipe.get_pressure_by_crd(1.3e5)
# print(f"pk = {result}")
# print(f"tk = {pipe.temperature_final}")
# pipe.pressure_initial = pipe.pressure_final
# pipe.temperature_initial = pipe.temperature_final
# result = pipe.get_pressure_by_crd(1e3)
# print(f"pk = {result}")
# print(f"tk = {pipe.temperature_final}")
# exit(result)

# print(round(pipe.get_final_pressure_by_x(70000)))
# pipe.temperature_medium = 280
# print(pipe.get_final_pressure_by_x(70000))
# exit()
rcParams['font.family'] = 'fantasy'
rcParams['font.fantasy'] = 'Arial'

# pk = formula.pressure_final(pipe.pressure_initial, 5414930, pipe.pressure_critical, pipe.volume_flow_standard,
#                        pipe.temperature_initial, pipe.temperature_critical, pipe.inner_diameter, pipe.delta,
#                        pipe.equivalent_roughness, 30000)
#
# pipe.pressure_medium = 5414930
# pk = pipe.get_final_pressure_by_x(30000)
# print(pk)
# exit(pipe.get_pressure_by_crd(100000))
# print(pipe.get_pressure_by_crd(30000))
# exit(pipe.mass_flow)


# temperature = lambda x: formula.temperature_final(x, Ksr=1.75, d=1.2, M=0.62*Constants.density_standard_air*32e6/(24*60*60), Cp=2500, Tgr=273, T0=303, Ddj=0.3, p0=6, pk=3.5)
# for t in [x*1e3 for x in [20, 40, 60, 80, 100, 120, 140]]:
#     print(temperature(t)-273)

#exit(formula.temperature_medium(20e3, Ksr=1.75, d=1.2, M=0.62*Constants.density_standard_air*32e6/(24*60*60), Cp=2500, Tgr=273, T0=303, Ddj=0.3, p0=6, pk=3.5)-273)



x = []
y_pk = []
y_tk = []
for _x in range(0, int(1.3e5), 1000):
    if _x == 0:
        x.append(0)
        y_pk.append(pipe.pressure_initial)
        y_tk.append(pipe.temperature_initial)
    else:
        x.append(_x)
        pipe.get_pressure_by_crd(1000)
        y_pk.append(round(pipe.pressure_final))
        pipe.pressure_initial = pipe.pressure_final
        # print(f't0 = {pipe.temperature_initial}')
        # print(f'tk = {pipe.temperature_final}')
        y_tk.append(pipe.temperature_final)
        pipe.temperature_initial = pipe.temperature_final
        # print(f"pk = {pipe.pressure_final}")
plt.plot(x, y_pk, label="Natural gas pressure")
plt.ylabel('P, Pa')
plt.xlabel('x, m')
plt.grid(True)
plt.title(r'$\mathrm{\alpha > \beta}$')
plt.legend()
plt.show()


plt.plot(x, y_tk, label="Natural gas temperature")
plt.grid(True)
plt.legend()
plt.show()
# # plt.savefig('line_plot.svg')
1
# https://matplotlib.org/stable/tutorials/text/mathtext.html