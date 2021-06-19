import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import FormatStrFormatter

from main_gas_pipeline.main_gas_pipeline import Pipeline
# from main_gas_pipeline import formula_old as formula
from main_gas_pipeline.constants import Constants
from pipe_object import pipe

# pipe.pressure_final = 4.5e6
# result = pipe.get_final_temperature_by_x(1e5)
# pipe.get_pressure_by_crd(1.5e5)
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
# rcParams['font.family'] = 'fantasy'
# rcParams['font.fantasy'] = 'Arial'
# rcParams["font.family"] = "Times New Roman"
rcParams["font.size"] = "12"

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

print(f"Mass flow, kg/s: {round(pipe.mass_flow, 1)}")
print(f"Cross sectional area, m2: {pipe.cross_sectional_area}")
print(f"Inner diameter of a pipe, m: {pipe.inner_diameter}")
print(f"Soil-air heat transfer coefficient, W/(m2*K): {pipe.soil_air_heat_transfer}")
print(f"Equivalent depth, m: {pipe.equivalent_depth}")
print(f"Pipe-soil heat transfer coefficient, W/m2*K: {pipe.pipe_soil_heat_transfer}")
print(f"Overall heat transfer coefficient, W/(m2*K): {pipe.heat_transfer_coefficient}")
print(f"Thermal resistance of isolation, (m2*K/W): {pipe.isolation_thermal_resistance}")
print(f"Natural gas density at standard temperature, kg/m3: {pipe.natural_gas.density_standard}")
print(f"Natural gas molar mass, kg/kmole: {pipe.natural_gas.molar_mass}")
print(f"Gas constant of natural gas, J/(kg*K): {pipe.natural_gas.gas_constant}")
print(f"Natural gas pseudocritical temperature (CH4 > 85%), K: {pipe.natural_gas.temperature_pseudocritical}")
print(f"Natural gas pseudocritical pressure (CH4 > 85%), MPa: {pipe.natural_gas.pressure_pseudocritical}")
print(f"Natural gas density relative to standard air density: {pipe.natural_gas.density_relative}")

x = [0]
y_pk = [pipe.pressure_initial/1e6]
y_tk = [pipe.temperature_initial]
y_tsr = [pipe.temperature_initial]
y_psr = [pipe.pressure_medium/1e6]
y_lambda = [pipe.hydraulic_resistance_coefficient]
y_Re = [pipe.reynolds]
y_V = [pipe.velocity]
y_Q = [pipe.volume_flow]
y_ro = [pipe.natural_gas.density]
y_Ppr = [pipe.natural_gas.pressure_reduced]
y_Tpr = [pipe.natural_gas.temperature_reduced]
y_Z = [pipe.natural_gas.compressibility_factor]
y_Cp = [pipe.natural_gas.specific_isobaric_heat_capacity]
y_Dj = [pipe.natural_gas.joile_tomson_factor]
y_mu = [pipe.natural_gas.viscosity_dynamic]
y_nu = [pipe.natural_gas.viscosity_kinematic]
y_soil_lambda = [pipe.soil_heat_conductivity]

