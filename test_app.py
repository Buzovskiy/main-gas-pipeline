from scipy.optimize import fsolve
import math
import matplotlib.pyplot as plt

#
# def f(lambda_soil, *data):
#     w, T, ro = data
#     return 1e3 * math.log10(lambda_soil) - (-920.27 + 13.9 * w + 3.26 * T + 18.6 * ro - 0.36 * w**2)
# print(fsolve(f, 1, args=(10, 273+12, 1.5)))


def soil_heat_conductivity(w, T, ro, soil_type):
    """
    Heat conductivity of a soil, W/(m2*K)
    :param w: humidity, %
    :param T: temperature, K
    :param ro: density of a soil, kg/m3
    :param soil_type: (str) type of a soil
    :return: heat conductivity of a soil, W/(m2*K)
    """
    return {
        'sand': 10**((-134.2 + 23.89*w - 2.389*T + 442.98*ro - 0.276*w**2)*1e-3),
        'loam': 10**((-711.8 + 8.25*w + 2.48*T - 17.2*ro)*1e-3),
        'mixed_soil': 10**((-920.27 + 13.9 * w + 3.26 * T + 18.6 * ro - 0.36 * w**2)*1e-3),
    }[soil_type.lower()]


print(soil_heat_conductivity(10, 273+12, 1.5, 'loam'))

# _w = []
# _lambda_soil = []
# for w in range(10, 20, 1):
#     _w.append(w)
#     _lambda_soil.append(lambda_soil(w, T=273+12, ro=1.5))
#
#
# plt.plot(_w, _lambda_soil)
# plt.grid(True)
# plt.show()





# def f(x, *data):
#     a, b = data
#     return x**2 + a*x - b
#
#
# z = fsolve(f, 2, args=(2, 10))
# print(z)
#
# print(z[0]**2 + 2*z[0] - 10)

