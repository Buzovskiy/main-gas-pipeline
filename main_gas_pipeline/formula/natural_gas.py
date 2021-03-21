def density_standard(components):
    """
    Natural gas density at standard temperature, kg/m3
    :param components: (list)  List of gas components. Each item is an object of class GasComponent
    :return: (float) The density of natural gas an standard parameters, kg/m3
    """
    return sum([component.density_standard * component.volume_percentage * 0.01 for component in components])


def molar_mass(components):
    """
    Natural gas molar mass, kg/kmole
    :param components: (list) The list of gas components. Each item is an object of class GasComponent
    :return: (float) Natural gas molar mass, kg/kmole
    """
    return sum([component.molar_mass * component.volume_percentage * 0.01 for component in components])


def gas_constant(R, mu):
    """
    Gas constant of natural gas, J/(kg*K)
    :param R: (float) Universal gas constant, J/(kmole*K)
    :param mu: (float) Molar mass of natural gas, kg/kmole
    :return: (float) Gas constant of natural gas, J/(kg*K)
    """
    return R / mu


def density(p, Z, R, T):
    """
    :param p: Absolute pressure of the natural gas, Pa
    :param Z: Compressibility factor of the natural gas, dimensionless
    :param R: Gas constant of the natural gas, J/(kg*K)
    :param T: Temperature of the natural gas, K
    :return: Density of the natural gas, kg/m3
    """
    return p / (Z*R*T)


def temperature_pseudocritical(ro_st):
    """
    Natural gas pseudocritical temperature (CH4 > 85%), K
    :param ro_st: (float) Natural gas density at standard parameters, kg/m3
    :return: (float) Pseudocritical temperature of the natural gas, K
    """
    return 155.24 * (0.564 + ro_st)


def pressure_pseudocritical(ro_st):
    """
    Natural gas pseudocritical pressure (CH4 > 85%), MPa
    :param ro_st: (float) Natural gas density at standard parameters, kg/m3
    :return: (float) Pseudocritical pressure of the natural gas, MPa
    """
    return 0.1737 * (26.831 - ro_st)


def density_relative(ro_st, ro_air_st):
    """
    Natural gas density relative to standard air density
    :param ro_st: (float) Density of the natural gas at standard parameters, kr/m3
    :param ro_air_st: (float) Density of the air at standard parameters, kg/m3
    :return: (float) Relative density of the natural gas, dimensionless
    """
    return ro_st / ro_air_st


def pressure_reduced(p, p_pkr):
    """
    :param p: (float) Absolute pressure of the natural gas, Pa
    :param p_pkr: (float) Pseudocritical pressure of the natural gas, MPa
    :return: (float) Reduced pressure of the natural gas, dimensionless
    """
    return p * 10**-6 / p_pkr


def temperature_reduced(t, t_pkr):
    """
    :param t: (float) Temperature of the natural gas, K
    :param t_pkr: Pseudocritical temperature of the natural gas, K
    :return: Reduced temperature of the natural gas, dimensionless
    """
    return t / t_pkr


def compressibility_factor(t_pr, p_pr):
    """
    :param t_pr: (float) Reduced temperature of the natural gas, dimensionless
    :param p_pr: (float) Reduced pressure of the natural gas, dimensionless
    :return: (float) Compressibility factor, dimensionless
    """
    tau = 1 - 1.68 * t_pr + 0.78 * t_pr**2 + 0.0107 * t_pr**3
    return 1 - 0.0241 * p_pr / tau

# def ng_compressibility_factor(pkr, tkr, p, t):
#     return 1 - 0.4273 * (p / pkr) * (t / tkr)**-3.668


def specific_isobaric_heat_capacity(p, t):
    """
    :param p: (float) Absolute pressure of the natural gas, Pa
    :param t: (float) Temperature of the natural gas, K
    :return: (float) Isobaric specific heat capacity Cp kJ/(kg*K)
    """
    return 1.695 + 1.838 * 10**-3 * t + 1.96 * 10**6 * (p * 10**-6 - 0.1) / t**3


def joile_tomson_factor(Cp, t):
    """
    :param Cp: (float) Isobaric specific heat capacity Cp kJ/(kg*K)
    :param t: (float) Temperature of the natural gas, K
    :return: (float) Joile-Tomson factor Di (K/MPa)
    """
    return (1 / Cp) * (0.98e6 / t**2 - 1.5)


def viscosity_dynamic(ro_st, T_pr, p_pr):
    """
    :param ro_st: (float) Density of the natural gas at standard parameters, kg/m3
    :param T_pr: (float) Reduced temperature of the natural gas at standard parameters, dimensionless
    :param p_pr: (float) Reduced pressure of the natural gas at standard parameters, dimensionless
    :return: (float) Dynamic viscosity of the natural gas, Pa*s
    """
    return 5.1e-6 * (1 + ro_st * (1.1 - 0.25 * ro_st)) * (0.037 + T_pr * (1 - 0.104 * T_pr)) * \
           (1 + p_pr**2 / (30 * (T_pr - 1)))


def viscosity_kinematic(mu, ro):
    """
    :param mu: Natural gas dynamic viscosity, Pa*s
    :param ro: Natural gas density, kg/m3
    :return: Natural gas kinematic viscosity, m2/s
    """
    return mu/ro