for _x in range(0, int(1.5e5), 1000):
    if _x != 0:
        x.append(_x/1000)
        pipe.get_pressure_by_crd(1000)
        # Абсолютное давление по длине трубопровода
        y_pk.append(pipe.pressure_final/1e6)
        pipe.pressure_initial = pipe.pressure_final
        # Температура по длине трубопровода
        y_tk.append(pipe.temperature_final)
        pipe.temperature_initial = pipe.temperature_final
        # Средняя температура на каждом отрезке
        y_tsr.append(pipe.temperature_medium)
        # Средняя давление на каждом отрезке
        y_psr.append(pipe.pressure_medium/1e6)
        # Hydraulic resistant coefficient
        y_lambda.append(pipe.hydraulic_resistance_coefficient)
        # Reynolds number
        y_Re.append(pipe.reynolds)
        # Velocity
        y_V.append(pipe.velocity)
        # Volume flow
        y_Q.append(pipe.volume_flow)
        # Natural gas density, kg/m3
        y_ro.append(pipe.natural_gas.density)
        # Reduced pressure of the natural gas, dimensionless
        y_Ppr.append(pipe.natural_gas.pressure_reduced)
        # Reduced temperature of the natural gas, dimensionless
        y_Tpr.append(pipe.natural_gas.temperature_reduced)
        # Compressibility factor, dimensionless
        y_Z.append(pipe.natural_gas.compressibility_factor)
        # Isobar specific heat capacity Cp J/(kg*K)
        y_Cp.append(pipe.natural_gas.specific_isobaric_heat_capacity)
        # Joile-Tomson factor Di (K/MPa)
        y_Dj.append(pipe.natural_gas.joile_tomson_factor)
        # Dynamic viscosity of the natural gas, Pa*s
        y_mu.append(pipe.natural_gas.viscosity_dynamic)
        # Natural gas kinematic viscosity, m2/s
        y_nu.append(pipe.natural_gas.viscosity_kinematic)
        # Heat conductivity of a soil, W/(m2*K)
        y_soil_lambda.append(pipe.soil_heat_conductivity)

# fig = plt.figure()
# fig.patch.set_facecolor('xkcd:mint green')
# plt.plot(x, y_pk, label="Natural gas pressure")
fig = plt.figure()
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.96, top=0.98, wspace=0.26, hspace=0.305)
# fig, ax = plt.subplots()
# fig.suptitle('Vertically stacked subplots')

