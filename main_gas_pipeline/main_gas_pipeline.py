from .natural_gases import NaturalGas
from .formulas import pipeline as f_pipeline


class Pipeline:

    def __init__(
            self,
            pressure_initial,
            volume_flow_standard,
            equivalent_roughness,
            outer_diameter,
            wall_thickness,
            temperature_initial,
            hydraulic_efficiency,
            wind_velocity,
            pipeline_depth,
            soil_heat_conductivity,
            isolation_heat_conductivity,
            isolation_thickness,
            snow_thickness,
            snow_heat_conductivity,
            temperature_soil,
            natural_gas_title='shebelinka'
    ):

        self.pressure_initial = pressure_initial
        self.volume_flow_standard = volume_flow_standard
        self.equivalent_roughness = equivalent_roughness
        self.outer_diameter = outer_diameter
        self.wall_thickness = wall_thickness
        self.temperature_initial = temperature_initial
        self.hydraulic_efficiency = hydraulic_efficiency
        self.wind_velocity = wind_velocity
        self.pipeline_depth = pipeline_depth
        self.soil_heat_conductivity = soil_heat_conductivity
        self.isolation_heat_conductivity = isolation_heat_conductivity
        self.isolation_thickness = isolation_thickness
        self.snow_thickness = snow_thickness
        self.snow_heat_conductivity = snow_heat_conductivity
        self.temperature_soil = temperature_soil

        self._pressure_medium = pressure_initial
        self._temperature_medium = temperature_initial
        # # Задаем природный газ
        self.natural_gas = NaturalGas(natural_gas_title)
        self.natural_gas.temperature = self.temperature_medium
        self.natural_gas.pressure = self.pressure_medium

        self.pressure_final = None
        self.temperature_final = None

    @property
    def temperature_medium(self):
        return self._temperature_medium

    @temperature_medium.setter
    def temperature_medium(self, value):
        self._temperature_medium = value
        self.natural_gas.temperature = value

    @property
    def pressure_medium(self):
        return self._pressure_medium

    @pressure_medium.setter
    def pressure_medium(self, value):
        self._pressure_medium = value
        self.natural_gas.pressure = value

    def get_pressure_by_crd(self, x):
        psr_calc = self.pressure_initial
        tsr_calc = self.temperature_initial
        pk = 0
        inaccuracy_p = 1
        inaccuracy_t = 1e-4
        while inaccuracy_p > 0.001 or inaccuracy_t > 0.001:
            self.pressure_medium = psr_calc
            self.temperature_medium = tsr_calc
            # print(self.pressure_initial)
            # self.natural_gas = NaturalGas(self.natural_gas_title, self.temperature_medium, self.pressure_medium)
            # self.natural_gas.temperature = self.temperature_medium
            # self.natural_gas.pressure = self.pressure_medium
            pk = self.get_final_pressure_by_x(x)
            psr_calc = f_pipeline.pressure_medium(self.pressure_initial, pk)
            inaccuracy_p = abs(self.pressure_medium - psr_calc)
            self.pressure_final = pk
            tsr_calc = self.get_temperature_medium(x)
            inaccuracy_t = abs(self.temperature_medium - tsr_calc)

        self.temperature_final = self.get_final_temperature_by_x(x)

        return pk

    def get_final_pressure_by_x(self, x):
        return f_pipeline.pressure_final(
            x=x,
            p0=self.pressure_initial,
            M=self.mass_flow,
            lambda_res=self.hydraulic_resistance_coefficient,
            Tsr=self.temperature_medium,
            Z=self.natural_gas.compressibility_factor,
            R=self.natural_gas.gas_constant,
            d=self.inner_diameter
        )

    def get_final_temperature_by_x(self, x):
        """
        :param x: Pipeline length, m
        :return: Temperature of natural gas at the end of the pipeline, K
        """
        return f_pipeline.temperature_final(
            x=x,
            Ksr=self.heat_transfer_coefficient,
            d=self.inner_diameter,
            M=self.mass_flow,
            Cp=self.natural_gas.specific_isobaric_heat_capacity,
            Tgr=self.temperature_soil,
            T0=self.temperature_initial,
            Ddj=self.natural_gas.joile_tomson_factor,
            p0=self.pressure_initial,
            pk=self.pressure_final,
            psr=self.pressure_medium,
        )

    def get_temperature_medium(self, x):
        return f_pipeline.temperature_medium(
            x=x,
            Ksr=self.heat_transfer_coefficient,
            d=self.inner_diameter,
            M=self.mass_flow,
            Cp=self.natural_gas.specific_isobaric_heat_capacity,
            Tgr=self.temperature_soil,
            T0=self.temperature_initial,
            Ddj=self.natural_gas.joile_tomson_factor,
            p0=self.pressure_initial,
            pk=self.pressure_final,
            psr=self.pressure_medium,
        )

    @property
    def mass_flow(self):
        """:returns: Mass flow of the natural gas, kg/s"""
        return self.volume_flow_standard * self.natural_gas.density_standard

    @property
    def hydraulic_resistance_coefficient(self):
        """:returns: Hydraulic resistance coefficient, dimensionless"""
        return f_pipeline.hydraulic_resistance_coefficient(
            Eg=self.hydraulic_efficiency,
            Re=self.reynolds,
            ke=self.equivalent_roughness,
            d=self.inner_diameter
        )

    @property
    def reynolds(self):
        """:returns: Reynolds number, dimensionless"""
        return f_pipeline.reynolds(
            v=self.velocity,
            d=self.inner_diameter,
            nu=self.natural_gas.viscosity_kinematic
        )

    @property
    def velocity(self):
        """:returns: Velocity of the natural gas, m/s"""
        return f_pipeline.velocity(
            Q=self.volume_flow,
            S=self.cross_sectional_area
        )


    @property
    def volume_flow(self):
        """:returns: Volume flow of the natural gas, m3/s"""
        return f_pipeline.volume_flow(
            self.pressure_medium,
            self.mass_flow,
            self.natural_gas.gas_constant,
            self.temperature_medium,
            self.natural_gas.compressibility_factor
        )

    @property
    def cross_sectional_area(self):
        """:returns: Cross sectional area, m2"""
        return f_pipeline.cross_sectional_area(self.inner_diameter)

    @property
    def inner_diameter(self):
        """:return: Inner diameter of a pipe, m"""
        return f_pipeline.inner_diameter(
            self.outer_diameter,
            self.wall_thickness
        )

    @property
    def soil_air_heat_transfer(self):
        """:return: Soil-air heat transfer coefficient, W/(m2*K)"""
        return f_pipeline.soil_air_heat_transfer(self.wind_velocity)

    @property
    def equivalent_depth(self):
        """:return: Equivalent depth, m"""
        return f_pipeline.equivalent_depth(
            self.pipeline_depth,
            self.soil_heat_conductivity,
            self.soil_air_heat_transfer,
            self.snow_thickness,
            self.snow_heat_conductivity,
        )

    @property
    def pipe_soil_heat_transfer(self):
        """:return: Pipe-soil heat transfer coefficient, W/m2*K"""
        return f_pipeline.pipe_soil_heat_transfer(
            self.soil_heat_conductivity,
            self.outer_diameter,
            self.equivalent_depth
        )

    @property
    def heat_transfer_coefficient(self):
        """:return: Overall heat transfer coefficient, W/(m2*K)"""
        return f_pipeline.heat_transfer_coefficient(
            self.isolation_thermal_resistance,
            self.pipe_soil_heat_transfer
        )

    @property
    def isolation_thermal_resistance(self):
        """:return: Thermal resistance of isolation, (m2*K/W)"""
        return f_pipeline.isolation_thermal_resistance(
            self.outer_diameter,
            self.isolation_heat_conductivity,
            self.isolation_thickness,
        )







