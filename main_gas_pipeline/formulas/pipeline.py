import math
# from .constants import Constants as const


def cross_sectional_area(d):
    """
    :param d: Inner diameter of a pipe, m
    :return: Cross sectional area, m2
    """
    return math.pi * d**2 / 4


def hydraulic_resistance_coefficient(Eg, Re, ke, d):
    """
    :param Eg: Coefficient of hydraulic efficiency. If no data: Eg=0.95 for pipelines with scraper system; Eg=0.92 for
    pipelines without scrapper system. Dimensionless
    :param Re: Reynolds number. Dimensionless
    :param ke: equivalent pipe roughness, m
    :param d: pipe inner diameter, m
    :returns: Hydraulic resistance coefficient, dimensionless
    """
    return (1.05/Eg**2) * 0.067 * (158/Re + 2*ke/d)**0.2


def reynolds(v, d, nu):
    """
    :param v: Velocity of the natural gas, m/s
    :param d: Pipe inner diameter, m
    :param nu: Kinematic viscosity, m2/s
    :return: Reynolds number, dimensionless
    """
    return v*d/nu


def velocity(Q, S):
    """
    :param Q: Volume flow for thermodynamic conditions in pipe, m3/s
    :param S: Сross-sectional area of a pipe, m2
    :return: Velocity of the natural gas, m/s
    """
    return Q/S


def volume_flow(p, G, R, T, Z):
    """
    :param p: Absolute pressure, Pa
    :param G: Mass flow, kg/s
    :param R: Gas constant, J/(kg*K)
    :param Z: Compressibility factor
    :return: Volume flow of the natural gas, m3/s
    """
    return Z * G * R * T / p


def inner_diameter(D, delta):
    """
    :param D: Outer diameter of a pipe, m
    :param delta: Wall thickness, m
    :return: Inner diameter of a pipe, m
    """
    return D - 2 * delta


def pressure_final(p0, M, lambda_res, Tsr, Z, R, d, x):
    """
    :param p0: Absolute natural gas pressure at the beginning of the pipe, Pa
    :param M: Mass flow of the natural gas, kg/c
    :param lambda_res: Hydraulic resistance coefficient, dimensionless
    :param Tsr: Medium temperature of natural gas, K
    :param Z: Compressibility factor of natural gas at medium parameters
    :param R: Gas constant of natural gas, J/(kg*K)
    :param d: Inner diameter of pipe, m
    :param x: Length of pipe section, m
    :return: Final absolute pressure pk, Pascal
    """
    return math.sqrt((p0 ** 2) - (16 * (M ** 2) * lambda_res * Z * R * Tsr * x) / (math.pi**2 * d**5))


def pressure_medium(p0, pk):
    """Medium pressure psr
    :param p0: Absolute pressure at the beginning of the pipe section, Pa
    :param pk: Absolute pressure at the end of the pipe section, Pa
    :return: Medium absolute pressure, Pa
    """
    return (2 / 3) * (p0 + (pk ** 2) / (p0 + pk))


def temperature_final(x, Ksr, d, M, Cp, Tgr, T0, Ddj, p0, pk, psr):
    """
    :param x: Length of pipe section, m
    :param Ksr: Medium heat transfer coefficient at pipe section, W/(m2*K)
    :param d: Inner diameter of pipe, m
    :param M: Mass flow of the natural gas, kg/s
    :param Cp: Isobaric heat capasity of natural gas, J/(kg*K)
    :param Tgr: Temperature of the soil, K
    :param T0: Initial temperature of natural gas, K
    :param Ddj: Joile-Tomson coefficient, K/MPa
    :param p0: Initial absolute pressure of natural gas at pipe section, Pa
    :param pk: Final absolute pressure of natural gas at pipe section, Pa
    :param psr: Medium absolute pressure of natural gas at pipe section, Pa
    :return: Final temperature of gas at pipe section, K
    """
    a = (Ksr * math.pi * d) / (M * Cp)
    return Tgr + (T0 - Tgr) * math.exp(-a * x) - Ddj*1e-6 * ((p0**2 - pk**2)/(2 * a * x * psr)) * (1 - math.exp(-a * x))