# График изменения абсолютного давления по длине трубопровода
rows = 5
cols = 3
axes = {}
graph_ind = 1
axes['ax1'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax1'].plot(x, y_pk, label="Natural gas pressure")
# axes['ax1'].plot(x, y_psr, label="Natural gas pressure medium")
axes['ax1'].set_ylabel('P, MPa')
axes['ax1'].set_xlabel('x, km')

graph_ind += 1
# График изменения температуры газа по длине трубопровода
axes['ax2'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax2'].plot(x, y_tk, label="Natural gas temperature")
# axes['ax2'].plot(x, y_tsr, label="Natural gas medium temperature")
axes['ax2'].set_ylabel('T, K')
axes['ax2'].set_xlabel('x, km')

graph_ind += 1
# Graph of hydraulic resistance coefficient depending the length of the pipe
axes['ax3'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax3'].plot(x, y_lambda, label="Hydraulic resistance coefficient")
axes['ax3'].set_ylabel(r'$\mathrm{\lambda}$')
axes['ax3'].set_xlabel('x, km')

graph_ind += 1
# Graph of Reynolds number depending the length of the pipe
axes['ax4'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax4'].plot(x, y_Re, label="Reynolds number")
axes['ax4'].set_ylabel('Re')
axes['ax4'].set_xlabel('x, km')

graph_ind += 1
# Graph of Reynolds number depending the length of the pipe
axes['ax5'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax5'].plot(x, y_V, label="Velocity of the natural gas")
axes['ax5'].set_ylabel(r"$V,$"+"\n"+r"$\frac{m}{s}$")
axes['ax5'].set_xlabel('x, km')

graph_ind += 1
# Graph of natural gas volume flow depending the length of the pipe
axes['ax6'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax6'].plot(x, y_V, label="Volume flow of the natural gas")
axes['ax6'].set_ylabel(r"$Q,$"+"\n"+r"$\frac{m^3}{hr}$", rotation=0, labelpad=13)
axes['ax6'].set_xlabel('x, km')

graph_ind += 1
# Graph of natural gas density depending the length of the pipe
axes['ax7'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax7'].plot(x, y_ro, label="Density of the natural gas")
axes['ax7'].set_ylabel(r"$\mathrm{\rho},$"+"\n"+r"$\frac{kg}{m^3}$", rotation=0, labelpad=13)
axes['ax7'].set_xlabel('x, km')

graph_ind += 1
# Graph of pressure reduced depending the length of the pipe
axes['ax8'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax8'].plot(x, y_Ppr, label="Pressure reduced of the natural gas")
axes['ax8'].set_ylabel(r"$P_{red}$", rotation=0, labelpad=13)
axes['ax8'].set_xlabel('x, km')

graph_ind += 1
# Graph of temperature reduced depending the length of the pipe
axes['ax9'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax9'].plot(x, y_Tpr, label="Temperature reduced of the natural gas")
axes['ax9'].set_ylabel(r"$T_{red}$", rotation=0, labelpad=13)
axes['ax9'].set_xlabel('x, km')

graph_ind += 1
# Graph of compressibility factor depending the length of the pipe
axes['ax10'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax10'].plot(x, y_Z, label="Compressibility factor of the natural gas")
axes['ax10'].set_ylabel(r"$Z$", rotation=0, labelpad=13)
axes['ax10'].set_xlabel('x, m')

graph_ind += 1
# Isobar specific heat capacity Cp J/(kg*K) depending the length of the pipe
axes['ax11'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax11'].plot(x, y_Cp, label="Isobar specific heat capacity of the natural gas")
axes['ax11'].set_ylabel(r"$C_p,$" +"\n"+r"$\frac{J}{kg \cdot K}$", rotation=0, labelpad=13)
axes['ax11'].set_xlabel('x, km')

graph_ind += 1
# Joile-Tomson factor Di (K/MPa) depending the length of the pipe
axes['ax12'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax12'].plot(x, y_Dj, label="Joile-Tomson factor")
axes['ax12'].set_ylabel(r"$D_i,$" +"\n"+r"$\frac{K}{MPa}$", rotation=0, labelpad=13)
axes['ax12'].set_xlabel('x, km')

graph_ind += 1
# Dynamic viscosity of the natural gas, Pa*s
axes['ax13'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax13'].plot(x, y_mu, label="Viscosity dynamic")
axes['ax13'].set_ylabel(r"$\mu,$" +"\n"+r"$Pa \cdot s$", rotation=0, labelpad=13)
axes['ax13'].set_xlabel('x, km')

graph_ind += 1
# Kinematic viscosity of the natural gas, m2*s
axes['ax14'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax14'].plot(x, y_nu, label="Viscosity kinematic")
axes['ax14'].set_ylabel(r"$\nu,$" +"\n"+r"$\frac{m^2}{s}$", rotation=0, labelpad=13)
axes['ax14'].set_xlabel('x, km')

graph_ind += 1
# Heat conductivity of a soil, W/(m2*K)
axes['ax15'] = fig.add_subplot(rows, cols, graph_ind)
axes['ax15'].plot(x, y_soil_lambda, label="Heat conductivity of a soil")
axes['ax15'].set_ylabel(r"$\mathrm{\lambda}_{soil}$," +"\n"+r"$\frac{W}{m^2 \cdot K}$", rotation=0, labelpad=13)
axes['ax15'].set_xlabel('x, km')

for ax in axes:
    axes[ax].grid(True)
    axes[ax].legend()


# ax.set_facecolor('xkcd:salmon')
# plt.xticks(np.arange(min(x), max(x) + 10, 20))
# axes = plt.gca()
# fig, ax = plt.subplots()
# ax.set_xticks([0.15, 0.68, 0.97])
# ax.set_yticks([0.2, 0.55, 0.76])
# axes.set_xlim([xmin,xmax])
# axes.set_ylim([3, 6.5])
# plt.locator_params(axis="y", nbins=5)
# plt.ylabel('P, Pa')
# plt.xlabel('x, m')
# plt.title(r'$\mathrm{\alpha > \beta}$')
# plt.show()
# plt.savefig('parameters.jpg', dpi=2300)
fig = plt.gcf()
cm = 1/2.54
fig.set_size_inches(45*cm, 40*cm)
# figure(figsize=())
# plt.savefig('parameters.jpg', dpi=700)
plt.show()
exit()


plt.plot(x, y_tk, label="Natural gas temperature")
plt.grid(True)
plt.legend()
plt.show()
# # plt.savefig('line_plot.svg')
1
# https://matplotlib.org/stable/tutorials/text/mathtext.html