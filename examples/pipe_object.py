import main_gas_pipeline as mgp


pipe = mgp.Pipeline(
    pressure_initial=6e6,  # p0
    volume_flow_standard=30e6 / (24 * 60 * 60),  # Qk
    equivalent_roughness=0.03e-3,  # k
    outer_diameter=1020e-3,  # d
    wall_thickness=10e-3,
    temperature_initial=313,  # T0
    hydraulic_efficiency=0.95,
    wind_velocity=2,
    pipeline_depth=1.5,
    isolation_heat_conductivity=0.1,
    isolation_thickness=10e-3,
    snow_thickness=0,
    snow_heat_conductivity=0.1,
    temperature_soil=12+273,
    natural_gas_title='shebelinka',
    soil_type='mixed_soil',
    soil_humidity=10,
    soil_density=1500
)

print(pipe)