def temperature_medium(x, Ksr, d, M, Cp, Tgr, T0, Ddj, p0, pk, psr):
    """Medium temperature of gas, K
    :param x: Length of pipe section, m
    :param Ksr: Medium heat transfer coefficient at pipe section, W/(m2*K)
    :param d: Inner diameter of pipe, m
    :param M: Mass flow of the natural gas, kg/s
    :param Cp: Isobaric heat capasity of natural gas, J/(kg*K)
    :param Tgr: Temperature of the soil, K
    :param T0: Initial temperature of natural gas, K
    :param Ddj: Joile-Tomson coefficient, K/MPa
    :param p0: Initial absolute pressure of natural gas at pipe section, Pa
    :param pk: Final absolute pressure of natural gas at pipe section, Pa
    :param psr: Medium absolute pressure of natural gas at pipe section, Pa
    :return: Medium temperature of natural gas at pipe section, K
    """
    a = (Ksr * math.pi * d) / (M * Cp)
    return Tgr + (T0 - Tgr) * (1 - math.exp(-a*x))/(a*x) - Ddj*1e-6*((p0**2 - pk**2)/(2 * a * x * psr)) * (1 - (1 - math.exp(-a*x))/(a*x))


def heat_transfer_coefficient(Ris, alpha_soil):
    """
    :param Ris: Thermal resistance of pipeline isolation, m*K/W
    :param alpha_soil: pipe-soil heat transfer coefficient, W/(m2*K)
    :return: Overall heat transfer coefficient, W/(m2*K)
    """
    return (Ris + 1/alpha_soil)**-1


def pipe_soil_heat_transfer(lambda_soil, D, h0e):
    """
    :param lambda_soil: Heat conductivity of a soil, W/(m*K)
    :param D: Outer diameter of the pipe, m
    :param h0e: Equivalent depth of the gas pipeline axis, m
    :return: Pipe-soil heat transfer coefficient, W/m2*K
    """
    return (lambda_soil / D) * (0.65 + (D/h0e)**2)


def equivalent_depth(h0, lambda_soil, alpha_air, delta_snow, lambda_snow):
    """
    :param h0: Depth of the gas pipeline axis, m
    :param lambda_soil: Heat conductivity coefficient of soil, W/(m*K)
    :param alpha_air: Soil-air heat transfer coefficient, W/(m2*K)
    :param delta_snow: Thickness of snow surface, m
    :param lambda_snow: Heat conductivity coefficient of snow, W/(m*K)
    :return: equivalent depth, m
    """
    return h0 + lambda_soil * (1/alpha_air + delta_snow/lambda_snow)


def soil_air_heat_transfer(Vw):
    """
    :param Vw: Velocity of the wind, m/s
    :return: Soil-air heat transfer coefficient, W/(m2*K)
    """
    return 6.2 + 4.2*Vw


def isolation_thermal_resistance(D, lambda_is, delta):
    """
    :param D: Outer diameter of pipeline or diameter of the last layer if pipeline has many
    layers of isolation, m
    :param lambda_is: heat conductivity of isolation, W/(m*K)
    :param delta: Thickness of isolation, m
    :return: Thermal resistance of isolation, (m2*K/W)
    """
    Dis = D + 2*delta
    return D/(2*lambda_is) * math.log(Dis/D)


def soil_heat_conductivity(w, T, ro, soil_type):
    """
    Heat conductivity of a soil, W/(m2*K)
    :param w: humidity, %
    :param T: temperature, K
    :param ro: density of a soil, kg/m3
    :param soil_type: (str) type of a soil
    :return: heat conductivity of a soil, W/(m2*K)
    """
    ro = ro / 1000
    return {
        'sand': 10**((-134.2 + 23.89*w - 2.389*T + 442.98*ro - 0.276*w**2)*1e-3),
        'loam': 10**((-711.8 + 8.25*w + 2.48*T - 17.2*ro)*1e-3),
        'mixed_soil': 10**((-920.27 + 13.9 * w + 3.26 * T + 18.6 * ro - 0.36 * w**2)*1e-3),
    }[soil_type.lower()]
