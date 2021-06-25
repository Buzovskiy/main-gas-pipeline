from pipe_object import pipe


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